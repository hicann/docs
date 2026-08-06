# SoftmaxCrossEntropyLoss

```c
REG_OP(SoftmaxCrossEntropyLoss)
    .INPUT(scores, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .INPUT(labels, TensorType({DT_INT32, DT_INT64}))
    .OPTIONAL_INPUT(weights, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .ATTR(ignore_index, Int, 0)
    .ATTR(reduction, String, "mean")
    .OUTPUT(loss, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .OUTPUT(log_prop, TensorType({DT_DOUBLE,DT_FLOAT16,DT_FLOAT,DT_BFLOAT16}))
    .OP_END_FACTORY_REG(SoftmaxCrossEntropyLoss)
```

## Brief

Loss function that measures the softmax cross entropy.

## Inputs

Three inputs, including:
- scores: A Tensor. Must be one of the following types: float16, bfloat16, float32, double.
A "batch_size * num_classes" matrix.
- labels: A Tensor. Must be one of the following types: "int32", "int64".
- weights: A manual rescaling weight given to each class, the same dtype with scores.
If given, it has to be a 1D Tensor assigning weight to each of the classes.
Otherwise, it is treated as if having all ones. 

## Outputs

- loss: A Tensor for per example loss (a "batch_size" vector). Has the same type as "scores".
- log_prop: A Tensor. Has the same type as "scores" .

## Attributes

ignore_index:Specifies a target value that is ignored and does not contribute to the input gradient.
It's an optional value, Defaults to 0. 
reduction: A character string from "none", "mean", and "sum", specifying the gradient output mode. Defaults to "mean" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 scores: float16,float32
- input1 labels: int32,int64
- input2 weights: float16,float32
- output0 loss: float16,float32
- output1 log_prop: float16,float32

## Third-party framework compatibility

Compatible with the ONNX operator SoftmaxCrossEntropyLoss.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
