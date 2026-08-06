# DropOutV3

```c
REG_OP(DropOutV3)
    .INPUT(x, "T")
    .OPTIONAL_INPUT(noise_shape, TensorType({DT_INT64}))
    .INPUT(p, TensorType({DT_DOUBLE, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OUTPUT(y, "T")
    .OUTPUT(mask, TensorType({DT_UINT8}))
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(DropOutV3)
```

## Brief

During training, randomly zeroes some of the elements of the input tensor
with probability

## Inputs

- x: A tensor, support ND format. Must be one of the following data types: float32,float16,bfloat16,1 ~ 8-D.
- noise_shape: A tensor, optional tensor. Must be int64,1-D.
- p: A required input, should be const data. Must be one of the following data types: double,float32,float16,bfloat16.
- seed: A required input, should be const data. Must be one of the following data types: int32,int64, 1-D.
- offset: A required input, should be const data. Must be int64, 1-D.
Shape is 2 and the value of index 0 is 0. Value of index 1 must be a multiple of 4.

## Outputs

- y: A tensor with the same shape and type as "x".
- mask_out: A tensor with the shape and type support uint8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 noise_shape: int64
- input2 p: bfloat16,double,float16,float32
- input3 seed: int32,int64
- input4 offset: int64
- output0 y: bfloat16,float16,float32
- output1 mask: uint8


---

[Back to Operator Specifications (Ascend950)](../README.md)
