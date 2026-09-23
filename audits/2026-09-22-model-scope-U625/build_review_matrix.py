"""Reproduce the dated U625 review matrix from its captured audit inputs.

This only writes audit artifacts next to this script, never the source model.
Semantic assessments are the explicit Codex review recorded during U625.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "scope-extract.json").read_text(encoding="utf-8"))
checks = json.loads((ROOT / "market-metadata-checks.json").read_text(encoding="utf-8"))
market = {(r["kind"], r["id"]): r for r in checks["entries"]}

node_notes = {
    "universe-supply": ("A01 A02", "Périmètre général étayé. Actualiser le renvoi au plan d'ensemble D17 et la place des politiques maîtrisées ; services numériques/humains au service de ce Domain, sans extension à toute l'entreprise."),
    "business-references": ("A01 A07", "Sept références conservées, gouvernances présentes ; finalité commune avec les policies encore absente du scope et de la présentation canonique."),
    "D04": ("A01 A03 A06 A07", "Demand doit porter besoins, exigences et promesse U595. Ancien Service Order encore cité. Sources Salesforce IT/TMF641 partielles pour cette finalité."),
    "D01": ("A01 A07", "Stock et apports attendus à distinguer lors de la refonte. Réservation, position, mouvement et protection restent des responsabilités distinctes ; pas de suppression déduite du changement de Purpose."),
    "D06": ("A03 A04 A07", "Actualiser Task et document optionnel U616/U617, frontière d'exécution, reprise ciblée et renvoi vers Demand pour la promesse."),
    "D15": ("A01 A04", "La promesse reste utile ; son appartenance à un Purpose séparé et son articulation avec les décisions du plan ne reflètent pas U595. ATP/CTP/PTP restent des repères marché possibles."),
    "D03": ("A01 A04 A07", "Compléter l'arbitrage avant exécution, y compris demandes fermes ; finalité commune avec le travail de plan à rendre explicite sans prendre en charge les réalisations."),
    "D05": ("A01 A07", "Responsabilités d'ajustement identifiées ; les rattacher au cadrage du plan sans déduire un déplacement global ni étendre la preuve scientifique à toutes les capacités."),
    "D17": ("A02 A07", "Plan d'ensemble, demande prévisionnelle et plan amont sont décrits à des mailles incompatibles. Définition, scope, enfant et positions marché à réaligner."),
}

term_notes = {
    "TER001": ("A06", "Définition méthodologique ; organiser son autorité et son renvoi depuis le glossaire métier. Capability manque comme entrée autonome du glossaire méthodologique."),
    "TER004": ("A06", "Clarifier le renvoi vers TER060 Article et la distinction avec unité physique / unité de gestion ; pas de fusion automatique."),
    "TER007": ("A06", "Alias ou distinction à rendre explicite avec TER055 ; aucune contradiction certaine déduite de la proximité."),
    "TER026": ("A06", "Notion de réalisation relevant du vocabulaire méthodologique ; conserver identifiant et liens historiques."),
    "TER027": ("A06", "Notion principalement méthodologique ; préciser son autorité et éviter deux définitions concurrentes."),
    "TER028": ("A06", "Distinction produit/capacité à préserver dans le vocabulaire méthodologique."),
    "TER029": ("A05 A06", "Regroupement de lecture distinct de Purpose fondé sur une finalité ; faire un renvoi explicite, sans les assimiler."),
    "TER030": ("A05 A06", "Domaine méthodologique à articuler avec MOD008 et la hiérarchie U624 ; éviter une assimilation automatique au sous-domaine DDD."),
    "TER055": ("A06", "Alias ou distinction à expliciter avec TER007 ; les usages Stock/Inventory/Goods Movement peuvent rester documentés."),
    "TER060": ("A06", "Articuler Article avec TER004 et les unités ; préserver les différences de granularité."),
    "TER066": ("A03", "Backing Service Order encore canonique ; nom et définition à aligner avec le document Service Order éventuellement produit par une Task U616."),
    "TER071": ("A06", "Déplacement physique défini trop largement pour expliquer à lui seul la distinction locale transfert / consignation / retour. Ajouter la frontière d'intention."),
    "TER072": ("A06", "Customer Return Order reste le nom du glossaire, alors que D04.l est Return Order U612 ; synchroniser sans réintroduire les comportements abandonnés."),
}

preserved_terms = {
    "TER016": "Distinction réservation / protection à conserver ; aucun nouvel écart identifié.",
    "TER056": "Le candidat Inventory Ledger Management est explicitement non adopté ; ce statut exploratoire n'est pas une erreur à effacer.",
    "TER069": "Sales Order reste l'intention de vente ; Consignment Issue doit être expliqué comme comportement, pas comme nouvelle famille autonome.",
    "TER070": "L'achat de biens ou prestations reste compatible avec U619 ; ne pas transformer toute sollicitation de Service en achat.",
    "TER073": "Le retour vers fournisseur et ses suites restent utiles ; ne pas confondre son sens avec une reprise de consignation sans motif de retour.",
    "TER075": "Service physique, humain ou numérique déjà correctement couvert ; la lacune porte sur la Task et le document qui l'entourent.",
    "TER080": "Sens local de Réassort explicitement distingué des usages plus larges du marché ; pas de normalisation automatique.",
    "TER088": "Service Provider déjà nommé ; conserver la différence fournisseur métier / connecteur de produit, et relier la policy locale.",
}

meta_notes = {
    "MOD001": ("À conserver", "Convention Decision incluant ses calculs. Références utilisateur présentes ; pas de comparaison de fiche autonome à inventer."),
    "MOD002": ("À conserver", "Planning inclut actualisation, simulation/analyse et application du plan retenu ; mobilise des décisions distinctes. U537/U538 et CMP220 tracés."),
    "MOD003": ("À conserver", "Management distingue tenue durable des états/engagements et cadre Policy. Le nom Management d'une capacité ne suffit pas à la reclasser."),
    "MOD004": ("À conserver", "Application transactionnelle reste distincte du choix et de la réalisation physique ; convention locale sourcée."),
    "MOD005": ("À conserver", "Couverture qualifiée par objet, périmètre, horizon et critère. Ne vaut pas preuve de réalisation installée."),
    "MOD006": ("À conserver", "Comportement terminal et justification de décomposition présents ; typologie et CMP145 référencés. Audit U431 non rouvert."),
    "MOD007": ("A05", "Sept natures dont Policy présentes, distinctes de la gouvernance. Remplacer l'exemple d'une Area Policy Management par un exemple compatible U618/U624 ; pas de reclassement global."),
    "MOD008": ("A05", "Définition avec Purposes présente. Compléter la traçabilité U624 et harmoniser les documents de méthode ; références métier auxiliaires sans cinquième niveau descriptif imposé."),
    "MOD013": ("A05 A07", "Purpose/Finalité et définition U624 présents. Relier la comparaison élargie U620–U624 à la fiche ; garder convention FLOW distincte d'un standard de marché."),
    "MOD009": ("À conserver", "Les trois gouvernances des références sont décrites ; un sujet peut présenter des responsabilités distinctes sans fusion de données."),
    "MOD010": ("A08", "Appartenance, présentation et interactions distinguées. Compléter le contrôle de rattachement Purpose ; une dépendance ne crée pas de parent."),
    "MOD011": ("À conserver", "Nature de comportement distincte de la nature de capacité et de sa gouvernance ; policy_strategy ne remplace pas policy."),
    "MOD012": ("À conserver", "Information distincte d'un modèle de données implémentable ; catalogue interne masqué et sans extension, conformément U470."),
    "MOD014": ("À conserver", "Domain-managed = CRUD local ; Projection = vérité externe ; Domain-View = vue construite et rafraîchie par le domaine. Valeurs indépendantes du type."),
}

def cell(value):
    return str(value).replace("|", " / ").replace("\n", " ")

def table(lines, header, rows):
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    lines.extend("| " + " | ".join(cell(v) for v in row) + " |" for row in rows)
    lines.append("")

lines = [
    "# Revue détaillée — U625", "",
    "État capturé le 22 septembre 2026. Lecture sémantique au périmètre glossaire / métamodèle / Domain / Purpose, complétée par le contrôle exhaustif des métadonnées marché. « Aucun écart supplémentaire identifié » ne signifie ni accord métier ni relecture externe exhaustive des sources. Les constats A01–A08 sont détaillés dans [rapport.md](rapport.md).", "",
    "## Domain et Purposes", "",
]
rows = []
for item in data["nodes"]:
    identifier = item["id"]
    finding, note = node_notes[identifier]
    evidence = market[("node", identifier)]
    rows.append([identifier, item["fields"]["name"], evidence["comparisons"], finding, note])
table(lines, ["ID", "Nom courant", "Rapprochements", "Constats", "Revue"], rows)

lines.extend(["## Métamodèle", ""])
rows = []
for item in data["metamodel_terms"]:
    state, note = meta_notes[item["id"]]
    rows.append([item["id"], item["name"], state, note])
table(lines, ["ID", "Terme", "Résultat", "Revue"], rows)
lines.extend([
    "Compléments hors des 14 entrées : autorité de Capability (TER001), distinction du niveau Purpose et du champ finality, mise à jour du guide U458. Deux termes portent une comparaison méthodologique explicite ; les autres ont des sources utilisateur ou des annexes. Ce constat de format ne démontre pas une absence de preuve marché.", "",
    "## Glossaire métier — 112 entrées", "",
])
rows = []
for item in data["terms"]:
    identifier = item["id"]
    finding, note = term_notes.get(identifier, ("—", preserved_terms.get(identifier, "Aucun écart supplémentaire identifié dans le périmètre U625 ; références et limites présentes.")))
    evidence = market[("term", identifier)]
    rows.append([identifier, item["name"], evidence["comparisons"], finding, note])
table(lines, ["ID", "Nom courant", "Rapprochements", "Constats", "Revue"], rows)
lines.extend([
    "## Notions à couvrir ou relier explicitement", "",
    "Task ; consignation et ses deux sens ; Consignment Fill-up ; Consignment Pick-up ; Consignment Issue ; distinction Service Provider / Service Catalog / Service Provider Policy. Les ajouts de définitions n'impliquent pas de nouveaux nœuds de capacité. Aucun identifiant retiré ne doit être réutilisé.", "",
    "## Reproduction", "",
    "`python audits/2026-09-22-model-scope-U625/build_review_matrix.py` régénère uniquement cette matrice à partir des pièces d'audit capturées et des appréciations explicites du script ; cette commande ne réaudite pas un backlog ultérieur.", "",
])
(ROOT / "revue-detaillee.md").write_text("\n".join(lines), encoding="utf-8")
print(f"U625 matrix: {len(data['nodes'])} nodes, {len(data['metamodel_terms'])} metamodel terms, {len(data['terms'])} glossary terms.")
