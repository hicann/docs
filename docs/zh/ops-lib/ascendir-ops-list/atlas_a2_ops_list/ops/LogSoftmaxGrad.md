# LogSoftmaxGrad

```c
REG_OP(LogSoftmaxGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(axis, ListInt, {-1})
    .OP_END_FACTORY_REG(LogSoftmaxGrad)
```

## Brief

Computes the gradient for log softmax activations.

## Inputs

- grad: A ND tensor. Must be one of the following data types: float16, bfloat16, float32.
- x: A ND tensor. Has the same data type and shape as "grad".

## Outputs

y: A ND tensor. Has the same data type and shape as "grad". 

## Attributes

axis: An optional list of ints. Multi-axis reduction is supported. Defaults to "{-1}".
In Ascend 950 AI Processor, only single-axis reduction is supported. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 grad: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator LogSoftmaxGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
