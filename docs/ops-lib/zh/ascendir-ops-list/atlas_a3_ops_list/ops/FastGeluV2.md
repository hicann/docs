# FastGeluV2

```c
REG_OP(FastGeluV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(FastGeluV2)
```

## Brief

The FastGeluV2 activation function is x*(sgn(x)*[(a/2)*(clip(|x|,max=-b)+b)^2+0.5]+0.5),
       where sgn(x) function is (x+0.000000000001)/|(x+0.000000000001)|.

## Inputs

One input, including:
x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bfloat16, float16, float32

## Outputs

y: A Tensor. Has the same type as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator FastGeluV2


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
