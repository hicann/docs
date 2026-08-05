# MoeGatingTopKSoftmax

```c
REG_OP(MoeGatingTopKSoftmax)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(finished, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(expert_idx, TensorType({DT_INT32}))
    .OUTPUT(row_idx, TensorType({DT_INT32}))
    .REQUIRED_ATTR(k, Int)
    .OP_END_FACTORY_REG(MoeGatingTopKSoftmax)
```

## Brief

compute softmax and topk for moe input.

## Inputs

- x: A 2D or 3D Tensor. Type is:BFloat16, Float16 or Float32. Format support ND.
- finished: A Tensor. Type is:Bool. Shape is x_shape[:-1]. Format support ND.

## Outputs

- y: A Tensor. Type is:BFloat16, Float16 or Float32. The data type must be the same as that of x.
The size of the non-1 axis must be the same as that of the corresponding axis of x.
The size of the -1 axis must be the same as that of k. Format support ND.
- expert_idx: A Tensor. Type is:Int32. The shape must be the same as that of y. Format support ND.
- row_idx: A Tensor. Type is:Int32. The shape must be the same as that of y. Format support ND.

## Attributes

- k: Required parameter. Type is:Int32. The value must greater than 0 and less than or equal to the size
of the -1 axis of x, and k must not greater than 1024.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 finished: bool
- output0 y: bfloat16,float16,float32
- output1 expert_idx: int32
- output2 row_idx: int32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
