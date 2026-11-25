# S4 — FLOPs, Compute-Bound and Memory-Bound

## 1. FLOPs

FLOPs means Floating Point Operations. It measures the number
of floating-point calculations performed by an operation.

## 2. Matrix multiplication

For A (M x N) multiplied by B (N x K):

FLOPs = 2 x M x N x K

For batch size B:

FLOPs = 2 x B x M x N x K

### Worked example

M = 640, N = 640, K = 640, batch = 1

FLOPs = 2 x 640 x 640 x 640
      = 524,288,000
      = 0.524288 GFLOPs

## 3. Convolution

FLOPs = 2 x H_out x W_out x C_out x C_in x k x k

For batch size B, multiply the result by B.

### Worked example

Input = 640 x 640 x 3
Output channels = 16
Kernel = 3 x 3
Stride = 2
Padding = 1
Output dimensions = 320 x 320

FLOPs = 2 x 320 x 320 x 16 x 3 x 3 x 3
      = 88,473,600
      = 0.0884736 GFLOPs

## 4. Compute-bound vs memory-bound

Compute-bound: Performance is limited mainly by the
processor's calculation capacity.

Memory-bound: Performance is limited mainly by data movement
between memory and the processor.

Quantization reduces the bits used for weights and activations,
which reduces memory usage and data transfer. It can improve
performance when memory bandwidth is the bottleneck.

## 5. Important takeaway

FLOPs estimate computational workload, but FLOPs alone do not
determine actual inference latency. Memory bandwidth, hardware,
runtime, precision and implementation also matter.

## 6. Connection to TransitNexus

When comparing PyTorch CPU and ONNX Runtime CPU, keep the model,
input shape, batch size and precision consistent. Record latency
alongside computational workload instead of assuming fewer FLOPs
automatically means faster inference.

### One-sentence summary

Compute-bound operations are limited by processing power, memory-bound operations are limited by data transfer speed, and quantization helps memory-bound operations by reducing the size of weights and activations.
