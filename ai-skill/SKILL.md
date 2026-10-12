---
name: cretan-hieroglyphic-research
description: Evidence-first AI research skill for the Cretan Hieroglyphic corpus.
version: 0.3.1
---

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
