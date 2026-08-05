# Iou

```c
REG_OP(Iou)
    .INPUT(bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gtboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(overlap, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(mode, String, "iou")
    .ATTR(eps, Float, 1.0)
    .ATTR(aligned, Bool, false)
    .OP_END_FACTORY_REG(Iou)
```

## Brief

Computes the intersection over union (iou) or the intersection over
foreground (iof) based on the ground-truth and predicted regions . 

## Inputs

Two inputs, including:
- bboxes: Bounding boxes, a 2D Tensor of type float16 or float32 with
shape (N, 4). "N" indicates the number of bounding boxes, and the value
"4" refers to "x0", "x1", "y0", and "y1".
- gtboxes: Ground-truth boxes, a 2D Tensor of type float16 or float32
with shape (M, 4). It's dtype should be same as bboxes.
"M" indicates the number of ground truth boxes, and
the value "4" refers to "x0", "x1", "y0", and "y1" . 

## Outputs

overlap: A 2D Tensor of type float16 or float32 with shape [M, N] or [M, 1], specifying
the IoU or IoF ratio . It's dtype should be same as bboxes. 

## Attributes

- mode: Computation mode, a character string with the value range of [iou, iof].
default value is iou .
- eps: An optional float, prevent division by 0, default value is 1.0 .
The value can only choose one of those values: [0, 0.01, 1] when Soc Version is : 
Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component. 
Atlas A3 Training Series Product/Atlas A3 Inference Series Product. 
Atlas Training Series Product. 
Atlas Inference Series Product. 
- aligned: A bool value, if aligned is true, calculate the ious between each aligned pair of bboxes and gtboxes.
default value is false . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bboxes: float16,float32
- input1 gtboxes: float16,float32
- output0 overlap: float16,float32

## Attention Constraints

Computation of float16 and float32 data are supported. To avoid overflow, the input
length and width are scaled by 0.2 internally.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
