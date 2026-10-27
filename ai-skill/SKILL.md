---
name: cretan-hieroglyphic-research
description: Evidence-first AI research skill for the Cretan Hieroglyphic corpus.
version: 0.3.1
---

## Load and validate this repository-bound skill

Use this file as the canonical individual skill. Load the complete matching
repository checkout or give the AI access to its files; this Markdown file alone
contains instructions, not the corpus. Do not claim that supplying a GitHub URL
installs a skill or makes private/local files available to an AI platform.
Resolve the paths below from the repository root. With Python 3.10+ available,
run `python scripts/validate_ai_skill.py` before describing this skill as
operational on the supplied checkout. Read `docs/AI-SKILL-VALIDATION.md` for the
exact workflow, examples, dependencies, validation scope and limitations.
If execution or source access is unavailable, say which step was not run and
make no fresh validation claim. Preserve all native source/rights restrictions.

Discover exact IDs with `python scripts/evidence_query.py --coverage` and
`python scripts/evidence_query.py --list COLLECTION`. Retrieve evidence with
`python scripts/evidence_query.py --record ID --collection COLLECTION`;
use `python scripts/research_delivery.py --dossier ID --collection COLLECTION`
for its evidence-only answer frame. Return the exact source path/hash/pointer,
attribution, uncertainty and native evidence unit. A missing ID means absent
from the selected view; never invent a replacement or infer global absence.


# Cretan Hieroglyphic Research Skill

This skill is an interface to the corpus in this repository. The corpus remains the canonical source of truth. Never maintain an independent scholarly dataset inside the skill.

## Governing rules
1. Separate physical/epigraphic observation, source transcription, normalization, computational derivation, scholarly interpretation, and AI-derived analysis.
2. Prefer canonical machine-readable corpus records over prose summaries for record-level questions.
3. Preserve identifiers, provenance, uncertainty, disagreements, corrections, negative results, and superseded analyses.
4. Never invent missing signs, readings, restorations, provenience, bibliography, source independence, or rights.
5. Label calculations performed by the AI and state enough method for reproduction.
6. Respect record/source-specific licensing and attribution. Repository-level licensing must not erase upstream restrictions.
7. For cross-corpus claims, establish comparability and source independence before interpreting similarity.
8. Report blocked or missing evidence rather than filling gaps.

## Corpus-specific caution
Undeciphered script: preserve sign-classification uncertainty and do not infer readings, language, or equivalence from graphic similarity alone.

## Default research response
Give the direct answer, followed as relevant by Evidence; Evidentiary status; Uncertainty/limitations; Reproducibility; Rights/attribution.

## Synchronization
Read `ai-skill/generated/source-state.json` before substantive work. It records the corpus commit from which the AI-facing package was synchronized. Generated files are rebuildable views; canonical corpus files govern if a discrepancy is found.

## Academic-scrutiny gates
- No native phonetic values are asserted
- Structural and comparative analyses remain BLOCKED until canonical gates change
- The five original primary readings on two entries and eight added dependent digital versions on four entries (13 versions on six entries in total) are not representative corpus coverage
- Zero independently reviewed objects must remain explicit
- Graphic similarity does not establish sign equivalence

## Context and dossier routing
Read `analysis/context-coverage-v1.json` and `research/record-dossiers.json` before record-level context or coverage claims. Follow native references, source IDs, locators and input digests. Separate metadata coverage from reading/occurrence coverage. Preserve literal unknowns, alternative script classifications and chronology qualifiers. Treat missing evidence as unknown. Do not upgrade source-reported catalogue links to physical identity, partial occurrences to complete transcriptions, or source closure to independent verification. Consult `docs/CONTEXT-AND-DOSSIERS.md` for the specific acquisition and rights limits.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. The browser uses only the explicit rights/provenance-reviewed allowlist in `research/browser-sources.json`, including the CHIC catalogue spine, context, critical readings, graph observations, core sign registry, disagreements and record dossiers. Never recursively ingest restricted/raw upstream material. Browser display does not establish decipherment, source independence or expert validation.


## Fleet EpiDoc and identity graph gates
Read `analysis/epidoc-interoperability-audit.json` and `research/identity-graph.json`. EpiDoc serialization must preserve sparse reading coverage, alternative script classifications, writing-versus-iconographic uncertainty and source lineage. Catalogue identity is not transcription verification. The 96-class sign registry carries no native phonetic values, and graphic resemblance never creates a cross-script identity assertion.

## Bounded source checkpoint (2026-10-11)

Use `research/source-check-2026-10-11.json`, `research/source-reconciliation.json` and `research/coverage-denominators.json` together. Retain source roles, unresolved competing labels/materials and literal identifier namespaces. Never sum overlapping catalogue and rich-record views, infer a physical corpus population, or promote dependent evidence to independent primary verification.

## Existing evidence: reconciliation and identity controls

Before source certainty, apparatus, duplicate or object-identity claims, read `research/reference-reconciliation-v2.json`, `research/identity-reconciliation-v2.json` and `docs/EXISTING-EVIDENCE-RECONCILIATION.md`. Literal source strings are frozen; read the apparatus ledger alongside them. Primary agreement of numeric labels is not independent sign verification. Unidentified marks and conditional alternatives are not added canonical occurrences. Namespaces and core/candidate status cannot be flattened, and zero exact alias collisions cannot establish physical uniqueness.

## Enforced assertion, dependency and bundle integrity

Read `docs/AI-INTEGRITY.md` and the required `research/cross-corpus-dependencies.json` before source counts or cross-corpus analysis. Use qualified assertion views when provided; original source literals must travel with their reconciliation, uncertainty and identity context. The dependency register does not certify physical identity or linguistic affinity. Shared catalogue references and duplicated digital sources are not independent witnesses. Missing links mean unknown, not independent. `scripts/check_cross_corpus_dependencies.py` screens declared record selections and rejects pooled physical/witness counts and phonetic transfer. Native AI bundle validation checks the dependency projection and local evidence hashes. Bundle publication validates the exact source parent and never rebases or force-pushes the validated artifact. Software and packaging checks do not establish expert or model-behavior acceptance.


## Source growth — 2026-10-12

Read `docs/SOURCE-GROWTH-2026-10-12.md` and `analysis/source-growth-2026-10-12.json` with `research/dbas-chs-catalogue-leads.json`, `research/inscribe-unmapped-discovery.json`. Keep 193 dependent catalogue leads, the 204/331 named-route union, 26 existing contexts and three unjoined object pages separate. A source script dash or CHIC sign-number comparison is not an object ID or accepted writing. No new reading coverage or physical witness is established.

## Primary H/Y frontier and post-edition discovery
Read `docs/HY-FRONTIER-2026-10-13.md`, `research/hy-primary-concordance-2026-10-13.json`, `research/inscribe-discovery-dispositions-2026-10-13.json` and `analysis/hy-frontier-2026-10-13.json`. Distinguish the historical 204/331 DBAS/INSCRIBE union from the expanded 331/331 three-route union. The additional 127 primary catalogue contexts (114 H, 13 Y) provide historical holdings/provenance/types; retain literal abbreviations and CHIC-331 unknown holding/angle brackets. Do not call them new readings, independent witnesses, current museum verification or representative evidence. Keep the 26 INSCRIBE contexts and 127 historical contexts as separate units.

Treat Vrysinas as a post-1996 reference candidate with no fabricated CHIC number. Preserve primary proposed brackets, side-a alternative 073 and side-d first-sign alternative 036. Its four text-extracted comparisons await primary visual collation; digital lines have no explicit face labels, so the order pairing is provisional. Keep the two CMS pages script-unassigned and their source inconsistencies/access failures explicit. Canonical coverage remains 13 reading versions across six entries and zero independent reviews. Never convert bounded discovery closure into whole-corpus completeness or expert-only readiness.

## Corpus-native evidence and alternatives

Read `docs/EVIDENCE-AND-ALTERNATIVES.md`, `research/evidence-query-profile.json` and `analysis/evidence-query-coverage.json` for evidence or competing-reading questions. Use `scripts/evidence_query.py` with exact native IDs and an explicit collection when ambiguous. Preserve `native_record`, every uncertainty/editorial mark, source attribution, locator, inspection status and rights. Cite artifact path, JSON pointer and SHA-256; hashes certify bytes only. Treat explicitly linked records as declared ID associations, not physical certification or independent witnesses. Context resources have corpus-level scope and are not automatically about the queried record. Distinguish a named source reading from a legacy queue label, uninspected bibliographic lead, count convention or hypothesis. Do not infer a count of collated alternative pairs or independent witnesses from searchable rows; those metrics remain unknown. Report the native units and scope of each view separately, and defer to the corpus-specific limits. No new readings, expert acceptance or decipherment follows from this interface.

## Bounded attribution review (2026-10-15)

Read `docs/ATTRIBUTION-REVIEW.md` and `research/attribution-review.json` before describing a dispute or source comparison. Run `python scripts/attribution_review.py --case ID` with the referenced evidence available. Preserve complete native evidence and distinguish reading, interpretation, classification, count, identity and representation questions. This checkpoint reviews pinned repository packets; it does not repeat their primary consultation or grant independent review. Inherit the exact author/publication, locator, consultation limits and dependence from each pointer; missing fields remain unknown. Use the case-specific remaining work. Do not count register entries or apparatus notes as fully attributed pairs, physical objects or independent witnesses.

Two located material conflicts and an explicit reading-apparatus gap. An empty dedicated disagreements list does not imply scholarly consensus.

## Research delivery, evidence answers and feedback

Read `docs/RESEARCH-DELIVERY.md` and verify `analysis/research-delivery.json`
with `python scripts/research_delivery.py --check` before using delivery claims.
Use `--dossier ID --collection COLLECTION` for exact evidence-bound answers;
preserve the complete native payload, citations, categories and limitations.
Use `--search TEXT` for source-record retrieval. Do not convert file pointers
into missing primary-edition citations, catalogue rows into unique objects,
source dependence into independent confirmation, or review forms into acceptance.
Prepare bounded review drafts with `--review-template`; validate submissions with
`--validate-review`, then require native human-maintainer acceptance. Treat delivery
and deterministic answer tests as engineering checks, not empirical LLM validation
or completion of scholarly/source-permission work. Local packaging grants no new
redistribution rights. Label any model-generated analysis separately and cite it.

## Apply scoped closure controls

Read `docs/CLOSURE-CONTROLS.md` and retrieve linked `closure-controls` before using a missing locator, conflicting material or printed type membership in a claim. Respect explicit nulls and exclusions. A completed control does not recover a source, adjudicate a conflict, establish sign identity or grant expert acceptance. Raw source literals remain available with their original qualifications.

## Preserve review provenance

Reject malformed JSON-pointer escapes and negative or leading-zero array indices
when verifying source citations; literal object keys retain their own spelling.
Read the [master hostile-review report](https://github.com/hawkinsnick/Master-Corpus-AI-Skill/blob/main/references/hostile-review-2026-10-25.md)
for this member's pinned retrieval scope and the limits of the source-fidelity
and development checks. Complete retrieval-view traversal does not certify
corpus completeness, accepted readings, independent witnesses or expert review.

## Execute research work without academic review

Read `docs/NONREVIEW-WORK.md` for the frozen source check, full-record development tests, short-text dependence screen, component package audit and executable researcher walkthrough. Separate executable work from the evidence needed to close a scholarly criterion. Preserve native null/false values, editorial notation and linked source assertions. Treat short-string equality as a lead only; require explicit source lineage for shared-source dispositions and never infer physical identity or independence. Treat native research archives as local-research packages until their actual components are cleared. Use the separate noncommercial tools-only export when source payload is not authorized for redistribution. Report digital-source fidelity, deterministic software tests, fresh model development responses and independent academic validation separately. Keep original scholarly gates and frozen study inputs unchanged.

For machine-readable source citations, emit one exact JSON pointer per reference. Do not put ranges, semicolon lists, prose headings or several pointers into a `pointer` field. For text use `locator_type: text_contains` and a literal `locator` instead. Bind each reference to bytes actually present at the stated commit; verify with `git show COMMIT:PATH` and SHA-256. A working-tree file absent from that commit cannot be cited as committed evidence. Disclose uncommitted execution context separately from source evidence. Use the master `scripts/verify_response_refs.py` when available; a passing citation check establishes byte/locus binding, not bibliographic truth.
