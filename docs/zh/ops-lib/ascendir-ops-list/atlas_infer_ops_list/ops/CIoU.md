# CIoU

```c
REG_OP(CIoU)
    .INPUT(bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gtboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(overlap, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(atan_sub, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(trans, Bool, false)
    .ATTR(is_cross, Bool, true)
    .ATTR(mode, String, "iou")
    .ATTR(atan_sub_flag, Bool, false)
    .OP_END_FACTORY_REG(CIoU)
```

## Brief

First calculate the minimum closure area of the two boxes, IoU,
The CIoU is obtained by combining the center distance and width to height ratio and IoU. 

## Inputs

Two inputs, including:
- bboxes: Bounding boxes, a 2D tensor of type float16 or float32 with
shape (4, N). "N" indicates the number of bounding boxes, and the value
"4" refers to [x1, y1, x2, y2] or [x, y, w, h].
- gtboxes: Ground-truth boxes, a 2D tensor of type float16 or float32
with shape (4, M). "M" indicates the number of ground truth boxes, and
the value "4" refers to [x1, y1, x2, y2] or [x, y, w, h]. Data type should
be the same with bboxes. 

## Outputs

Two outputs, including:
- overlap: A 2D tensor of type float16 or float32 with shape [M, N] or [1, N],
specifying the IoU(Intersection over Union) or IoF(Intersection over Foreground) ratio.
Data type should be the same with inputs.
- atan_sub: A 2D tensor of type float16 or float32 with shape [M, N] or [1, N],
specifying the IoU or IoF ratio. Data type should be the same with inputs.
The shape of atan_sub is the same with overlap. 

## Attributes

- trans: An optional bool, true for 'xywh', false for 'xyxy'.
- is_cross: An optional bool, control whether the output shape is [M, N] or [1, N].
The output shape is [M, N] if is_cross is true. The output shape is [1, N] if is_cross is false.
- mode: An optional string, computation mode, a character string with the value range of [iou, iof].
- atan_sub_flag: An optional bool, control whether to output atan_sub.
If true, output atan_sub. If false, not output atan_sub. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bboxes: float16,float32
- input1 gtboxes: float16,float32
- output0 overlap: float16,float32
- output1 atan_sub: float16,float32

## Attention Constraints

- The values of M and N must be consistent and multiples of 1024.
- "is_cross" only support false, "atan_sub_flag" only support true.
- This interface does not support jit_compile=False(dynamic compilation) currently.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
