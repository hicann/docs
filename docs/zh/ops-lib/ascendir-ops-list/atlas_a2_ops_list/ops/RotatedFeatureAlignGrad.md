# RotatedFeatureAlignGrad

```c
REG_OP(RotatedFeatureAlignGrad)
    .INPUT(dy, TensorType({DT_FLOAT}))
    .INPUT(bboxes, TensorType({DT_FLOAT}))
    .OUTPUT(dx, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(spatial_scale, Float)
    .ATTR(points, Int, 1)
    .OP_END_FACTORY_REG(RotatedFeatureAlignGrad)
```

## Brief

RotatedFeatureAlignGrad:Calculate the gradient of input features according to
the gradient of output features. 

## Inputs

- dy: A tensor of type float32. The gradient of output features.
- bboxes: A tensor of type float32. The position information of bboxes.

## Outputs

- dx: A tensor of type float32. The gradient of input features.

## Attributes

- spatial_scale: A required float32. The scale of feature map to initial image.
- points: An optional int. Defaults to "1". The number of sample points.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float32
- input1 bboxes: float32
- output0 dx: float32

## Third-party framework compatibility

Compatible with MMCV RotatedFeatureAlign operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
