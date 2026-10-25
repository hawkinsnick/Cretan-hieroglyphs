# Cretan Hieroglyphic Open Corpus

[Scoped academic controls](docs/CLOSURE-CONTROLS.md) make exclusions and unresolved source qualifications explicit in researcher retrieval.


## Use the AI research skill

Start with [the individual skill](ai-skill/SKILL.md) and the
[step-by-step use and validation guide](docs/AI-SKILL-VALIDATION.md).
Run `python scripts/validate_ai_skill.py` on a complete matching checkout.
The skill requires access to its native evidence; a GitHub link alone does not
install it. Passing checks establish the documented retrieval scope, not accepted
readings, expert review or cross-platform model accuracy.


## AI research skill

This corpus project includes a vendor-neutral, evidence-first AI research skill in [`ai-skill/`](ai-skill/). The corpus remains the scholarly source of truth; the skill is an interface to it, not a second corpus and not an independent authority.

Researchers using ChatGPT, Claude, Gemini, or another capable model can provide the repository (or its AI-ready bundle) together with [`ai-skill/SKILL.md`](ai-skill/SKILL.md). The skill requires the model to preserve provenance, uncertainty, exclusions, source dependence, rights, and this project's scientific gates. Before substantive use, check [`ai-skill/generated/source-state.json`](ai-skill/generated/source-state.json) and the generated research-bundle index for the corpus commit represented by the AI package.

For questions spanning multiple corpus projects, use the **Combined Corpus Research AI** documented in the Linear A repository under [`combined-ai-skill/`](https://github.com/hawkinsnick/Linear-A/tree/main/combined-ai-skill). It orchestrates the registered individual skills while keeping their evidence models and rights separate. Membership in the combined system does **not** imply linguistic relationship, sign equivalence, chronology, decipherment, or independent replication.

## Current status — 5.3.0

Adds 234 source-attributed contextual assertions on 26 CHIC entries from 29 INSCRIBE catalogue pages; three unnumbered pages remain excluded source leads. All 331 identities have reproducible review dossiers. Script alternatives, unknown findspots and chronology qualifiers remain literal. The primary pilot remains five readings on two entries; the 2026-10-11 checkpoint adds eight dependent digital versions on four entries. There are 13 versions on six entries and zero independent reviews.

Family contract 1.2 aligns all five projects with [Phaistos Disc 1.6.0](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v1.6.0). The shared readiness report preserves native sampling units, source rights and blocked linguistic controls. It authorizes no pooling or linguistic relationship claim. See [`research/family-readiness-v1.json`](research/family-readiness-v1.json).

The authoritative current gate summary is [`analysis/current-status.json`](analysis/current-status.json). Historical release reports below retain their original versions and claims.

Validate this checkout with:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate_current_state.py
python scripts/test_current_state.py
```


**5.0.0 — critical corpus production contract**

A provenance-first, source-critical and reproducible research corpus for Cretan Hieroglyphic.

5.0 turns the mature 4.x engineering platform into a stable production contract for inscription-level critical evidence. It adds exact-locator critical readings, source-access and redistribution controls, versioned corpus snapshots, explicit research boundaries and compatibility with the cross-project matched-information-environment protocol.

The foundation remains 331 CHIC catalogue-spine records and a 96-entry numbered core registry inside the broader multi-repertoire model. No native phonetic values are asserted. At the historical 5.0 baseline, critical readings, source-checked occurrences and independent reviews were zero. The current source-access pilot above adds readings while independent review remains pending.

**Blocked is a valid scientific result.** Internal structural analysis, CH–Linear A comparison and fine matched-degradation experiments remain blocked by their predeclared evidence requirements.


The shared family report now targets the Disc [2.0.0-rc.2 prerelease](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v2.0.0-rc.2). Final independently reviewed Disc 2.0 remains blocked; compatibility does not confer linguistic equivalence or independent review. Native evidence and this repository’s release version are unchanged.

### Research evidence workbench 1.0

Download the research workbench ZIP, extract it, and open [workbench/evidence.html](workbench/evidence.html). It includes searchable pinned evidence, coverage definitions and unverified inspection-note export. See the [reading and review guide](research/workbench-guide.md). This engineering milestone grants no independent epigraphic acceptance.

### Research workbench 1.1

Download the [research workbench 1.1 package](https://github.com/hawkinsnick/Cretan-hieroglyphs/releases/tag/research-workbench-v1.1.0), extract it, and open `workbench/evidence.html`. It adds snapshot-bound inspection collections and includes the immutable release correction tracker. The Disc explorer also presents readable scenario comparisons. This engineering release grants no scientific acceptance.

## Context and review dossiers — 5.3.0

Adds 234 source-attributed contextual assertions on 26 CHIC entries from 29 INSCRIBE catalogue pages; three unnumbered pages remain excluded source leads. All 331 identities have reproducible review dossiers. Script alternatives, unknown findspots and chronology qualifiers remain literal. The primary pilot remains five readings on two entries; the 2026-10-11 checkpoint adds eight dependent digital versions on four entries. There are 13 versions on six entries and zero independent reviews.

Read [the researcher guide](docs/CONTEXT-AND-DOSSIERS.md), [the coverage audit](analysis/context-coverage-v1.json) and [record dossiers](research/record-dossiers.json). Run `python scripts/research_dossiers.py` to check deterministic replay. Metadata coverage does not imply reading coverage or representative sampling.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. The browser uses only the explicit rights/provenance-reviewed allowlist in `research/browser-sources.json`, including the CHIC catalogue spine, context, critical readings, graph observations, core sign registry, disagreements and record dossiers. Never recursively ingest restricted/raw upstream material. Browser display does not establish decipherment, source independence or expert validation.

## Source checkpoint — 2026-10-11

See [source coverage and reconciliation](docs/SOURCE-COVERAGE-2026-10-11.md), [unresolved source comparisons](research/source-reconciliation.json) and [bounded coverage inventories](research/coverage-denominators.json). Source checking has expanded; complete primary reconciliation and independent expert acceptance remain open.

## Existing-evidence reconciliation — 2026-10-11

Reading coverage is unchanged. [Existing-evidence reconciliation](docs/EXISTING-EVIDENCE-RECONCILIATION.md) now accounts for every existing assertion and identity, preserving source apparatus and unresolved scholarly decisions.

## AI integrity checkpoint — 2026-10-11

[AI integrity controls](docs/AI-INTEGRITY.md) document source-bound bundle publication and checked cross-corpus dependency safeguards. Reading coverage and scholarly acceptance are unchanged.


### Source coverage and reconciliation — 2026-10-12

Added 193 attributed DBAS catalogue leads and three unmapped INSCRIBE object pages; the two named routes now locate 204 existing CHIC identities. New leads are distinct from accepted metadata/readings. See [scope, rights and verification](docs/SOURCE-GROWTH-2026-10-12.md).

## Primary H/Y catalogue frontier — 2026-10-13

Direct inspection of CHIC pp. 54–57 accounts for all 127 identities missing from the earlier DBAS/INSCRIBE route union (114 H, 13 Y). Historical museum/provenance/type assertions now accompany their dossiers; the three-route union covers 331/331 catalogue identities. This is catalogue-context coverage, not reading completeness or current museum certification. The three INSCRIBE discovery pages have explicit dispositions, including a post-1996 Vrysinas candidate and provisional primary-text uncertainty comparisons. Canonical readings remain 13 versions on six entries; independent reviews remain zero. Read [scope, checks and remaining acquisition](docs/HY-FRONTIER-2026-10-13.md).

## Evidence and alternative-reading queries

[Query source evidence and unresolved alternatives](docs/EVIDENCE-AND-ALTERNATIVES.md) using exact native IDs, full source records, pinned artifact locators and explicit corpus-specific scope. [Coverage by native view](analysis/evidence-query-coverage.json) keeps catalogue entries, reading versions, assertions and research issues distinct. This interface adds no source collation, canonical reading or expert acceptance.

Bounded attribution and comparison review: [source qualifications and remaining gaps](docs/ATTRIBUTION-REVIEW.md).

## Research delivery and feedback

[Search, reproducible local packages, evidence-bound answers and review submissions](docs/RESEARCH-DELIVERY.md).
[Measured delivery scope](analysis/research-delivery.json) retains native evidence
units and all scholarly, rights and expert-review dependencies.
