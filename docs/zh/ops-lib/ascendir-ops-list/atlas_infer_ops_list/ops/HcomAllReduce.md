# HcomAllReduce

```c
REG_OP(HcomAllReduce)
    .INPUT(x, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_INT8, DT_INT16, DT_FLOAT16, DT_INT64}))
    .REQUIRED_ATTR(reduction, String)
    .REQUIRED_ATTR(group, String)
    .ATTR(fusion, Int, 1)
    .ATTR(fusion_id, Int, -1)
    .OP_END_FACTORY_REG(HcomAllReduce)
```

## Brief

Outputs a tensor containing the reduction across all input tensors
passed to op.

## Inputs

x: A tensor. Must be one of the following types: int8, int16, int32, int64, float16,
float32.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- reduction: A required string identifying the reduction operation to
perform.The supported operation are: "sum", "max", "min", "prod".
- group: A required string identifying the group name of ranks
participating in the op.
- fusion: An optional integer identifying the fusion flag of the op.
0: no fusion; 1 (default): fusion the ops by gradient segmentation strategy; 2: fusion the ops by fusion id.
- fusion_id: An optional integer identifying the fusion id of the op.
The HcomAllReduce ops with the same fusion id will be fused.

## Attention Constraints

- "group" is limited to 128 characters. Use "hccl_world_group"
as the name of a world group.
- For Altas 300I Duo, "prod"/"max"/"min" does not support int16
- For Altas A2, "prod" does not support int16/bfp16
- For Altas A3, "prod" does not support int16/bfp16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
