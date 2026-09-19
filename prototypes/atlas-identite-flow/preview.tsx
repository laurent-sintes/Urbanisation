import { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { createPortal } from 'react-dom';
import { App } from '../../app/src/App';
import '../../app/src/styles.css';
import './theme.css';
import './preview.css';
import flowLogo from './assets/flow-original.png';
import beaumanoirLogo from './assets/beaumanoir-original.png';

const palette = [
  ['Vert FLOW', '#236159', 'Navigation, liens et actions'],
  ['Menthe', '#D9F2EA', 'Sélection et surfaces légères'],
  ['Lavande', '#DAE0F2', 'Surfaces secondaires'],
  ['Sable', '#EADFCD', 'Repère des référentiels'],
  ['Pêche', '#FFD8B2', 'Accent graphique ponctuel'],
  ['Blanc cassé', '#FCFDFD', 'Fond de l’application'],
];

function Preview() {
  const [theme, setTheme] = useState<'flow' | 'current'>('flow');
  const [slots, setSlots] = useState<{ flow: Element | null; beaumanoir: Element | null }>({ flow: null, beaumanoir: null });
  const dialog = useRef<HTMLDialogElement>(null);
  useEffect(() => {
    const host = (selector: string) => {
      const parent = document.querySelector(selector);
      if (!parent) return null;
      const element = document.createElement('span');
      parent.append(element);
      return element;
    };
    // Dedicated empty hosts keep the comparison wrapper separate from App's React children.
    const flow = host('.brand-symbol');
    const beaumanoir = host('.topbar-context');
    setSlots({ flow, beaumanoir });
    return () => { flow?.remove(); beaumanoir?.remove(); };
  }, []);
  useEffect(() => { document.documentElement.dataset.atlasBrand = theme; }, [theme]);
  return <>
    <App/>
    {slots.flow && createPortal(<img className="flow-source-mark" src={flowLogo} alt=""/>, slots.flow)}
    {slots.beaumanoir && createPortal(<img className="beaumanoir-source-logo" src={beaumanoirLogo} alt="Groupe Beaumanoir"/>, slots.beaumanoir)}
    <aside className="proposal-controls" aria-label="Comparer la proposition graphique">
      <span className="proposal-label">Proposition graphique</span>
      <div className="proposal-switch" role="group" aria-label="Identité graphique">
        <button aria-pressed={theme === 'current'} onClick={() => setTheme('current')}>Actuel</button>
        <button aria-pressed={theme === 'flow'} onClick={() => setTheme('flow')}>FLOW</button>
      </div>
      <nav aria-label="Vues de la proposition"><a href="#node=universe-supply&view=map">Univers</a><a href="#node=business-references&view=map">Référentiels</a><a href="#node=D01.f&view=sheet">Fiche</a></nav>
      <button className="proposal-palette-button" onClick={() => dialog.current?.showModal()}>Palette et logos</button>
    </aside>
    <dialog className="brand-dialog" ref={dialog}>
      <button className="dialog-close" aria-label="Fermer la palette" onClick={() => dialog.current?.close()}>Fermer ×</button>
      <span className="dialog-kicker">Template projet FLOW</span><h2>Une identité commune pour Atlas</h2>
      <p>Les couleurs ci-dessous proviennent des formes des masques du PowerPoint. Les deux PNG sont extraits à l’identique du fichier fourni.</p>
      <div className="brand-palette">{palette.map(([name, hex, purpose]) => <div key={hex}><span className="swatch" style={{ background: hex }}/><strong>{name}</strong><code>{hex}</code><small>{purpose}</small></div>)}</div>
      <div className="brand-originals"><figure><img src={flowLogo} alt="Logo FLOW intégral"/><figcaption><a href={flowLogo} download="flow-original.png">Logo FLOW original</a></figcaption></figure><figure><img src={beaumanoirLogo} alt="Logo Groupe Beaumanoir intégral"/><figcaption><a href={beaumanoirLogo} download="beaumanoir-original.png">Logo Beaumanoir original</a></figcaption></figure></div>
      <p className="brand-note">Dans l’en-tête, l’emblème FLOW est cadré pour un usage compact, à côté du nom Atlas. Les fichiers originaux conservent le logo complet et sa signature. Les couleurs de statut restent indépendantes de l’identité graphique.</p>
    </dialog>
  </>;
}

if (!location.hash) history.replaceState({}, '', '#node=universe-supply&view=map');
createRoot(document.getElementById('root')!).render(<Preview/>);
