#!/usr/bin/env python3
"""Build a vendor-neutral, provenance-aware AI research bundle from canonical repo artifacts."""
import csv, hashlib, json, os, subprocess
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"ai-skill"/"generated"; OUT.mkdir(parents=True,exist_ok=True)
sha=os.environ.get("SOURCE_COMMIT") or subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
CANDIDATES=[('attribution_review', 'research/attribution-review.json'), ('attribution_review', 'analysis/attribution-review-audit.json'), ('attribution_review', 'docs/ATTRIBUTION-REVIEW.md'), ('attribution_review', 'scripts/attribution_review.py'), ('attribution_review', 'scripts/test_attribution_review.py')]+[('native_evidence_profile', 'research/evidence-query-profile.json'), ('native_evidence_coverage', 'analysis/evidence-query-coverage.json'), ('native_evidence_query', 'scripts/evidence_query.py'), ('native_evidence_query_tests', 'scripts/test_native_evidence_query.py'), ('native_evidence_guide', 'docs/EVIDENCE-AND-ALTERNATIVES.md')]+[('hy_frontier', 'research/hy-primary-concordance-2026-10-13.json'), ('hy_frontier', 'research/inscribe-discovery-dispositions-2026-10-13.json'), ('hy_frontier', 'analysis/hy-frontier-2026-10-13.json'), ('hy_frontier', 'docs/HY-FRONTIER-2026-10-13.md'), ('hy_frontier', 'scripts/validate_hy_frontier.py')]+[('source_growth', 'research/dbas-chs-catalogue-leads.json'), ('source_growth', 'research/inscribe-unmapped-discovery.json'), ('source_growth', 'analysis/source-growth-2026-10-12.json'), ('source_growth', 'docs/SOURCE-GROWTH-2026-10-12.md'), ('source_growth', 'scripts/source_growth.py')]+[
 ("cross_corpus_dependencies","research/cross-corpus-dependencies.json"),("sync_publication_guard","ai-skill/scripts/publish_sync.py"),("ai_integrity_guide","docs/AI-INTEGRITY.md"),
 ("qualified_assertions","research/qualified-assertion-views.json"),
 ("reference_reconciliation","research/reference-reconciliation-v2.json"),("identity_reconciliation","research/identity-reconciliation-v2.json"),
 ("source_expansion","research/source-check-2026-10-11.json"),("source_reconciliation","research/source-reconciliation.json"),("coverage_denominators","research/coverage-denominators.json"),
 ("readable_dossiers","docs/RECORD-DOSSIERS.md"),
 ("record_dossiers","research/record-dossiers.json"),("context_coverage","analysis/context-coverage-v1.json"),("context_assertions","corpus/context-assertions.json"),("bibliography","bibliography/sources.json"),("context_guide","docs/CONTEXT-AND-DOSSIERS.md"),
 ("current_status","analysis/current-status.json"),("source_inspection","research/source-inspection-2026-10-02.json"),("dbas_chs_baseline","research/dbas-chs-baseline.json"),("manifest","corpus/manifest.json"),("critical_readings","corpus/critical-readings.json"),("pre_expert_maximum","research/pre-expert-maximum.json"),("pre_expert_source_exhaustion","research/pre-expert-source-exhaustion.json"),("audit","exports/audit.json"),
 ("coverage","data/coverage.json"),("claims","release/CLAIM-REGISTRY.csv"),
 ("corpus_json","exports/corpus.json"),("corpus_jsonl","exports/corpus.jsonl"),
 ("greek_subset","exports/greek-subset.json"),("eteocypriot_components","exports/eteocypriot-components.json"),
 ("rights_matrix","DATA-LICENSE-MATRIX.md"),("rights","docs/RIGHTS.md"),
 ("rights_and_licensing","docs/RIGHTS-AND-LICENSING.md"),("notice","NOTICE"),("third_party","THIRD-PARTY-NOTICES.md")
]
CANDIDATES += [("research_delivery", p) for p in ['scripts/research_delivery.py','scripts/test_research_delivery.py','docs/RESEARCH-DELIVERY.md','analysis/research-delivery.json']]
CANDIDATES += [('skill_function_validation', p) for p in ['ai-skill/SKILL.md', 'ai-skill/manifest.json', 'scripts/validate_ai_skill.py', 'scripts/test_ai_skill_validation.py', 'docs/AI-SKILL-VALIDATION.md', '.github/workflows/ai-skill-function.yml']]
CANDIDATES += [('skill_validator_code', p) for p in ['ai-skill/scripts/build_bundle.py', 'ai-skill/scripts/validate_bundle.py', 'ai-skill/scripts/sync_skill.py']]
CANDIDATES += [("academic_closure_control", p) for p in ["research/closure-controls.json", "scripts/closure_controls.py", "scripts/test_closure_controls.py", "docs/CLOSURE-CONTROLS.md"]]
CANDIDATES += [('nonreview_workflow', 'docs/NONREVIEW-WORK.md')]
artifacts=[]
for role,rel in CANDIDATES:
 p=ROOT/rel
 if p.is_file():
  b=p.read_bytes(); artifacts.append({"role":role,"path":rel,"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)})
bundle={"schema_version":"0.3.1","skill_version":"0.3.1","source_commit":sha,
 "generated_at_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
 "canonical_repository":True,
 "contract":{"corpus_is_authoritative":True,"missing_means_unknown":True,"cross_corpus_equivalence_requires_explicit_evidence":True,
 "preserve_uncertainty":True,"preserve_source_independence":True,"preserve_rights":True},
 "artifacts":artifacts}
(OUT/"research-bundle-index.json").write_text(json.dumps(bundle,indent=2)+"\n",encoding="utf-8")
(OUT/"source-state.json").write_text(json.dumps({"schema_version":"1.0","source_commit":sha,"skill_version":"0.3.1","bundle_index":"ai-skill/generated/research-bundle-index.json"},indent=2)+"\n",encoding="utf-8")
print(f"Indexed {len(artifacts)} canonical artifacts at {sha}")
