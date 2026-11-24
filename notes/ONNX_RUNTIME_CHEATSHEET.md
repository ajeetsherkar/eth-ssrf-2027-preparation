# ONNX Runtime — One-Page Cheat Sheet

## 1. Export YOLOv8 to ONNX

from ultralytics import YOLO

model = YOLO("best.pt")

model.export(
    format="onnx",
    imgsz=640,
    simplify=True,
    opset=17,
    half=False
)

## 2. Import ONNX Runtime

import onnxruntime as ort
import numpy as np

## 3. Check Available Providers

print(ort.get_available_providers())

## 4. Create Session Options

so = ort.SessionOptions()
so.intra_op_num_threads = 4
so.graph_optimization_level = (
    ort.GraphOptimizationLevel.ORT_ENABLE_ALL
)
so.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL

## 5. Create Inference Session

sess = ort.InferenceSession(
    "best_benchmark.onnx",
    sess_options=so,
    providers=["CPUExecutionProvider"]
)

## 6. Inspect Model Input

inp = sess.get_inputs()[0]

print(inp.name)
print(inp.shape)
print(inp.type)

## 7. Run Inference Once

# x must be a preprocessed NumPy input
# with the correct shape and data type.

outputs = sess.run(
    None,
    {inp.name: x.astype(np.float32)}
)

print("Inference completed")
print("Number of outputs:", len(outputs))

## 8. Important Benchmark Settings

- Runtime: ONNX Runtime
- Provider: CPUExecutionProvider
- Threads: 4
- Graph optimization: ORT_ENABLE_ALL
- Execution mode: ORT_SEQUENTIAL
- Input size: 640x640
- Batch size: 1
- Precision: FP32

Note: The inference input must be preprocessed to match
the model's expected input format.
