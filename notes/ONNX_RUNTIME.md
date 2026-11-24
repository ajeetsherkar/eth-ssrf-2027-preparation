
# S3 — Fundamentals: ONNX and ONNX Runtime

## Task 1: ONNX Runtime and Execution Providers

### 1. What is ONNX?
ONNX (Open Neural Network Exchange) is an open format used to represent machine-learning models so they can work across different frameworks and platforms.

### 2. What is ONNX Runtime?
ONNX Runtime (ORT) is an inference engine that loads ONNX models and executes their operations.

### 3. What is an Execution Provider (EP)?
An Execution Provider is a backend that assigns ONNX model operations to supported hardware.

Think of it as choosing the hardware engine for inference.

| Execution Provider | Where it runs |
|---|---|
| CPUExecutionProvider | CPU |
| CUDAExecutionProvider | NVIDIA GPU using CUDA |
| CoreMLExecutionProvider | Apple Core ML-supported hardware |
| TensorrtExecutionProvider | NVIDIA GPU using TensorRT |

### 4. Execution Providers for My Setup

- CPUExecutionProvider: Runs inference on CPU; my TransitNexus benchmark baseline.
- CoreMLExecutionProvider: Uses Apple's Core ML framework and compatible Apple hardware.
- CUDAExecutionProvider: Uses NVIDIA GPUs; not applicable to my MacBook Air.
- TensorrtExecutionProvider: Uses NVIDIA TensorRT; not applicable to my current setup.

Provider availability depends on the installed ONNX Runtime build.

### 5. Provider Priority
ONNX Runtime can use multiple providers in priority order.

Example:
[CUDAExecutionProvider, CPUExecutionProvider]

It tries CUDA first and uses CPU for operations that CUDA cannot execute.

### Key Takeaway
For my TransitNexus PyTorch vs ONNX Runtime benchmark, CPUExecutionProvider is the baseline. I will document the available providers before configuring the inference session.


## Task 2: ONNX Runtime Session Options

### 1. intra_op_num_threads
Controls the number of CPU threads used to perform a single operation.

### 2. graph_optimization_level
Controls the level of graph optimization applied by ONNX Runtime to improve execution efficiency.

Available levels:
- ORT_DISABLE_ALL: No graph optimizations.
- ORT_ENABLE_BASIC: Basic optimizations.
- ORT_ENABLE_EXTENDED: Extended optimizations.
- ORT_ENABLE_ALL: All supported graph optimizations.

### 3. execution_mode
Controls how operations in the computation graph are executed.

- ORT_SEQUENTIAL: Executes graph operations sequentially.
- ORT_PARALLEL: Executes independent graph branches in parallel.

### Key Takeaway
For my TransitNexus CPU benchmark, I will explicitly document the thread count, graph optimization level and execution mode to ensure reproducible measurements.


## Task 3: Loading and Inspecting the ONNX Model

### Model Inspection Results

Model path: models/pothole/best_benchmark.onnx

Available execution providers:
- CoreMLExecutionProvider
- AzureExecutionProvider
- CPUExecutionProvider

Model input details:
- Input name: images
- Input shape: [1, 3, 640, 640]
- Input type: tensor(float)

Active execution provider:
- CPUExecutionProvider

### Key Takeaway
The YOLOv8 ONNX model loaded successfully using ONNX Runtime on my MacBook Air. The model accepts a batch of 1 RGB image with 640x640 resolution and uses CPUExecutionProvider for the current benchmark.


## Task 4: Ultralytics ONNX Export

### 1. Export Command

from ultralytics import YOLO

model = YOLO("best.pt")

model.export(
    format="onnx",
    imgsz=640,
    simplify=True,
    opset=17,
    half=False
)

### 2. Important Export Options

- format="onnx": Exports the PyTorch model into ONNX format.
- imgsz=640: Sets the input image resolution to 640x640.
- simplify=True: Simplifies the ONNX computation graph.
- opset=17: Selects ONNX operator-set version 17 for compatibility.
- half=False: Keeps FP32 precision instead of FP16.

### 3. GPU and Precision Requirements

- Standard FP32 ONNX export can run on CPU.
- Ultralytics supports FP16 ONNX export; suitable hardware and exporter support must be checked.
- FP16 TorchScript export requires a CUDA GPU.
- half=True is a legacy precision flag; quantize=16 is the newer option.

### 4. My TransitNexus Benchmark Choice

I will use:
- Format: ONNX
- Image size: 640x640
- Simplification: Enabled
- Precision: FP32
- Half precision: Disabled

I will retain the existing best_benchmark.onnx model and will not re-export or overwrite it during this session.

### Key Takeaway

Ultralytics converts a trained YOLOv8 PyTorch model into ONNX format using the export() method. Export settings control format, image size, graph simplification, operator compatibility and precision.

