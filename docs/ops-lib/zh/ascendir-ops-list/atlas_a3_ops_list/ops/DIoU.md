# DIoU

```c
REG_OP(DIoU)
    .INPUT(bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gtboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(overlap, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(trans, Bool, false)
    .ATTR(is_cross, Bool, true)
    .ATTR(mode, String, "iou")
    .OP_END_FACTORY_REG(DIoU)
```

## Brief

First calculate the minimum closure area of the two boxes, IoU,
The DIoU is obtained by combining the center distance and IoU. 

## Inputs

Two inputs, including:
- bboxes: Bounding boxes, a 2D Tensor of type float16 or float32 with
shape (4, N). "N" indicates the number of bounding boxes, and the value
"4" refers to [x1, y1, x2, y2] or [x, y, w, h].
- gtboxes: Ground-truth boxes, a 2D Tensor of type float16 or float32
with shape (4, M). "M" indicates the number of ground truth boxes, and
the value "4" refers to [x1, y1, x2, y2] or [x, y, w, h] . 

## Outputs

overlap: A 2D Tensor of type float16 or float32 with shape [N, M] or [1, N],
specifying the IoU or IoF ratio . 

## Attributes

- trans: An optional bool, true for 'xywh', false for 'xyxy', default value is false.
- is_cross: An optional bool, control whether the output shape is [N, M] or [1, N], default value is false.
- mode: An optional string, computation mode, a character string with the value range of [iou, iof],
default value is 'iou'. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bboxes: float16,float32
- input1 gtboxes: float16,float32
- output0 overlap: float16,float32

## Attention Constraints

"is_cross" only support false.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
