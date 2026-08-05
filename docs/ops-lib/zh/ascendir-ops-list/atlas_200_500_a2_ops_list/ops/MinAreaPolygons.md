# MinAreaPolygons

```c
REG_OP(MinAreaPolygons)
    .INPUT(pointsets, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(polygons, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(MinAreaPolygons)
```

## Brief

Find a min polygon from the point set in the operator MinAreaPolygons. 

## Inputs

- pointsets: A 2D Tensor with shape (N, 18), format ND, dtype must be one
of the following types: float16, float32, double. 

## Outputs

- polygons: A 2D Tensor with shape (N, 8), format ND, dtype must be one of
the following types: float16, float32, double.  

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 pointsets: double,float16,float32
- output0 polygons: double,float16,float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
