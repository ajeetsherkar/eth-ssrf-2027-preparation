# TransitNexus Benchmark Experiment Plan

## 1. Research Question

How do runtime, precision, input size, batch size, and thread count affect latency, throughput, and detection accuracy of the TransitNexus detection pipeline on the available hardware?

## 2. Variables Under Investigation

- Runtime: PyTorch vs ONNX Runtime
- Precision: FP32 vs lower-precision formats, where supported
- Input size: Different image resolutions
- Batch size: Number of frames processed together
- Thread count: Number of CPU threads used

## 3. Experimental Controls

The following conditions will remain fixed during the baseline
runtime comparison:

| Control | Fixed setting |
|---|---|
| Benchmark video | data/bench_clip_fixed.mp4 |
| Number of frames | 200 |
| Video resolution | 1280 x 720 |
| Video frame rate | 30 FPS |
| Video duration | Approximately 6.67 seconds |
| Detection task | Pothole detection |
| PyTorch model | ../transitnexus-sih/models/pothole/best.pt |
| ONNX model | ../transitnexus-sih/models/pothole/best_benchmark.onnx |
| Inference image size | 640 x 640 |
| Baseline precision | FP32 |
| PyTorch device | CPU |
| ONNX execution provider | CPUExecutionProvider |
| Confidence threshold | 0.25 |
| NMS IoU threshold | 0.70 |
| Python environment | Python 3.11.13, same virtual environment |
| Hardware | Apple M2 MacBook Air |
| Input frames | Same decoded frames for both runtimes |
### Environmental Controls

- Use the same MacBook Air for all experiments.
- Connect the laptop to power before benchmarking.
- Close unnecessary background applications.
- Use the same Python virtual environment.
- Avoid changing model weights during the experiment.
- Record software versions and hardware details.
- Change only the variable being investigated in each experiment.

The fixed settings above define the baseline. Individual experiments
may deliberately change one variable while keeping the remaining
settings constant.

## 4. Evaluation Metrics

The following metrics will be recorded during each experiment:

| Metric | Meaning | Unit |
|---|---|---|
| Mean latency | Average time required to process one frame | ms/frame |
| Median latency (p50) | Middle value of frame processing times | ms/frame |
| p95 latency | 95th percentile of frame processing times | ms/frame |
| p99 latency | 99th percentile of frame processing times | ms/frame |
| Throughput | Number of frames processed per second | FPS |
| Model loading time | Time required to load the model | seconds |
| Peak memory usage | Maximum memory consumed during inference | MB |
| Detection count | Total number of detected objects | count |
| Detection consistency | Agreement between PyTorch and ONNX bounding boxes | IoU |
### Measurement Rules

- Exclude warm-up runs from measured inference latency.
- Measure model loading time separately.
- Use the same frames for both runtimes.
- Report mean, p50, p95 and p99 latency.
- Calculate throughput using the total measured inference time.
- Record memory usage separately from latency.
- Use IoU >= 0.50 as the bounding-box matching threshold.
- Do not treat detection consistency as a substitute for ground-truth accuracy evaluation.

## 5. Experiment Matrix

Each experiment changes one independent variable while keeping
the other baseline settings fixed.

| Experiment | Variable | Configurations | Purpose |
|---|---|---|---|
| E1 | Runtime | PyTorch CPU, ONNX CPU | Compare inference performance |
| E2 | Input size | 320, 416, 640 | Study resolution impact |
| E3 | Batch size | 1, 4, 8 | Study batch processing impact |
| E4 | CPU threads | 1, 2, 4, 8 | Study CPU parallelism impact |
| E5 | Precision | FP32, FP16 where supported | Study numerical precision and speed |
### Experiment Execution Rules

- E1 is the baseline runtime comparison.
- E2 changes only inference image size.
- E3 changes only batch size.
- E4 changes only CPU thread count.
- E5 changes only numerical precision.
- Use the same video frames for comparable experiments.
- Use warm-up runs before collecting measurements.
- Exclude warm-up runs from reported latency.
- Record unsupported configurations and their reasons.
- Check prediction consistency when changing precision or image size.
- Do not compare results from different hardware as if they were equivalent.


## 6. Stop Rules and Failure Conditions

An experiment will be stopped or marked invalid under the following
conditions:

1. Stop if the model fails to load or produces invalid outputs.
2. Stop if the benchmark video cannot provide all expected 200 frames.
3. Stop if inference produces runtime errors or non-finite latency values.
4. Stop if the laptop shows signs of thermal instability or system instability.
5. Stop if memory usage becomes unsafe or the system becomes unresponsive.
6. Repeat the experiment if unexpected background activity significantly affects measurements.
7. Mark unsupported runtime, precision, batch-size or thread configurations as unsupported.
8. Do not silently discard failed runs or unusual measurements.
9. Record the reason for every stopped, repeated or invalid experiment.
10. Do not report incomplete experiments as successful benchmark results.

### Result Validity

- Use repeated runs to check measurement stability.
- Investigate unusually large latency variations.
- Keep raw measurements for later analysis.
- Report limitations and failed configurations transparently.


## 7. Research Hypotheses

The following hypotheses will be evaluated through controlled experiments.
They are predictions and will be accepted or rejected based on measured results.

### H1 – Runtime Comparison

PyTorch CPU and ONNX Runtime CPU will show differences in inference
latency and throughput when processing the same frames on the same hardware.

### H2 – Input Resolution

Increasing the inference input resolution will increase inference
latency because the model processes more image data.

### H3 – Batch Size and CPU Threads

Changing batch size and CPU thread count will affect inference
throughput and per-frame latency.

