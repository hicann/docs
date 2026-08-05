# GIoU

```c
REG_OP(GIoU)
    .INPUT(bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gtboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(overlap, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(trans, Bool, false)
    .ATTR(is_cross, Bool, true)
    .ATTR(mode, String, "iou")
    .OP_END_FACTORY_REG(GIoU)
```

## Brief

First calculate the minimum closure area of the two boxes, IoU,
the proportion of the closed area that does not belong to the two boxes in the closure area,
and finally subtract this proportion from IoU to get GIoU . 

## Inputs

Two inputs, including:
- bboxes: Bounding boxes, a 2D Tensor of type float16 or float32 with
shape (N, 4). "N" indicates the number of bounding boxes, and the value
"4" refers to [x1, y1, x2, y2] or [x, y, w, h].
- gtboxes: Ground-truth boxes, a 2D Tensor of type float16 or float32
with shape (M, 4). "M" indicates the number of ground truth boxes, and
the value "4" refers to [x1, y1, x2, y2] or [x, y, w, h] . 

## Outputs

overlap: A 2D Tensor of type float16 or float32 with shape [M, N] or [1, N],
specifying the IoU or IoF ratio . 

## Attributes

- trans: An optional bool, true for 'xywh', false for 'xyxy'.
- is_cross: An optional bool, control whether the output shape is [M, N] or [1, N]
- mode: Computation mode, a character string with the value range of [iou, iof] .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bboxes: float16,float32
- input1 gtboxes: float16,float32
- output0 overlap: float16,float32

## Attention Constraints

Only computation of float16 data is supported. To avoid overflow, the input
length and width are scaled by 0.2 internally.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
