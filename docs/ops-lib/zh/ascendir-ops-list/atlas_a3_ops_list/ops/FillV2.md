# FillV2

```c
REG_OP(FillV2)
    .INPUT(dims, TensorType({DT_INT16, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT16, DT_INT32, DT_INT64}))
    .ATTR(value, Float, 0)
    .OP_END_FACTORY_REG(FillV2)
```

## Brief

Fill the value to a tensor has the specified shape.

## Inputs

One inputs, including:
- dims: An Tensor, specify the shape that the value to fill.

## Outputs

- y: A Tensor. Has the shape specify by attr shape, and full of the value specify by attr value.

## Attributes

- value: An optional float value. Defaults to 0.0.

## Third-party framework compatibility

Compatible with the ONNX operator ConstantOfShape.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
