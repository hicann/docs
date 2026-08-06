# SoftmaxGrad

```c
REG_OP(SoftmaxGrad)
    .INPUT(softmax, TensorType({ DT_FLOAT16, DT_BF16, DT_FLOAT }))
    .INPUT(grad_softmax, TensorType({ DT_FLOAT16, DT_BF16, DT_FLOAT }))
    .OUTPUT(grad_x, TensorType({ DT_FLOAT16, DT_BF16, DT_FLOAT }))
    .ATTR(axes, ListInt, {-1})
    .OP_END_FACTORY_REG(SoftmaxGrad)
```

## Brief

Computes gradients for a softmax operation.

## Inputs

Two inputs, including:
- softmax: A ND tensor. Output of the softmax operator. Must be one of the following
data types: float16, bfloat16, float32.
- grad_softmax: A ND tensor. Has the same shape and data type as "softmax".

## Outputs

grad_x: A ND tensor. Has the same shape and data type as "softmax" . 

## Attributes

axes: An optional list of ints. Multi-axis reduction is supported. Defaults to "{-1}".
In Ascend 950 AI Processor, only single-axis reduction is supported. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 softmax: bfloat16,float16,float32
- input1 grad_softmax: bfloat16,float16,float32
- output0 grad_x: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator SoftmaxGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
