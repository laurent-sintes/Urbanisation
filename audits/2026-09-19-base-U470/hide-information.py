"""Withdraw the reader entry points while preserving the catalogue and its code."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def change(path,replacements):
 p=ROOT/path;s=p.read_text(encoding='utf-8')
 for old,new in replacements:
  assert old in s,(path,old)
  s=s.replace(old,new)
 p.write_text(s,encoding='utf-8')
change('app/src/components/BusinessSheet.tsx',[
 ("import { informationForNode } from '../information';\n",''),
 ("import { InformationSummary } from './InformationPage';\n",''),
 ('  const information = informationForNode(model, node.id);\n',''),
 ("information.length > 0 && ['information', 'Informations'], ",''),
 ('      <InformationSummary model={model} nodeId={node.id} items={information}/>\n',''),
])
change('app/src/components/Sidebar.tsx',[
 (', Waypoints',''),('  onOpenInformation: (id?: string) => void;\n',''),
 (', onOpenInformation }: Props)', ' }: Props)'),
 ("    : route.type === 'information' ? model.information.map(item => ({ id: item.id, kind: 'information', name: item.name, excerpt: item.question, score: 0 }))\n",''),
 ('<option value="information">Informations métier</option>',''),
 ("result.kind === 'information' ? onOpenInformation(result.id) : ",''),
 ("result.kind === 'information' ? <Waypoints size={22}/> : ",''),
 ("result.kind === 'information' ? 'Information métier' : ",''),
 ('      <button className="glossary-nav information-nav" onClick={() => onOpenInformation()} aria-current={route.view === \'information\' ? \'page\' : undefined}><Waypoints size={17}/>Informations métier</button>\n',''),
])
change('app/src/App.tsx',[
 ("import { InformationPage } from './components/InformationPage';\n",''),
 (', Waypoints',''),(" || view === 'information'",''),
 ("  const openInformation = useCallback((information = '') => {\n    changeRoute({ view: 'information', information, node: '', term: '', principle: '', section: '', scope: '', relation: '', source: '', anchor: '', sourceId: '', query: '', type: '', status: '' });\n    setDrawer(false);\n    setTimeout(() => heading.current?.focus({ preventScroll: true }), 30);\n  }, [changeRoute]);\n",''),
 (' onOpenInformation={openInformation}',''),
 ("view === 'information' ? 'Informations métier' : ",''),
 ("view === 'information' ? <Waypoints size={30}/> : ",''),
 ("view === 'information' ? 'LE CONTENU MÉTIER' : ",''),
 ("view === 'information' ? 'Ce que les capacités connaissent, utilisent et font évoluer, avec le sens et le contexte nécessaires.' : ",''),
 ("view === 'information' ? <InformationPage key={model.version} model={model} selected={route.information} nodeId={route.node || undefined}/> : ",''),
])
change('app/src/search.ts',[
 ("import { informationSearchText } from './information.ts';\n",''),
 (" | 'information'",''),
 ("    ...model.information.map(item => ({ id: item.id, kind: 'information' as const, name: item.name,\n      excerpt: informationSearchText(item), score: 0 })),\n",''),
])
change('app/src/navigation.ts',[
 ("const requestedView = p.get('view') === 'sheet'", "// U470: old information links return to the model in the same publication.\n  if (p.get('view') === 'information') p.set('view', node && !legacyRoots.includes(node) ? 'sheet' : 'map');\n  if (p.get('type') === 'information') p.delete('type');\n  const requestedView = p.get('view') === 'sheet'"),
 ("    ...(view === 'information' && p.has('information') ? { information: p.get('information') || '' } : {}),\n",''),
])
change('app/src/components/ModelLinks.tsx',[
 ('term?.short_description || String(', 'term?.definition || term?.short_description || String('),
])
print('Information navigation, search, sheet cards and legacy route access withdrawn; source catalogue retained.')
