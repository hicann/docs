# OpTiling

```c
REG_OP(OpTiling)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .DYNAMIC_INPUT(output_shape, TensorType::ALL())
    .OUTPUT(tiling_data, TensorType({DT_UINT8}))
    .OUTPUT(tiling_key, TensorType({DT_UINT64}))
    .OUTPUT(block_dim, TensorType({DT_INT32}))
    .OUTPUT(tiling_cond, TensorType({DT_INT32}))
    .REQUIRED_ATTR(tiling_node, String)
    .REQUIRED_ATTR(op_type, String)
    .OP_END_FACTORY_REG(OpTiling)
```

## Brief

Abstract tiling function to an op definition.
       The input will be data or shape. 

## Inputs

- x: The data of input. All types are available. It's a dynamic input.
- outputshape: The shape of previous op output shape. All types are available. It's a dynamic input.

## Outputs

- tiling_data: A Tensor. Must be one of the following types: uint8. Tiling data of tiling function.
                It should be a buffer.
- tiling_key: A Tensor. Must be one of the following types: uint64. Tiling key of tiling function.
- block_dim: A Tensor. Must be one of the following types: int32. Block dim of tiling function.
- tiling_cond: A Tensor. Must be one of the following types: int32.
                Tiling condition of tiling function which will be used to determined real execute kernel. 

## Attributes

- tiling_node: A string. Real tiling node such as matmul.
- op_type:  A string. Op type of the original node.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
