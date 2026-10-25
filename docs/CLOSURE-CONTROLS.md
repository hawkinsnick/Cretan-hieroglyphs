# Preserve unresolved material pairs

CHIC-202 and CHIC-252 each retain the attributed CHIC Ivoire and INSCRIBE Animal bone assertions, including their exact source locators. The linked closure control returns `resolved_material: null` and prohibits a single resolved material value. Neither the material nor the physical join has been adjudicated.

```sh
python scripts/evidence_query.py --record CHIC-202 --collection catalogue-dossiers
python scripts/evidence_query.py --record CHIC-252 --collection closure-controls
```

This completes ACD-015's unresolved-pair representation criterion. Material adjudication remains a separate scientific follow-up. Do not mistake either historical source's literal value for the project's resolved material.

## Replay and scope

```sh
python scripts/closure_controls.py --check
python scripts/test_closure_controls.py
```

The tests exercise actual researcher queries, exclusions/nulls and source-pin integrity, and reject inconsistent input evidence. Software controls establish no new expert approval, source reading, material determination or physical identity.
