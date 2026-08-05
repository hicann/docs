# Muls

```c
REG_OP(Muls)
     .INPUT(x, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
     .OUTPUT(y, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
     .REQUIRED_ATTR(value, Float)
     .OP_END_FACTORY_REG(Muls)
```

## Brief

Multiply tensor with scale.

## Inputs

One input, including:
x: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
bfloat16, int32, int16, int64, float16, float32, complex32, complex64.

## Outputs

y: A ND Tensor. Has the same dtype and shape as "x".

## Attributes

- value: An required attribute. Must be float.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,complex32,complex64,float16,float32,int32,int64
- output0 y: bfloat16,complex32,complex64,float16,float32,int32,int64

## Attention Constraints

For parameters of the float32 type, there is no precision loss. For INT32 and INT64 parameters,
precision loss occurs when the parameter value exceeds 2^24. it is recommended to use Mul.

## Third-party framework compatibility

Compatible with the PyTorch operator muls.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
