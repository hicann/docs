# FillV2D

```c
REG_OP(FillV2D)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_UINT8, DT_INT16, DT_INT32, DT_INT64}))
    .ATTR(value, Float, 0)
    .REQUIRED_ATTR(dims, ListInt)
    .OP_END_FACTORY_REG(FillV2D)
```

## Brief

Fill the value to a tensor has the specified shape.

## Outputs

y: A Tensor. Has the shape specify by attr shape, and full of the value specify by attr value.

## Attributes

- value: An optional float value. Defaults to 0.0.
- dims: A required listInt to specify the shape that the value to fill.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- output0 y: float32

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with the ONNX operator ConstantOfShape.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
