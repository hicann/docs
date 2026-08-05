# ArgMaxGrad

```c
REG_OP(ArgMaxGrad)
    .INPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8}))
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(updates, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8}))
    .REQUIRED_ATTR(dimension, Int)
    .OP_END_FACTORY_REG(ArgMaxGrad)
```

## Brief

Returns the reverse tensor of the ArgMax operator of a tensor. 

## Inputs

three input, including:
var: A ND Tensor of type float16, float32, int32 or int8. 
indices: A ND Tensor of type int32. 
updates: A ND Tensor of type float16, float32, int32 or int8. 

## Outputs

y: A ND Tensor of type float16, float32, int32 or int8. 

## Attributes

- dimension: An integer of type int, specifying the axis information of the index with the maximum value.

## Attention Constraints

- indices: only support int32,and shape same to "updates"
- The value range of "dimension" is [-dims, dims - 1]. "dims" is the dimension length of "x".
- y:A ND Tensor, the type and shape is same to "var"

## Third-party framework compatibility

not support all scene like pytorch operator scatter
exp:
var.shape=[2,3,4,5], dim=2, the shape of indices and updates should be [2,3,5]
not support the shape of indices and updates is [2,3,2,5] like pytorch operator scatter. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
