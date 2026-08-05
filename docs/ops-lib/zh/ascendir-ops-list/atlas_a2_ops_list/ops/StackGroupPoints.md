# StackGroupPoints

```c
REG_OP(StackGroupPoints)
    .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(features_batch_cnt, TensorType({DT_INT32, DT_INT64}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(indices_batch_cnt, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(StackGroupPoints)
```

## Brief

Group the points in the point cloud according to the group they belong to. 

## Inputs

Four inputs, including:
- features:  Tensor of features to group, input shape is (N1 + N2 ..., C).
- features_batch_cnt:  Input features nums in each batch, just like (N1, N2, ...). Defaults to None.
- indices: The indices of features to group with, input shape is (M1 + M2 ..., nsample).
- indices_batch_cnt: Input indices nums in each batch, just like (M1, M2, ...). Defaults to None.

## Outputs

One outputs: Grouped features, the shape is (M1 + M2 ..., C, nsample).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 features: float16,float32
- input1 features_batch_cnt: int32
- input2 indices: int32
- input3 indices_batch_cnt: int32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the MMCV operator GroupPoints(StackGroupPoints branch).


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
