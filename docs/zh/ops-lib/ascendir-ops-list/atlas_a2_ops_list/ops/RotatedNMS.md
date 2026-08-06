# RotatedNMS

```c
REG_OP(RotatedNMS)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(labels, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(selected_detections, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(keep_indices, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(iou_threshold, Float)
    .ATTR(is_angle, Bool, true)
    .OP_END_FACTORY_REG(RotatedNMS)
```

## Brief

Performs non-maximum suppression (NMS) on the rotated boxes according
to their intersection-over-union (IoU). Rotated NMS interatively removes lower
scoring rotated boxes which have an IoU greater than iou_threshold with
another (higher scoring) rotated box.

## Inputs

Three inputs, including:
- boxes: A 2D Tensor of float16 or float32 with shape (N, 5). Rotated boxes to
perform NMS on. They are expected to be in (x1, y1, x2, y2, angle_degress) format.
- scores: A 1D Tensor of float16 or float32 with shape (N). Scores for each one of
the rotated boxes.
- labels: A 1D Tensor of int32 or int64 with shape (N). Labels for each one of
the rotated boxes.

## Outputs

Two outputs, including:
- selected_detections: A 2D Tensor of float16 or float32 with shape (N, 5).
The selected boxes that kept by Rotated NMS, sorted in decreasing order of scores.
- keep_indices: A 1D Tensor of int32 or int64 with shape (N). The indices of
selected_detections.

## Attributes

iou_threshold: A required float attribute. Discards all overlapping rotated
boxes with IoU < iou_threshold.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 boxes: float16,float32
- input1 scores: float16,float32
- input2 labels: int32,int64
- output0 selected_detections: float16,float32
- output1 keep_indices: int32,int64

## Attention Constraints

Currently, the tensor type of input (boxes, scores) only support float.
The tensor type of keep_indices only support int32.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
