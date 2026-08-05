# CorrectBBox

```c
REG_OP(CorrectBBox)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(grid, TensorType({DT_FLOAT16}))
    .INPUT(anchor_grid, TensorType({DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(stride, Int)
    .REQUIRED_ATTR(yolo_version, String)
    .OP_END_FACTORY_REG(CorrectBBox)
```

## Brief

Compute correct bounding box.

## Inputs

Three inputs, including:
- x: A 5D Tensor of type float16 with shape (N, na, no, H, W), na indicates the number of anchors,
no indicates the number of outputs per anchor, including [xywh, class_num, conf_score].
- grid: A 5D Tensor of type float16 with shape (1, na, 2, H, W) for V3/V5 and (1, 1, 2, H, W) for V7,
the value "2" indicates offsets of coordinates.
- anchor_grid: A 5D Tensor of type float16 with shape (1, na, 2, H, W) for V3/V5 and (1, 1, 2, 1, 1) for V7,
the value "2" indicates anchors relative to the original image.

## Outputs

- y: A 5D Tensor of type float16 with shape (N, na, no, H, W), same as the input x.

## Attributes

- stride: A required int32, scale for each box.
- yolo_version: A required string, specifying the YOLO version, optional [V3, V5, V7].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 grid: float16
- input2 anchor_grid: float16
- output0 y: float16

## Third-party framework compatibility

It is a custom operator.

## attention Constraints

- This operator applies to YOLO V3, V5 and V7 networks.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
