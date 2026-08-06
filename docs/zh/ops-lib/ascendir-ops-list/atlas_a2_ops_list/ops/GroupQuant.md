# GroupQuant

```c
REG_OP(GroupQuant)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(group_index, TensorType({DT_INT32, DT_INT64}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT4, DT_INT8}))
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(GroupQuant)
```

## Brief

Quantize feature map by group.

## Inputs

- x: A Tensor. 2-D with shape [S, H]. Must be one of the following types:
float32, float16, bfloat16. The format support ND.
- scale: A Tensor. Specifying the quantitation scale of x. 2-D with shape
[E, H], the second dim of scale shape is same as the second dim of x shape.
Must be one of the following types: float32, float16, bfloat16.
The format support ND.
- group_index: A Tensor. Specifying the index of group. 1-D with shape
[E, ], the first dim of scale shape is same as the first dim of scale shape.
Must be one of the following types: int32, int64. The format support ND.
- offset: A Tensor. Optional. Specifying the quantitation offset of x. 1-D
with shape [1, ] or 0-D with shape []. Must be one of the following types:
float32, float16, bfloat16. The dtype of offset should be same as scale.
The format support ND.

## Outputs

y: A 2-D Tensor. Shape is same as input x. The format support ND.
Must be one of the following types: int4, int8.

## Attributes

dst_type: An optional attribute of type int. Declare the output dtype.
Support DT_INT4, DT_INT8. Defaults to DT_INT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 scale: bfloat16,float16,float32
- input2 group_index: int32,int64
- input3 offset: bfloat16,float16,float32
- output0 y: int4,int8

## Attention Constraints

- If output y data type is INT4, the last dim of y shape should be
an even number.
- Input group_index value should be in the range of [0, S] and be an
non-decreasing sequence. The last value of input group_index must be the
same as the first dim of x shape.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
