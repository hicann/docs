# NonMaxSuppression

```c
REG_OP(NonMaxSuppression)
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT}))
    .INPUT(max_output_size, TensorType({DT_INT32}))
    .OUTPUT(selected_indices, TensorType({DT_INT32}))
    .ATTR(iou_threshold, Float, 0.5f)
    .OP_END_FACTORY_REG(NonMaxSuppression)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of
score . 

## Inputs

Input boxes and  scores must be float type. Inputs include:
- boxes: A 2-D float tensor of shape [num_boxes, 4].
- scores: A 1-D float tensor of shape [num_boxes] representing a single
score corresponding to each box (each row of boxes).
- max_output_size: A scalar integer tensor representing the maximum number
of boxes to be selected by non max suppression . 

## Outputs

selected_indices: A 1-D integer tensor of shape [M] representing the selected
indices from the boxes tensor, where M <= max_output_size . 

## Attributes

iou_threshold: A float representing the threshold for deciding whether boxes
overlap too much with respect to IOU , default is 0.5f.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 boxes: float32
- input1 scores: float32
- input2 max_output_size: int32
- output0 selected_indices: int32

## Attention Constraints

Input boxes and  scores must be float type . 

## Third-party framework compatibility

Compatible with tensorflow NonMaxSuppression operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
