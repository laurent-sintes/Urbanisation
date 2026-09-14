"""Named publication descriptors and an atomic technical index for Atlas."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


try:
    from .structured_io import read
except ImportError:
    from structured_io import read


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def within(folder, relative):
    if not isinstance(relative, str) or any(c in relative for c in ('\\', ':', '\0')):
        raise ValueError('Invalid publication path')
    parts=relative.split('/')
    if any(p in ('', '.', '..') for p in parts): raise ValueError('Invalid publication path')
    path=folder.joinpath(*parts).resolve()
    if not path.is_relative_to(folder.resolve()): raise ValueError('Publication escapes release directory')
    return path


def legacy_descriptor(folder, version):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}\.[1-9]\d*', version): raise ValueError('Invalid publication version')
    manifest=read(within(folder, version+'/manifest.json'))
    relative=version+'/'+manifest.get('model_path', 'model.json')
    path=within(folder, relative); model=read(path)
    return {'schema_version':'1.0.0','model_id':model['model_id'],'space':'release','version':version,
            'revision':model.get('revision'), 'published_at':None, 'last_modified':model.get('last_modified'),
            'path':relative,'sha256':digest(path),
            'note':'Publication historique ; horodatage précis non enregistré.'}


def descriptors(folder):
    folder=Path(folder)
    if not (folder/'index.json').exists():
        return [legacy_descriptor(folder,p.name) for p in folder.iterdir() if p.is_dir() and (p/'manifest.json').is_file()]
    index=read(folder/'index.json'); result=[]
    entries=index['publications']
    if len({e['descriptor'] for e in entries}) != len(entries): raise ValueError('Duplicate publication descriptor')
    if index['current'] not in {e['descriptor'] for e in entries}: raise ValueError('Current descriptor missing from index')
    for entry in entries:
        path=within(folder,entry['descriptor'])
        if digest(path)!=entry['sha256']: raise ValueError('Publication descriptor hash mismatch')
        item=read(path); item['descriptor']=entry['descriptor'];result.append(item)
    if len({e['version'] for e in result})!=len(result):raise ValueError('Duplicate publication version')
    return result


def resolve_release(folder, version=None):
    folder=Path(folder)
    if (folder/'index.json').exists():
        values=descriptors(folder); current=read(folder/'index.json')['current']
        selected=[v for v in values if (v['version']==version if version else v['descriptor']==current)]
        if len(selected)!=1: raise ValueError('Unknown publication version')
        item=selected[0]
    elif version:
        item=legacy_descriptor(folder,version)
    else:
        item=read(folder/'current.json')
    model_path=within(folder,item['path'])
    if digest(model_path)!=item['sha256']:raise ValueError('Published model hash mismatch')
    model=read(model_path)
    if model['version']!=item['version']:raise ValueError('Published model version mismatch')
    if item.get('revision') is not None:
        for key in ('revision','last_modified'):
            if model.get(key)!=item[key]:raise ValueError('Published model metadata mismatch: '+key)
    if item.get('release_notes'):
        if digest(within(folder,item['release_notes']))!=item['release_notes_sha256']:raise ValueError('Release notes hash mismatch')
    return item


def catalog(folder):
    current=resolve_release(folder)
    values=descriptors(Path(folder))
    values.sort(key=lambda d: tuple(map(int,re.split(r'[-.]',d['version']))),reverse=True)
    return {'current_version':current['version'],'versions':[{k:d.get(k) for k in ('version','revision','published_at','last_modified','release_notes','descriptor')} for d in values]}


def register(folder, release, notes_path, write, activate):
    """Write immutable descriptors, activate the index last, retain old pointer bytes."""
    folder=Path(folder); version=release['version']
    stamp=datetime.now(timezone.utc)
    filename=f"urbanisation-v{release['revision']:03d}-{stamp.strftime('%Y-%m-%d-%H%M%S')}.yaml"
    descriptor={'schema_version':'1.0.0','model_id':release['model_id'],'space':'release',
                'version':version,'revision':release['revision'],'published_at':stamp.isoformat(timespec='microseconds').replace('+00:00','Z'),
                'last_modified':release['last_modified'],'path':version+'/model.yaml','sha256':digest(folder/version/'model.yaml'),
                'release_notes':notes_path,'release_notes_sha256':digest(folder/notes_path)}
    write(folder/filename,descriptor)
    if (folder/'index.json').exists():
        descriptors(folder)  # Refuse to extend an inconsistent index.
        previous=read(folder/'index.json')['publications']
    else:
        previous=[]
        for legacy in descriptors(folder):
            if legacy['version']==version:continue
            name='urbanisation-'+legacy['version']+'-legacy.json'
            write(folder/name,legacy)
            previous.append({'descriptor':name,'sha256':digest(folder/name)})
    index={'schema_version':'1.0.0','model_id':release['model_id'],'current':filename,
           'publications':[{'descriptor':filename,'sha256':digest(folder/filename)},*previous]}
    activate(folder/'index.json',index)
    old=folder/'current.json'
    if old.exists():
        legacy_dir=folder/'legacy';legacy_dir.mkdir(exist_ok=True)
        old_version=read(old)['version']
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}\.[1-9]\d*',old_version):raise ValueError('Invalid legacy pointer version')
        old.rename(legacy_dir/('current-'+old_version+'.json'))
    return filename
