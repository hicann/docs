# HardSigmoid

```c
REG_OP(HardSigmoid)
    .INPUT(input_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OUTPUT(output_y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(alpha, Float, 0.16666666)
    .ATTR(beta, Float, 0.5)
    .OP_END_FACTORY_REG(HardSigmoid)
```

## Brief

Calculate the hard sigmoid function.

## Inputs

One input, including:
input_x: A ND tensor. The shape should be within the range of 0D to 8D.
Must be one of the following types: float16, float32, int32, bfloat16.

## Outputs

output_y: A ND tensor with the same dtype and shape as 'input_x'.

## Attributes

- alpha: An optional float. Slope of the operator, defaults to 0.16666666.
- beta: An optional float. Offset of the operator, defaults to 0.5.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: bfloat16,float16,float32,int32
- output0 output_y: bfloat16,float16,float32,int32

## Third-party framework compatibility

Compatible with the Pytorch operator Hardsigmoid.


---

[Back to Operator Specifications (Ascend950)](../README.md)
