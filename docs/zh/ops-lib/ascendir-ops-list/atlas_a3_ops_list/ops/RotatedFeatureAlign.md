# RotatedFeatureAlign

```c
REG_OP(RotatedFeatureAlign)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(bboxes, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(spatial_scale, Float)
    .ATTR(points, Int, 1)
    .OP_END_FACTORY_REG(RotatedFeatureAlign)
```

## Brief

RotatedFeatureAlign:Calculate the output features according to
the input features. 

## Inputs

- x: A tensor of type float32. The input features.
- bboxes: A tensor of type float32. The position information of bboxes.

## Outputs

- y: A tensor of type float32. The output features.

## Attributes

- spatial_scale: A required float32. The scale of feature map to initial image.
- points: An optional int. Defaults to "1". The number of sample points.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 bboxes: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with MMCV RotatedFeatureAlign operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
