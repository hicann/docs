# PointsInPolygons

```c
REG_OP(PointsInPolygons)
.INPUT(points, TensorType({DT_FLOAT}))
.INPUT(polygons, TensorType({DT_FLOAT}))
.OUTPUT(output, TensorType({DT_FLOAT}))
.OP_END_FACTORY_REG(PointsInPolygons)
```

## Brief

Determine if the target points set is inside polygons. 

## Inputs

- points: A 2D Tensor with shape (N, 2), format ND, dtype must be float32.
- polygons: A 2D Tensor with shape (M, 8), format ND, dtype must be float32.
    This parameter will be transposed to be (8, M) before passed to the operator. 

## Outputs

- output: A 2D Tensor with shape (N, M), format ND, dtype must be float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 points: float32
- input1 polygons: float32
- output0 output: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
