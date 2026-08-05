# MultilabelMarginLoss

```c
REG_OP(MultilabelMarginLoss)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(target, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(is_target, TensorType({DT_INT32}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(MultilabelMarginLoss)
```

## Brief

Creates a criterion that optimizes a multi-class multi-classification hinge loss (margin-based loss)
       between input x (a 2D mini-batch Tensor) and output y (which is a 2D Tensor of target class indices) 

## Inputs

Two inputs, including:
- x: A tensor. Must be one of the following types:
    float16, float32, bfloat16.
- target: A tensor. Must be the following types:
    int32. 

## Outputs

- y: A Tensor has same element type as input x.
- is_target: A Tensor has same element type as input target.

## Attributes

reduction: An optional string. Defaults to "mean" 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 target: int32
- output0 y: bfloat16,float16,float32
- output1 is_target: bfloat16,float16,float32,int32

## Third-party framework compatibility

Compatible with the Pytorch operator MultiLabelMarginLoss. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
