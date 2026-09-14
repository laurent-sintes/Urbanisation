#Requires -Version 5.1
[CmdletBinding()]
param(
    [ValidateRange(1024, 65535)]
    [int]$Port = 8765,
    [switch]$Browser,
    [switch]$NoBrowser,
    [switch]$Stop
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$atlasRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$atlasServer = Join-Path $atlasRoot 'app\server.py'
$atlasRuntime = Join-Path $atlasRoot 'app\.runtime'
$atlasStateFile = Join-Path $atlasRuntime "server-$Port.json"
$atlasUrl = "http://127.0.0.1:$Port/"

function Get-AtlasStatus {
    try {
        return Invoke-RestMethod -Uri ($atlasUrl + 'api/status') -TimeoutSec 2 -ErrorAction Stop
    }
    catch {
        return $null
    }
}

function Test-AtlasIdentity {
    param($Status)
    if ($null -eq $Status) { return $false }
    foreach ($field in @('appName', 'repositoryRoot', 'pid')) {
        if ($null -eq $Status.PSObject.Properties[$field]) { return $false }
    }
    try {
        return $Status.appName -eq 'FLOW Atlas' -and
            [string]::Equals([System.IO.Path]::GetFullPath([string]$Status.repositoryRoot), $atlasRoot, [System.StringComparison]::OrdinalIgnoreCase) -and
            [int]$Status.pid -gt 0
    }
    catch { return $false }
}

function Save-AtlasProcess {
    param($Status)
    $atlasProcess = Get-Process -Id ([int]$Status.pid) -ErrorAction Stop
    [void][System.IO.Directory]::CreateDirectory($atlasRuntime)
    @{
        appName = 'FLOW Atlas'
        repositoryRoot = $atlasRoot
        port = $Port
        pid = [int]$Status.pid
        processStartedUtc = $atlasProcess.StartTime.ToUniversalTime().ToString('o')
    } | ConvertTo-Json | Set-Content -LiteralPath $atlasStateFile -Encoding UTF8
}

function Find-AtlasPython {
    $candidates = @()
    foreach ($commandName in @('python', 'python3')) {
        $pythonCommand = Get-Command $commandName -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -ne $pythonCommand) { $candidates += $pythonCommand.Source }
    }
    if ($env:USERPROFILE) {
        $candidates += Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
    }
    foreach ($candidate in ($candidates | Select-Object -Unique)) {
        if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) { continue }
        # Les alias Windows Store vides ne sont pas des interpreteurs installes.
        if ($candidate -like '*\Microsoft\WindowsApps\*' -and (Get-Item -LiteralPath $candidate).Length -eq 0) { continue }
        try {
            $pythonProbe = & $candidate -c "import sys; print('FLOW_ATLAS_PYTHON_OK' if sys.version_info >= (3, 10) else 'OLD')" 2>$null
            if ($LASTEXITCODE -eq 0 -and $pythonProbe -eq 'FLOW_ATLAS_PYTHON_OK') { return $candidate }
        }
        catch { continue }
    }
    throw 'Python 3.10 ou plus recent est requis. Aucun interpreteur fonctionnel trouve dans PATH ou dans le runtime Codex utilisateur.'
}

function Test-AtlasPortAvailable {
    $atlasListener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, $Port)
    try {
        $atlasListener.Start()
        return $true
    }
    catch { return $false }
    finally { $atlasListener.Stop() }
}

function Open-AtlasWindow {
    if ($NoBrowser) { return }
    if (-not $Browser) {
        $edgeCandidates = @()
        foreach ($programRoot in @(${env:ProgramFiles(x86)}, $env:ProgramFiles, $env:LOCALAPPDATA)) {
            if ($programRoot) { $edgeCandidates += Join-Path $programRoot 'Microsoft\Edge\Application\msedge.exe' }
        }
        $edgeExecutable = $edgeCandidates | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
        if ($edgeExecutable) {
            # La fenetre visible est l'application demandee, le serveur reste cache.
            Start-Process -FilePath $edgeExecutable -ArgumentList @("--app=$atlasUrl")
            return
        }
    }
    Start-Process -FilePath $atlasUrl
}

$atlasStatus = Get-AtlasStatus
if ($Stop) {
    if (-not (Test-Path -LiteralPath $atlasStateFile -PathType Leaf)) {
        Write-Host "Aucun serveur suivi pour ce depot sur le port $Port."
        return
    }
    $atlasRecord = Get-Content -LiteralPath $atlasStateFile -Raw | ConvertFrom-Json
    foreach ($field in @('appName', 'repositoryRoot', 'port', 'pid', 'processStartedUtc')) {
        if ($null -eq $atlasRecord.PSObject.Properties[$field]) { throw 'Fichier de suivi incomplet. Aucun processus arrete.' }
    }
    if (-not (Test-AtlasIdentity $atlasStatus) -or $atlasRecord.appName -ne 'FLOW Atlas' -or
        $atlasRecord.repositoryRoot -ne $atlasRoot -or [int]$atlasRecord.port -ne $Port -or
        [int]$atlasRecord.pid -ne [int]$atlasStatus.pid) {
        throw 'Le serveur actif ne correspond pas au depot et au PID suivis. Aucun processus arrete.'
    }
    $atlasProcess = Get-Process -Id ([int]$atlasStatus.pid) -ErrorAction Stop
    $atlasRecordedStart = ([datetime]$atlasRecord.processStartedUtc).ToUniversalTime()
    if ($atlasProcess.StartTime.ToUniversalTime().Ticks -ne $atlasRecordedStart.Ticks) {
        throw 'Le PID a ete reutilise depuis le lancement. Aucun processus arrete.'
    }
    Stop-Process -InputObject $atlasProcess -ErrorAction Stop
    Remove-Item -LiteralPath $atlasStateFile -ErrorAction Stop
    Write-Host "FLOW Atlas arrete sur le port $Port."
    return
}

if (-not (Test-Path -LiteralPath (Join-Path $atlasRoot 'app\dist\index.html') -PathType Leaf)) {
    throw 'Interface Atlas non compilee. Depuis le projet : pnpm --dir app install, puis pnpm --dir app build. Le serveur peut etre arrete avec -Stop meme sans compilation.'
}

if (Test-AtlasIdentity $atlasStatus) {
    Save-AtlasProcess $atlasStatus
    Write-Host "FLOW Atlas est deja disponible : $atlasUrl"
    Open-AtlasWindow
    return
}
if (-not (Test-AtlasPortAvailable)) {
    throw "Le port $Port est utilise par un autre service. Relance avec -Port 8766, par exemple."
}
if (-not (Test-Path -LiteralPath $atlasServer -PathType Leaf)) {
    throw "Serveur introuvable : $atlasServer"
}

$atlasPython = Find-AtlasPython
& $atlasPython -c "import sys; sys.path.insert(0, sys.argv[1]); import scripts.structured_io" $atlasRoot
if ($LASTEXITCODE -ne 0) {
    throw 'Lecteur YAML indisponible. Installer depuis la racine : python -m pip install --target .tools/yaml-runtime -r requirements.txt'
}
[void][System.IO.Directory]::CreateDirectory($atlasRuntime)
$atlasStdout = Join-Path $atlasRuntime "server-$Port.stdout.log"
$atlasStderr = Join-Path $atlasRuntime "server-$Port.stderr.log"
$atlasStartedProcess = Start-Process -FilePath $atlasPython -ArgumentList @('-u', ('"' + $atlasServer + '"'), '--port', [string]$Port) `
    -WorkingDirectory $atlasRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput $atlasStdout -RedirectStandardError $atlasStderr
$atlasTimer = [System.Diagnostics.Stopwatch]::StartNew()
while ($atlasTimer.Elapsed.TotalSeconds -lt 20) {
    $atlasStatus = Get-AtlasStatus
    if (Test-AtlasIdentity $atlasStatus) {
        if ([int]$atlasStatus.pid -ne $atlasStartedProcess.Id) {
            throw 'Un autre serveur a pris le port pendant le lancement. Consulte les journaux dans app/.runtime.'
        }
        Save-AtlasProcess $atlasStatus
        Write-Host "FLOW Atlas : $atlasUrl"
        Open-AtlasWindow
        return
    }
    $atlasStartedProcess.Refresh()
    if ($atlasStartedProcess.HasExited) {
        throw "Le serveur a quitte avant de devenir disponible. Consulte $atlasStderr"
    }
    Start-Sleep -Milliseconds 200
}
throw "Le serveur ne repond pas encore. Consulte $atlasStderr puis relance le lanceur pour verifier son etat."
