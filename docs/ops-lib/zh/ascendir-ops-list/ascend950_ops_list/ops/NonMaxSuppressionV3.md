# NonMaxSuppressionV3

```c
REG_OP(NonMaxSuppressionV3)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(max_output_size, TensorType({DT_INT32}))
    .INPUT(iou_threshold, TensorType({DT_FLOAT16,DT_FLOAT}))
    .INPUT(score_threshold, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(selected_indices, TensorType({DT_INT32}))
    .ATTR(offset, Int, 0)
    .OP_END_FACTORY_REG(NonMaxSuppressionV3)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of
score . 

## Inputs

Input boxes and  scores must be float type. Inputs include:
- boxes: A 2-D float tensor of shape [num_boxes, 4]. They are expected to be in (x1, y1, x2, y2)
format with x1 < x2 and y1 < y2.
- scores: A 1-D float tensor of shape [num_boxes] representing a single
score corresponding to each box (each row of boxes).
- max_output_size: A scalar integer tensor representing the maximum number
of boxes to be selected by non max suppression.
- iou_threshold: A 0-D float tensor representing the threshold for deciding
whether boxes overlap too much with respect to IOU.
- score_threshold: A 0-D float tensor representing the threshold for
deciding when to remove boxes based on score . 

## Outputs

selected_indices: A 1-D integer tensor of shape [M] representing the selected
indices from the boxes tensor, where M <= max_output_size . 

## Attributes

offset: An optional int. Defaults to 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 boxes: float16,float32
- input1 scores: float16,float32
- input2 max_output_size: int32
- input3 iou_threshold: float16,float32
- input4 score_threshold: float16,float32
- output0 selected_indices: int32

## Attention Constraints

Input boxes and  scores must be float type . 

## Third-party framework compatibility

Compatible with tensorflow NonMaxSuppressionV3 operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
