# BoundingBoxEncode

```c
REG_OP(BoundingBoxEncode)
    .INPUT(anchor_box, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(ground_truth_box, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(delats, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(means, ListFloat, {0.0, 0.0, 0.0, 0.0})
    .ATTR(stds, ListFloat, {1.0, 1.0, 1.0, 1.0})
    .OP_END_FACTORY_REG(BoundingBoxEncode)
```

## Brief

Computes the coordinate variations between bboxes and ground truth
boxes. It is a customized FasterRcnn operator.

## Inputs

Two inputs, including:
- anchor_box: Anchor boxes. A 2D Tensor of float32 or float16 with shape (N, 4).
"N" indicates the number of bounding boxes, and the value "4" refers to
"x0", "x1", "y0", "y1".
- ground_truth_box: Ground truth boxes. A 2D Tensor of float32 or float16 with
shape (N, 4). "N" indicates the number of bounding boxes, and the value "4"
refers to "x0", "x1", "y0" "y1". 

## Outputs

delats: A 2D Tensor of type float32 or float16 with shape (N, 4),
specifying the variations between all anchor boxes and ground truth boxes.

## Attributes

- means: An index of type int. Defaults to [0,0, 0,0].
"deltas" = "deltas" x "stds" + "means".
- stds: An index of type int. Defaults to [1.0, 1.0, 1.0, 1.0].
"deltas" = "deltas" x "stds" + "means". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 anchor_box: float16
- input1 ground_truth_box: float16
- output0 delats: float16


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
