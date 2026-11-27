# TransitNexus — Research Case Study

One-sentence description: An AI-powered road hazard detection system developed as a Smart India Hackathon project.

## Overview

TransitNexus investigates an AI-powered road hazard detection pipeline, with this case study focusing on inference performance and reproducible benchmarking.

TODO:
- [ ] Explain the problem, intended users, and system functionality.
- [ ] Summarize the scope of this research case study.

## Architecture

TODO:
- [ ] Add an architecture diagram.
- [ ] Explain the major system components in approximately five lines each.
- [ ] Show the data flow from input frame to detection output.

## Methodology

TODO:
- [ ] Document the model and inference frameworks.
- [ ] Describe the datasets and input data.
- [ ] Document preprocessing and postprocessing rules.
- [ ] Explain the evaluation and benchmarking protocol.

## Experiments

TODO:
- [ ] Describe each experiment, configuration, and measurement procedure.
- [ ] Record hardware and software configurations.
- [ ] Link experiment scripts and detailed evaluation reports.

## Results

TODO:
- [ ] Add a results table with measured values and hardware details.
- [ ] Add relevant performance figures.
- [ ] Report accuracy and latency findings where available.

## Limitations

TODO:
- [ ] Document hardware and environment constraints.
- [ ] Identify measurement limitations and sources of variability.
- [ ] Distinguish preliminary findings from established conclusions.

## How to reproduce

TODO:
- [ ] Specify the required Python version and dependencies.
- [ ] Provide exact environment setup commands.
- [ ] Provide exact commands to reproduce each experiment.
- [ ] Document expected outputs and result locations.

## Performance study

The full TransitNexus inference performance study will be published on Day 13.

TODO:
- [ ] Add the completed benchmark report when available.

**Report:** [TransitNexus Benchmark Report v1](../../report/TransitNexus_benchmark_v1.pdf)

## Research Objective

Investigate the existing inference pipeline, understand its architecture and measurement methodology, identify performance measurement limitations, and establish a foundation for reproducible benchmarking experiments.

## S1 — Initial Pipeline Audit

The first research session focused on:

- Understanding the end-to-end system architecture.
- Tracing the live edge inference pipeline.
- Identifying what the existing timing measurements include and exclude.
- Reviewing the existing PyTorch and ONNX benchmarking approach.
- Identifying limitations in the available performance evidence.

## Research Evidence

| File | Description |
|---|---|
| `audit.md` | Detailed technical pipeline audit |
| `notes/timing_grep.txt` | Code investigation of timing-related implementation |
| `results/first_run.txt` | Initial experiment output |
| `results/first_run_terminal.txt` | Terminal execution evidence |

## Next Research Steps

- Establish a reproducible PyTorch baseline.
- Benchmark inference latency and throughput.
- Compare PyTorch and ONNX Runtime.
- Investigate performance under different configurations.
- Evaluate accuracy and performance trade-offs.
- Document findings, limitations, and reproducibility details.

## Research Integrity

- Preserve original experiment outputs.
- Distinguish measured results from assumptions.
- Document hardware and software configurations.
- Avoid presenting preliminary measurements as definitive conclusions.

## Original Project

The original project and its source code are maintained separately:

https://github.com/ajeetsherkar/transitnexus-sih

---

**Research programme:** ETH SSRF 2027  
**Case study:** TransitNexus  
**Current stage:** S1 — Initial Pipeline Audit completed
