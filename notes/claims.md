# Resume Claims Audit — ETH SSRF 2027

Resume: AjeetSherkar_Resume(20261125-092446).pdf

Status definitions:
- VERIFIED: Direct supporting evidence inspected.
- NEEDS INSPECTION: Evidence location identified but not checked.
- RE-MEASURE: Original measurement needs reproduction.
- CANNOT SHOW: No reliable supporting evidence found.

## 1. Quantitative claims

| ID | Claim | Evidence location | Status |
|---|---|---|---|
| C01 | Maintained a CGPA of 7.76 through Semester IV | Sanjivani University Statement of Grades, April 2026, page 3 | VERIFIED |
| C02 | TransitNexus edge processing: 76.9 ms rolling median (historical live test) | Original transitnexus-sih README, A7 Edge Processing Measurement | VERIFIED |
| C03 | Pothole model: 78.2% precision on 97-image test set | Original docs/MODEL_CARD.md, Test Set evaluation | VERIFIED |
| C04 | Pothole model: 74.3% mAP@50 on 97-image test set | Original docs/MODEL_CARD.md, Test Set evaluation | VERIFIED |
| C05 | 14 reports from 10 simulated buses consolidated into 1 incident | Original transitnexus-sih README, simulated fleet test | VERIFIED |
| C06 | 44 reports from 3 physical phones consolidated into 1 incident | Original transitnexus-sih README, real-device field test | VERIFIED |
| C07 | TransitNexus live field-test throughput: 0.2–0.7 FPS observed across November 21, 2026 screenshots | Original physical-phone field-test dashboard screenshots | VERIFIED |
| C08 | LedgerPilot 94.20% precision | Reproduced held-out evaluation | VERIFIED |
| C09 | LedgerPilot 86.67% recall | Reproduced held-out evaluation | VERIFIED |
| C10 | LedgerPilot 100% auto-resolution precision | Reproduced held-out evaluation | VERIFIED |
| C11 | LedgerPilot 150 held-out records | Held-out ground truth and reproduced evaluation | VERIFIED |
| C12 | LedgerPilot 308 automated tests | Full pytest run: 308 passed | VERIFIED |

## 2. Strong action-verb claims

| ID | Claim | Evidence location | Status |
|---|---|---|---|
| C13 | Built EdgePulse predictive maintenance system | EdgePulse repository | NEEDS INSPECTION |
| C14 | Engineered vibration-based features | Feature-engineering code | NEEDS INSPECTION |
| C15 | Trained and evaluated XGBoost classifier | Training/evaluation code | NEEDS INSPECTION |
| C16 | Built FastAPI service using ONNX Runtime | API/inference code | NEEDS INSPECTION |
| C17 | Implemented SHAP importance and PDF reporting | Source code/report | NEEDS INSPECTION |
| C18 | Built Gmail bank-statement automation using Activepieces, PDF extraction, AI transaction parsing and Google Sheets | `personal-finance-tracker-activepieces/workflow.json` — Gmail trigger, PDF extraction, AI parsing, Sheets persistence and Gmail reporting | VERIFIED |
| C19 | Implemented statement validation, conditional routing, statement-period duplicate prevention and correction/reprocessing | `personal-finance-tracker-activepieces/workflow.json` — validation engine, validation router, idempotency check/router and correction branches | VERIFIED |
| C20 | Built TransitNexus mobile sensing client using WebSocket and GPS | Original client source and pipeline audit | VERIFIED |
| C21 | Implemented YOLOv8, OpenCV and ByteTrack tracking | edge/detector.py and edge/server.py | VERIFIED |
| C22 | Built structured event engine converting detections into events | Edge processing and event-engine implementation | VERIFIED |
| C23 | Designed spatio-temporal deduplication with adaptive GPS radius and confidence fusion | backend/dedup.py and deduplication tests | VERIFIED |
| C24 | Implemented incident lifecycle and recurrence linking | backend/dedup.py, backend/models.py and backend/tests/test_dedup.py | VERIFIED |
| C25 | Built SQLite offline outbox with retry and idempotent ingestion | edge/outbox.py and edge/uplink.py | VERIFIED |
| C26 | Developed FastAPI/PostgreSQL backend with automated tests and GitHub Actions CI | backend/, backend/tests/, .github/workflows/ci.yml and deployment documentation | VERIFIED |
| C27 | Built Leaflet GIS dashboard with fleet map and incident views | frontend-web/index.html | VERIFIED |
| C28 | Created multi-bus fleet simulator and field-tested on physical phones | tools/simulate_fleet.py and November 21, 2026 field-test records | VERIFIED |
| C29 | Implemented a DNN for MNIST handwritten-digit classification using a 784-128-64-10 architecture | `optimizer-comparison-dnn/notebooks/optimizer_experiment.py` — MNIST preprocessing and Keras Sequential model | VERIFIED |
| C30 | Compared SGD, Adam and RMSprop under a common DNN training setup | `optimizer-comparison-dnn/notebooks/optimizer_experiment.py` — three optimizer configurations, 10 epochs and batch size 128 | VERIFIED |
| C31 | Evaluated optimizer convergence and performance using validation accuracy, validation loss and test-set evaluation | `optimizer-comparison-dnn/notebooks/optimizer_experiment.py` and `results/accuracy_plot.png`, `results/loss_plot.png`; exact README accuracy figures not independently reproduced | VERIFIED |
| C32 | Built deterministic LedgerPilot reconciliation system | LedgerPilot source | VERIFIED |
| C33 | Designed confidence-gated human review | Decision-engine code/tests | VERIFIED |
| C34 | Fixed tied candidate-score ambiguity bug | Commit/regression test | VERIFIED |
| C35 | Deployed LedgerPilot with Docker and PostgreSQL | Deployment configuration | VERIFIED |

## 3. Three strongest claims — provisional

1. LedgerPilot: 94.20% precision, 86.67% recall and 100% auto-resolution precision.
2. TransitNexus: 78.2% precision and 74.3% mAP@50.
3. LedgerPilot: 308 automated tests.

## 4. Three least-certain claims — provisional

1. TransitNexus: approximately 67–76 ms per frame.
2. TransitNexus: approximately 0.2–0.9 FPS per phone.
3. Optimizer comparison: Adam and RMSprop achieved faster convergence and higher final accuracy than SGD.

## 5. Audit rules

- Never mark a claim VERIFIED based only on the resume.
- Preserve original evaluation artifacts.
- Re-measure claims when measurement conditions are unclear.
- Do not invent missing evidence.
- Record exact file paths, commands and outputs when verified.

## LedgerPilot — C12 verification evidence

- Claim: 308 automated tests.
- Status: VERIFIED
- Repository: ~/LedgerPilot
- Test command: `pytest -q`
- PostgreSQL service: `docker compose up -d postgres`
- Database readiness check: `docker compose exec postgres pg_isready`
- Test output: `308 passed in 2.55s`
- Failed tests: 0
- Environment: LedgerPilot `.venv`
- Verification date: 2026-11-25


## LedgerPilot — C08 to C11 held-out verification

- Repository: ~/LedgerPilot
- Evaluation implementation: evaluation/evaluate.py
- Original metrics: evaluation/results/held_out_metrics.json
- Held-out dataset: data/heldout/
- Ground truth: data/ground_truth/heldout_ground_truth.csv

### Reproduction

Command:
`python` with `evaluate(data_dir=Path("data/heldout"), ground_truth_path=Path("data/ground_truth/heldout_ground_truth.csv"))`

Original and reproduced metrics matched exactly:

- Ground-truth records: 150
- Predicted matches: 138
- Correct matches: 130
- Precision: 94.2029%
- Recall: 86.6667%
- F1: 90.2778%
- Auto-resolved records: 123
- Correct auto-resolved records: 123
- Auto-resolution precision: 100%

Comparison: 9/9 metric checks passed.

### Claim decisions

- C08 — 94.20% precision: VERIFIED
- C09 — 86.67% recall: VERIFIED
- C10 — 100% auto-resolution precision: VERIFIED
- C11 — 150 held-out records: VERIFIED

Verification date: 2026-11-25


## S5 — Final claim reflection

### Three strongest claims

1. **C08–C12 — LedgerPilot:** Strong implementation and evaluation evidence, including 308 passing automated tests and reproduced held-out evaluation metrics.
2. **C34 — LedgerPilot ambiguity fix:** A specific candidate-selection bug was fixed, with regression tests demonstrating the ambiguous and clear-match cases.
3. **C20–C28 — TransitNexus:** Substantial implementation evidence covering detection, tracking, event processing, deduplication, offline handling, backend services and physical-phone testing.

### Three least-certain claims

1. **C13–C17 — EdgePulse:** Deferred. The README was reviewed, but implementation evidence has not yet been inspected. These claims must not be treated as verified.
2. **C03–C04 — TransitNexus model metrics:** The reported 78.2% precision and 74.3% mAP@50 are documented, but 48 of the 97 test images share a filename-derived source identifier with training images. Dataset independence is therefore a limitation.
3. **C05–C06 — TransitNexus incident consolidation:** The 14-report and 44-report results demonstrate system-level corroboration and deduplication, not independent human-confirmed ground truth.

### S5 completion notes

- Academic CGPA verified against the university Statement of Grades.
- Evidence locations and verification statuses recorded for assessed claims.
- EdgePulse claims C13–C17 intentionally deferred.
- Numerical claims with measurement or evaluation limitations retain their qualifications.
- No Git commit or push performed as part of this audit.
