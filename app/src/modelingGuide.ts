import { fetchJson, guideUrl, type FetchLike } from './publication.ts';

export interface GuideSource {
  readonly id: string;
  readonly title: string;
  readonly excerpt: string;
  readonly scope: string;
}
export interface GuideLesson {
  readonly id: string;
  readonly label: string;
  readonly title: string;
  readonly rule: string;
  readonly established_at: string;
  readonly scene: {
    readonly kind: 'comparison' | 'decomposition' | 'dependency' | 'responsibilities' | 'objects' | 'evidence';
    readonly parent?: string;
    readonly connector?: string;
    readonly caption: string;
    readonly items: readonly { readonly label: string; readonly text: string }[];
    readonly variants?: readonly {
      readonly id: string;
      readonly label: string;
      readonly description: string;
      readonly realizations: readonly { readonly label: string; readonly capability_indexes: readonly number[] }[];
    }[];
  };
  readonly question: string;
  readonly choices: readonly { readonly label: string; readonly feedback: string }[];
  readonly explanation: string;
  readonly contributor: {
    readonly criterion: string;
    readonly boundary: string;
    readonly scope: string;
    readonly source_refs: readonly string[];
  };
  readonly model_links: readonly { readonly id: string; readonly label: string }[];
}
export interface ModelingGuide {
  readonly glossary?: {
    readonly terms: readonly { id: string; name: string; label_fr?: string; definition: string; role?: string; examples?: readonly string[] }[];
    readonly model_term_ids: readonly string[];
  };
  readonly id: string;
  readonly version: string;
  readonly as_of: string;
  readonly title: string;
  readonly subtitle: string;
  readonly source_refs: readonly string[];
  readonly lessons: readonly GuideLesson[];
  readonly sources: readonly GuideSource[];
}
export interface GuideResponse {
  readonly schema_version: '1.0.0';
  readonly publication_version: string;
  readonly status: 'available' | 'unavailable';
  readonly message: string;
  readonly association?: { readonly scope: string; readonly note: string };
  readonly guide?: ModelingGuide;
}

/** Every read is pinned to the displayed publication, including live-current mode. */
export async function fetchModelingGuide(version: string, signal?: AbortSignal, fetcher: FetchLike = fetch): Promise<GuideResponse> {
  const raw = await fetchJson(guideUrl(version), signal, fetcher) as GuideResponse;
  if (!raw || raw.schema_version !== '1.0.0' || raw.publication_version !== version
    || !['available', 'unavailable'].includes(raw.status) || typeof raw.message !== 'string'
    || (raw.status === 'available' && (!raw.guide?.version || !Array.isArray(raw.guide.lessons) || !raw.guide.lessons.length || !Array.isArray(raw.guide.sources)))) {
    throw new Error('Le guide reçu ne correspond pas à cette publication.');
  }
  return raw;
}
