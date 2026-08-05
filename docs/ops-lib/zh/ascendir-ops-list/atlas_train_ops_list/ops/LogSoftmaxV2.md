# LogSoftmaxV2

```c
REG_OP(LogSoftmaxV2)
    .INPUT(logits, TensorType({DT_DOUBLE, DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(logsoftmax, TensorType({DT_DOUBLE, DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(axes, ListInt, {-1})
    .OP_END_FACTORY_REG(LogSoftmaxV2)
```

## Brief

Computes log softmax activations .

## Inputs

One input:
logits: A ND tensor. Must be one of the following data types: double, bfloat16, float16, float32 . 

## Outputs

logsoftmax: A ND tensor. Has the same data type as "logits" . 

## Attributes

axes: An optional list of ints. Multi-axis reduction is supported. Defaults to "{-1}" .
In Ascend 950 AI Processor, only single-axis reduction is supported. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 logits: float16,float32
- output0 logsoftmax: float16,float32
### AI CPU
- input0 logits: double,float16,float32
- output0 logsoftmax: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator LogSoftmax.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
