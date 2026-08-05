# ArgMaxGradD

```c
REG_OP(ArgMaxGradD)
    .INPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8}))
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(updates, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8}))
    .INPUT(assist, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8}))
    .REQUIRED_ATTR(dimension, Int)
    .OP_END_FACTORY_REG(ArgMaxGradD)
```

## Brief

Returns the reverse tensor of the ArgMax operator of a tensor. 

## Inputs

four input, including:
- var: A ND Tensor of type float16, float32, int32 or int8.
- indices: A ND Tensor of type int32.
- updates: A ND Tensor of type float16, float32, int32 or int8.
- assist: A ND Tensor of int32,also a assist matrix and it's shape must match the shape of var

## Outputs

y: A ND Tensor of type float16, float32, int32 or int8. 

## Attributes

- dimension: An integer of type int, specifying the axis information of the index with the maximum value.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32,int8,int32
- input1 indices: int32
- input2 updates: float16,float32,int8,int32
- input3 assist: int32
- output0 y: float16,float32,int8,int32

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

not support all scene like pytorch operator scatter
exp:
var.shape=[2,3,4,5], dim=2, the shape of indices and updates should be [2,3,5]
not support the shape of indices and updates is [2,3,2,5] like pytorch operator scatter. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
