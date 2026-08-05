# ThreeNN

```c
REG_OP(ThreeNN)
    .INPUT(xyz1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(xyz2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(dist, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(idx, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(ThreeNN)
```

## Brief

Calculate the index and distance of the nearest three point to the target point.

## Inputs

Two input:
xyz1: The set of target points.
xyz2: The set of compare points. 

## Outputs

dist: A Tensor, the distance of the nearest point to the target point.
idx: A Tensor, the index of the nearest point to the target point. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 xyz1: float16,float32
- input1 xyz2: float16,float32
- output0 dist: float32
- output1 idx: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
