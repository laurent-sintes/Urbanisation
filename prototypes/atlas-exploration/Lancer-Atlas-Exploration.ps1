#Requires -Version 5.1
[CmdletBinding()]
param(
    [ValidateRange(1024, 65535)]
    [int]$Port = 8767,
    [switch]$Browser,
    [switch]$NoBrowser,
    [switch]$Stop
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$explorationRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$explorationRepository = [System.IO.Path]::GetFullPath((Join-Path $explorationRoot '..\..'))
$explorationRuntime = Join-Path $explorationRoot '.runtime'
$explorationStateFile = Join-Path $explorationRuntime "preview-$Port.json"
$explorationUrl = "http://127.0.0.1:$Port/"

function Get-ExplorationStatus {
    try { return Invoke-RestMethod -Uri ($explorationUrl + '__atlas_experiment') -TimeoutSec 2 -ErrorAction Stop }
    catch { return $null }
}

function Test-ExplorationRepository {
    param([string]$Candidate)
    try {
        $normalized = [System.IO.Path]::GetFullPath($Candidate).TrimEnd([char[]]@('\', '/'))
        return [string]::Equals($normalized, $explorationRepository.TrimEnd([char[]]@('\', '/')), [System.StringComparison]::OrdinalIgnoreCase)
    }
    catch { return $false }
}

function Test-ExplorationIdentity {
    param($Status)
    if ($null -eq $Status) { return $false }
    foreach ($field in @('appName', 'repositoryRoot', 'pid')) {
        if ($null -eq $Status.PSObject.Properties[$field]) { return $false }
    }
    try {
        return $Status.appName -eq 'FLOW Atlas Exploration' -and
            (Test-ExplorationRepository ([string]$Status.repositoryRoot)) -and [int]$Status.pid -gt 0
    }
    catch { return $false }
}

function Save-ExplorationProcess {
    param($Status)
    if (-not (Test-ExplorationIdentity $Status)) { throw 'Identite du prototype non verifiee.' }
    $explorationProcess = Get-Process -Id ([int]$Status.pid) -ErrorAction Stop
    [void][System.IO.Directory]::CreateDirectory($explorationRuntime)
    @{
        appName = 'FLOW Atlas Exploration'
        repositoryRoot = $explorationRepository
        prototypeRoot = $explorationRoot
        port = $Port
        pid = [int]$Status.pid
        processStartedUtc = $explorationProcess.StartTime.ToUniversalTime().ToString('o')
    } | ConvertTo-Json | Set-Content -LiteralPath $explorationStateFile -Encoding UTF8
}

function Test-ExplorationPortAvailable {
    $explorationListener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, $Port)
    try { $explorationListener.Start(); return $true }
    catch { return $false }
    finally { $explorationListener.Stop() }
}

function Find-ExplorationNode {
    $candidates = @()
    $nodeCommand = Get-Command node -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -ne $nodeCommand) { $candidates += $nodeCommand.Source }
    if ($env:USERPROFILE) {
        $candidates += Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
    }
    foreach ($candidate in ($candidates | Select-Object -Unique)) {
        if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) { continue }
        try {
            $nodeProbe = & $candidate -p "Number(process.versions.node.split('.')[0]) >= 24 ? 'ATLAS_EXPLORATION_NODE_OK' : 'OLD'" 2>$null
            if ($LASTEXITCODE -eq 0 -and $nodeProbe -eq 'ATLAS_EXPLORATION_NODE_OK') { return $candidate }
        }
        catch { continue }
    }
    throw 'Node.js 24 ou plus recent est requis. Aucun runtime fonctionnel dans PATH ou dans le runtime Codex utilisateur.'
}

function Ensure-ExplorationAtlasApi {
    $atlasLauncher = Join-Path $explorationRepository 'Lancer-FLOW-Atlas.ps1'
    if (-not (Test-Path -LiteralPath $atlasLauncher -PathType Leaf)) { throw "Lanceur Atlas introuvable : $atlasLauncher" }
    # This existing launcher checks identity and only starts the API when needed.
    & $atlasLauncher -Port 8765 -NoBrowser
    $atlasApiStatus = Invoke-RestMethod -Uri 'http://127.0.0.1:8765/api/status' -TimeoutSec 3 -ErrorAction Stop
    if ($null -eq $atlasApiStatus.PSObject.Properties['appName'] -or
        $null -eq $atlasApiStatus.PSObject.Properties['repositoryRoot'] -or
        $atlasApiStatus.appName -ne 'FLOW Atlas' -or
        -not (Test-ExplorationRepository ([string]$atlasApiStatus.repositoryRoot))) {
        throw 'Le port 8765 ne sert pas l API FLOW Atlas de ce depot.'
    }
}

function Open-ExplorationBrowser {
    if ($Browser -and -not $NoBrowser) {
        # A visible browser is opened only on the explicit -Browser request.
        Start-Process -FilePath $explorationUrl
    }
}

$explorationStatus = Get-ExplorationStatus
if ($Stop) {
    if (-not (Test-Path -LiteralPath $explorationStateFile -PathType Leaf)) {
        Write-Host "Aucun prototype suivi pour ce depot sur le port $Port."
        return
    }
    $explorationRecord = Get-Content -LiteralPath $explorationStateFile -Raw | ConvertFrom-Json
    foreach ($field in @('appName', 'repositoryRoot', 'prototypeRoot', 'port', 'pid', 'processStartedUtc')) {
        if ($null -eq $explorationRecord.PSObject.Properties[$field]) { throw 'Suivi incomplet. Aucun processus arrete.' }
    }
    if (-not (Test-ExplorationIdentity $explorationStatus) -or
        $explorationRecord.appName -ne 'FLOW Atlas Exploration' -or
        -not (Test-ExplorationRepository ([string]$explorationRecord.repositoryRoot)) -or
        [System.IO.Path]::GetFullPath([string]$explorationRecord.prototypeRoot) -ne $explorationRoot -or
        [int]$explorationRecord.port -ne $Port -or [int]$explorationRecord.pid -ne [int]$explorationStatus.pid) {
        throw 'Le serveur actif ne correspond pas au depot, au port et au PID suivis. Aucun processus arrete.'
    }
    $explorationProcess = Get-Process -Id ([int]$explorationStatus.pid) -ErrorAction Stop
    $explorationRecordedStart = ([datetime]$explorationRecord.processStartedUtc).ToUniversalTime()
    if ($explorationProcess.StartTime.ToUniversalTime().Ticks -ne $explorationRecordedStart.Ticks) {
        throw 'Le PID a ete reutilise depuis le lancement. Aucun processus arrete.'
    }
    Stop-Process -InputObject $explorationProcess -ErrorAction Stop
    if (-not $explorationProcess.WaitForExit(5000)) { throw 'Le processus du prototype ne confirme pas encore son arret.' }
    Remove-Item -LiteralPath $explorationStateFile -ErrorAction Stop
    Write-Host "Prototype Atlas Exploration arrete sur le port $Port. L API Atlas sur 8765 reste disponible."
    return
}

if (Test-ExplorationIdentity $explorationStatus) {
    Ensure-ExplorationAtlasApi
    Save-ExplorationProcess $explorationStatus
    Write-Host "Atlas Exploration est deja disponible : $explorationUrl"
    Open-ExplorationBrowser
    return
}
if (-not (Test-ExplorationPortAvailable)) { throw "Le port $Port est occupe par un autre service. Aucun service n a ete arrete." }

$explorationEntry = Join-Path $explorationRoot 'dist\index.html'
$explorationVite = Join-Path $explorationRoot 'node_modules\vite\bin\vite.js'
if (-not (Test-Path -LiteralPath $explorationEntry -PathType Leaf)) {
    throw 'Le prototype n est pas construit. Dans prototypes/atlas-exploration : node scripts/generate-likec4.mjs puis pnpm run build. Voir README.md.'
}
if (-not (Test-Path -LiteralPath $explorationVite -PathType Leaf)) {
    throw 'Vite manque dans node_modules. Installer explicitement les dependances avec pnpm install --frozen-lockfile. Le lanceur ne telecharge rien.'
}
$explorationNode = Find-ExplorationNode
Ensure-ExplorationAtlasApi
[void][System.IO.Directory]::CreateDirectory($explorationRuntime)
$explorationStdout = Join-Path $explorationRuntime "preview-$Port.stdout.log"
$explorationStderr = Join-Path $explorationRuntime "preview-$Port.stderr.log"
$explorationStartedProcess = Start-Process -FilePath $explorationNode `
    -ArgumentList @(('"' + $explorationVite + '"'), 'preview', '--host', '127.0.0.1', '--port', [string]$Port, '--strictPort') `
    -WorkingDirectory $explorationRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput $explorationStdout -RedirectStandardError $explorationStderr
$explorationTimer = [System.Diagnostics.Stopwatch]::StartNew()
while ($explorationTimer.Elapsed.TotalSeconds -lt 20) {
    $explorationStatus = Get-ExplorationStatus
    if (Test-ExplorationIdentity $explorationStatus) {
        if ([int]$explorationStatus.pid -ne $explorationStartedProcess.Id) { throw 'Un autre processus a pris le port pendant le lancement. Consulte .runtime.' }
        Save-ExplorationProcess $explorationStatus
        Write-Host "Atlas Exploration : $explorationUrl"
        Open-ExplorationBrowser
        return
    }
    $explorationStartedProcess.Refresh()
    if ($explorationStartedProcess.HasExited) { throw "Le prototype a quitte avant de devenir disponible. Consulte $explorationStderr" }
    Start-Sleep -Milliseconds 200
}
throw "Le prototype ne repond pas encore. Consulte $explorationStderr puis relance le lanceur pour verifier son etat."
