# RotatedBoxEncode

```c
REG_OP(RotatedBoxEncode)
    .INPUT(anchor_box, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gt_box, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(weight, ListFloat, {1.0, 1.0, 1.0, 1.0, 1.0})
    .OP_END_FACTORY_REG(RotatedBoxEncode)
```

## Brief

RotatedBoxEncode. 

## Inputs

Two inputs, including:
- anchor_box: A 3D Tensor of float32 (float16) with shape (B, 5, N).
"B" indicates the number of batch size
"N" indicates the number of bounding boxes, and the value "5" refers to
"x0", "x1", "y0", "y1" and "angle".
- gt_box: A 3D Tensor of float32 (float16) with shape (B, 5, N).
"B" indicates the number of batch size
"N" indicates the number of bounding boxes, and the value "5" refers to
"x0", "x1", "y0", "y1" and "angle". 

## Outputs

- y: A 3D Tensor of type float32 (float16) with shape (B, 5, N),
specifying the variations between all anchor boxes and ground truth boxes.

## Attributes

- weight: A float list for "x0", "x1", "y0", "y1" and "angle",
defaults to [1.0, 1.0, 1.0, 1.0, 1.0].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 anchor_box: float16,float32
- input1 gt_box: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
