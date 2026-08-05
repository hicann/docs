# GeluGrad

```c
REG_OP(GeluGrad)
    .INPUT(dy, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(z, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(GeluGrad)
```

## Brief

Computes the gradient for the gelu of "x" .

## Inputs

Three inputs, including:
- dy: A Tensor. Support 1D ~ 8D. Must be one of the following types:bfloat16, float16, float32.
- x: A Tensor of the same type, shape and format as "dy".
- y: A Tensor of the same type, shape and format as "dy" .

## Outputs

z: A Tensor. Has the same type, format and shape as "dy".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 y: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32

## Attention Constraints

In Ascend 950 AI Processor, inputs and outputs support broadcasting.

## Third-party framework compatibility

Compatible with the TensorFlow operator GeluGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
