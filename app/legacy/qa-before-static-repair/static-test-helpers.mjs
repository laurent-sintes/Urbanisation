/** Resolve the same explicit static catalog used by the SPA. */
export async function staticModelUrl(base, version) {
  if (!version) {
    const response = await fetch(base + '/data/index.json');
    if (!response.ok) throw new Error(`Catalog HTTP ${response.status}`);
    version = (await response.json()).current_version;
  }
  return base + '/data/' + encodeURIComponent(version) + '/model.json';
}
