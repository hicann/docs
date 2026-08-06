# NanToNum

```c
REG_OP(NanToNum)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(nan, Float)
    .REQUIRED_ATTR(posinf, Float)
    .REQUIRED_ATTR(neginf, Float)
    .OP_END_FACTORY_REG(NanToNum)
```

## Brief

Replace Nan, positive infinity, and negative infinity values in input
with the values specified by nan, posinf, and neginf, respectively

## Inputs

x: A ND Tensor. Must be one of the following types: bfloat16, float16, float32. 

## Outputs

y: A ND Tensor of the same dtype as "x". 

## Attributes

- nan: An required attribute of type float32,
specifying the value to replace NaNs with.
- posinf: An required attribute of type float32,
specifying the value to replace Infs with.
- neginf: An required attribute of type float32,
specifying the value to replace -Infs with. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch operator nan_to_num.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
