# TransitNexus — Research Case Study

## Overview

TransitNexus is an AI-powered road hazard detection system developed as a Smart India Hackathon project.

This case study documents the technical investigation of its machine learning inference pipeline as part of ETH SSRF 2027 research preparation.

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
