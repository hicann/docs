# SortedNMS

```c
REG_OP(SortedNMS)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(sorted_scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(input_indices, TensorType({DT_INT32}))
    .INPUT(max_output_size, TensorType({DT_INT32}))
    .INPUT(iou_threshold, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(score_threshold, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(selected_indices, TensorType({DT_INT32}))
    .ATTR(offset, Int, 0)
    .OP_END_FACTORY_REG(SortedNMS)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of
score . 

## Inputs

- boxes: A 2-D float tensor of shape [num_boxes, 4]. They are expected to be in (x1, y1, x2, y2) format
with 0 <= x1 < x2 and 0 <= y1 < y2. Supported type: float16, float32. Supported format: ND.
- sorted_scores: A 1-D float tensor of shape [num_boxes] representing boxes' scores, which is sorted
by descending order. Supported type: float16, float32. Supported format: ND.
- input_indices: A 1-D integer tensor of shape [num_boxes] representing the indices for each row of
boxes that would sort row of boxes by scores in descending order. Supported type: int32. Supported format: ND.
- max_output_size: A scalar integer tensor representing the maximum number
of boxes to be selected by non max suppression. Supported type: int32. Supported format: ND.
- iou_threshold: A 0-D float tensor representing the threshold for deciding
whether boxes overlap too much with respect to IOU. Supported type: float16, float32. Supported format: ND.
- score_threshold: A 0-D float tensor representing the threshold for
deciding when to remove boxes based on score. Supported type: float16, float32. Supported format: ND . 

## Outputs

- selected_indices: A 1-D integer tensor of shape [M] representing the selected
indices from the boxes tensor, where M <= max_output_size. Supported type: int32. Supported format: ND . 

## Attributes

offset: An optional int. Defaults to "0". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float16,float32
- input1 sorted_scores: float16,float32
- input2 input_indices: int32
- input3 max_output_size: int32
- input4 iou_threshold: float16,float32
- input5 score_threshold: float16,float32
- output0 selected_indices: int32

## Attention Constraints

Input boxes and scores must be float type . 


---

[Back to Operator Specifications (Ascend950)](../README.md)
