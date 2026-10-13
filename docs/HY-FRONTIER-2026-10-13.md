# Cretan Hieroglyphic evidence frontier — 13 October 2026

The 127 CHIC identities absent from the two previously enumerated discovery routes are now accounted for by directly inspected primary-edition museum concordance pages. They comprise 114 H-series and 13 Y-series identities. This is a systematic coverage gap in those discovery views, not evidence of lost inscriptions or an incomplete CHIC numbering spine.

## What changed

[Primary-concordance assertions](../research/hy-primary-concordance-2026-10-13.json) bind each former gap to CHIC 1996 printed pp. 54–57, with image/page digests, source-reported museum abbreviation, provenance abbreviation and document type. The assertions appear in the [331 review dossiers](RECORD-DOSSIERS.md). OCR was used to locate entries; the four primary page images were visually checked before factual encoding. No page images, edition prose, transnumerations or drawings are republished.

| Measure | Before | This checkpoint |
|---|---:|---:|
| CHIC identities in DBAS/INSCRIBE named-route union | 204 | 204 |
| Additional identities with inspected primary-concordance assertions | 0 | 127 |
| Identities with at least one of these three source routes | 204 | 331 |
| Identities absent from all three bounded routes | 127 | 0 |
| Canonical reading versions / catalogue entries | 13 / 6 | 13 / 6 |
| Independently reviewed entries | 0 | 0 |

These are overlapping catalogue views, not independent witnesses or additional objects. Historical holdings are statements of the 1996 edition, not present-day museum verification. Keep provenance abbreviations literal. CHIC-331 retains its unknown holding symbol and angle-bracketed number; do not assign a museum or infer current survival. The 127-row supplement is separate from the existing 26 INSCRIBE context records and 234 assertions.

## Three INSCRIBE discovery pages

[Discovery dispositions](../research/inscribe-discovery-dispositions-2026-10-13.json) retain all three pages outside the CHIC spine:

- **VRY S (4/4) 01:** an attributed primary article reports discovery in the 2011 season, after CHIC 1996. Treat it as a post-edition reference candidate, not a missing CHIC join. Four provisional textual comparisons distinguish the primary article's initial uncertain labels and proposed readings from INSCRIBE's definite strings. Side a has proposed 005 and alternative 073; side d has proposed 038 and an attributed alternative 036 for its first sign. Brackets and alternative identifications must accompany any discussion. The article copy was available through web-extracted text, but direct host retrieval failed with HTTP403; figures and primary PDF facsimile were not visually collated. Do not promote these comparisons to accepted canonical readings.
- **CMS II,1 064:** the digital page has a dash for script and transnumeration. A motif comparison is not an inscription or CHIC object identification.
- **CMS II,2 221:** the page has a dash for script. Keep possible motif interpretations provisional. Its three-sided subtype versus a side-d remark is an unresolved source inconsistency. Both INSCRIBE CMS links literally target Heidelberg book/89 in the directly acquired source HTML; access to that route was denied. Do not claim CMS II,2 was delivered or inspected.

Source attribution, source access, intended-use rights, primary visual collation and independent acceptance remain separate. Do not use this checkpoint as a redistribution licence for source transcriptions, images or 3D models.

## Verification and remaining work

Run `python scripts/validate_hy_frontier.py`, `python -m unittest discover -s scripts -p test_hy_frontier.py`, and native current-state/dossier validation. The receipt is [analysis/hy-frontier-2026-10-13.json](../analysis/hy-frontier-2026-10-13.json). The individual AI bundle includes both new registers and this guide.

The discovery-route gap is closed at this finite scope. Reading coverage remains six of 331 catalogue entries, with 325 lacking an encoded reading. Next source work is primary object-page/apparatus collation, lawful representative H/I/S/Y reading acquisition, current holding verification where relevant, post-1996 extension discovery, and visual verification of the Vrysinas comparison. Existing CHIC-202/252 material disagreements and CHIC-252/328 apparatus qualifications remain unresolved. Corpus-wide structural and comparative analysis remain blocked; no whole-corpus pre-expert completion or expert-only readiness is claimed.
