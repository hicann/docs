# Iou3D

```c
REG_OP(Iou3D)
    .INPUT(bboxes, TensorType({DT_FLOAT}))
    .INPUT(gtboxes, TensorType({DT_FLOAT}))
    .OUTPUT(iou, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(Iou3D)
```

## Brief

Calculate the intersection ratio of two rotated cuboids . 

## Inputs

- bboxes : data of grad increment, a 3D Tensor of type float32 with
shape (B, 7, N). "N" indicates the number of boxes, and the value
"7" refers to [x, y, z, w, h, d, theta].
- gtboxes: Bounding boxes, a 3D Tensor of type float32 with
shape (B, 7, K). "K" indcates the number of boxes, and the value
"7" refers to [x, y, z, w, h, d, theta].

## Outputs

iou: A 3D Tensor of float32 with shape [B, N, K].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bboxes: float32
- input1 gtboxes: float32
- output0 iou: float32

## Attention Constraints

In each batch, the invalid box cannot appear before the valid box.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
