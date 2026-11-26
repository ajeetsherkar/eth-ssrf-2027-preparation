# TransitNexus — CV Bullets v0

## 1. Refined evidence-backed CV bullets

### Bullet 1 — Computer Vision: Pothole Detection

Developed and evaluated a custom YOLOv8n pothole-detection model, achieving 78.2% precision and 74.3% mAP@50 on a reported test evaluation of 97 images containing 292 ground-truth objects.

Evidence:
- Reported model evaluation metrics.
- Test evaluation: 97 images and 292 ground-truth objects.
- These are reported results, not an independently repeated evaluation in this benchmark study.

### Bullet 2 — Inference Benchmarking

Built a reproducible PyTorch CPU benchmarking workflow for YOLOv8n at 640x640, measuring 47.04 ms mean latency and 49.16 ms P95 across 200 end-to-end iterations.

Evidence:
- Original latency CSV containing 200 measurements.
- PyTorch CPU FP32, batch size 1.
- Includes preprocessing, inference, NMS and Python predictor overhead.
- Starts with an already-decoded BGR frame; excludes video decoding, model loading and warm-up.
- Results are from one end-to-end benchmark launch.

### Bullet 3 — Model Architecture Profiling

Profiled a custom YOLOv8n model at 640x640, verifying 3.01M parameters and approximately 8.2 GFLOPs through PyTorch model inspection, THOP profiling and the Ultralytics model summary.

Evidence:
- PyTorch model inspection: 3,011,043 parameters.
- THOP: 4.0958 G MACs.
- Ultralytics model summary: approximately 8.2 GFLOPs.
- MACs and FLOPs are different counting conventions and must not be treated as interchangeable.

## 2. Future benchmark placeholders — NOT YET MEASURED

- PyTorch-to-ONNX speed-up: [X]x
- ONNX mean latency: [X] ms
- ONNX P95 latency: [X] ms
- Accuracy change after export: [X] percentage points
- Additional reproducible tests: [N] tests

Replace placeholders only after running and verifying the corresponding experiments.

## 3. Important evaluation limitation

The reported dataset split has source-image overlap:
- 48 test images share source identifiers with training.
- 89 validation images share source identifiers with training.

This limits claims about generalization to unseen source images. Disclose this limitation in research discussions and avoid describing the reported metrics as leakage-free performance.

## 4. CV writing rule

Every bullet must communicate:
1. Action verb.
2. What was built, tested or measured.
3. A verifiable result.
4. How the result was validated.

Avoid bullets that only list tools or technologies.
