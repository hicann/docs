# RotatedIou

```c
REG_OP(RotatedIou)
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(query_boxes, TensorType({DT_FLOAT}))
    .OUTPUT(iou, TensorType({DT_FLOAT}))
    .ATTR(trans, Bool, false)
    .ATTR(mode, String, "iou")
    .ATTR(is_cross, Bool, true)
    .ATTR(v_threshold, Float, 0)
    .ATTR(e_threshold, Float, 0)
    .OP_END_FACTORY_REG(RotatedIou)
```

## Brief

RotatedIou . 

## Inputs

- boxes : data of grad increment, a 3D Tensor of type float32 with
shape (B, 5, N). "N" indicates the number of boxes, and the value
"5" refers to [x1, y1, x2, y2, theta] or [x, y, w, h, theta].
- query_boxes: Bounding boxes, a 3D Tensor of type float32 with
shape (B, 5, K). "K" indicates the number of boxes, only supported to be less than 1600,
and the value  "5" refers to [x1, y1, x2, y2, theta] or [x, y, w, h, theta].

## Outputs

iou: A 3D Tensor of float32 with shape [B, N, K].

## Attributes

- trans: An optional attr, true for 'xyxyt', false for 'xywht'.
- mode: An optional attr, a character string with the value range of ['iou', 'iof'],
only support 'iou' now.
- is_cross: Cross calculation when it is True, and one-to-one calculation when it is False.
- v_threshold: An optional attr, provide condition relaxation for intersection calculation.
- e_threshold: An optional attr, provide condition relaxation for intersection calculation.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float32
- input1 query_boxes: float32
- output0 iou: float32

## Attention Constraints

In each batch, the invalid box cannot appear before the valid box.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
