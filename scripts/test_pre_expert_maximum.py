#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
load=lambda p:json.loads((R/p).read_text())
x=load("research/pre-expert-maximum.json");s=load("analysis/current-status.json");q=load("research/acquisition-queue.json")
assert x["target"]=="PRE_EXPERT_MAXIMUM"
assert s["committed_evidence_counts"]["catalogue_identities"]==331
assert s["committed_evidence_counts"]["critical_readings"]==13
assert s["committed_evidence_counts"]["source_checked_occurrence_objects"]==6
assert s["committed_evidence_counts"]["independently_reviewed_objects"]==0
assert {i["series"]:i["target_min"] for i in q["strata"]}=={"H":8,"I":5,"S":8,"Y":4}
assert s["scientific_results"]["structural_analysis"]=="BLOCKED"
assert s["scientific_results"]["comparative_analysis"]=="BLOCKED"
print("PASS: Cretan Hieroglyphic pre-expert maximum ledger")
