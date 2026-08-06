# RotatedOverlaps

```c
REG_OP(RotatedOverlaps)
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(query_boxes, TensorType({DT_FLOAT}))
    .OUTPUT(overlaps, TensorType({DT_FLOAT}))
    .ATTR(trans, Bool, false)
    .OP_END_FACTORY_REG(RotatedOverlaps)
```

## Brief

RotatedOverlaps . 

## Inputs

- boxes : data of grad increment, a 3D Tensor of type float32 with
shape (B, 5, N). "N" indicates the number of boxes, and the value
"5" refers to [x1, y1, x2, y2, theta] or [x, y, w, h, theta].
- query_boxes: Bounding boxes, a 3D Tensor of type float32 with
shape (B, 5, K). "K" indicates the number of boxes, and the value
"5" refers to [x1, y1, x2, y2, theta] or [x, y, w, h, theta].

## Outputs

overlaps: A 3D Tensor of type float32 with shape [B, N, K].

## Attributes

trans: An optional attr, true for 'xyxyt', false for 'xywht'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float32
- input1 query_boxes: float32
- output0 overlaps: float32

## Attention Constraints

In each batch, the invalid box cannot appear before the valid box.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
