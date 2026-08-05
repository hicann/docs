# Round

```c
REG_OP(Round)
    .INPUT(x, TensorType(DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT32, DT_INT64,
                         DT_DOUBLE))
    .OUTPUT(y, TensorType(DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT32, DT_INT64,
                          DT_DOUBLE))
    .ATTR(decimals, Int, 0)
    .OP_END_FACTORY_REG(Round)
```

## Brief

Rounds the values of a tensor to the nearest integer, element-wise.
Rounds half to even.

## Inputs

Inputs including:
x: An ND Tensor of type bfloat16, float16, float, int64, double, int32.

## Outputs

y: An ND Tensor. Has the same data type and shape as "x".

## Attributes

decimals: An optional int attr, number of decimal places to round to. Defaults to "0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- output0 y: float16,float32,int32
### AI CPU
- input0 x: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Attention Constraints

- When the input value is between [-0.5, -0], the output value is 0.
- In the scenarios where the decimals is not zero:
    The input data exceeds the range of (-347000, 347000), which may affect the precision errors.

## Third-party framework compatibility

Compatible with the TensorFlow operator Round.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
