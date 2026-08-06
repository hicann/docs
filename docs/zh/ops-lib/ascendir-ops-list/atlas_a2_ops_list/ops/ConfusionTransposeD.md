# ConfusionTransposeD

```c
REG_OP(ConfusionTransposeD)
    .INPUT(x, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(perm, ListInt)
    .REQUIRED_ATTR(shape, ListInt)
    .REQUIRED_ATTR(transpose_first, Bool)
    .OP_END_FACTORY_REG(ConfusionTransposeD)
```

## Brief

Fusion of Reshape and Transpose Operations.

## Inputs

One input, including:
x: A tensor. Must be one of the following types:
  int8, int16, int32, int64, uint8, uint16, uint32, uint64, float16, float, bfloat16. 

## Outputs

y: A Tensor with the same type and shape of x. 

## Attributes

- perm: A required listInt. The index of the aixs in the original tensor that corresponds to each axis in the transposed tensor.
- shape: An required listInt. The shape of the tensor after reshaping.
- transpose_first: An required bool. The attribution determines whether to perform the transpose operation first.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
