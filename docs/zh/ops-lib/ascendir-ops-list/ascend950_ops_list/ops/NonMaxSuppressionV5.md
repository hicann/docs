# NonMaxSuppressionV5

```c
REG_OP(NonMaxSuppressionV5)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(max_output_size, TensorType({DT_INT32}))
    .INPUT(iou_threshold, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(score_threshold, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(soft_nms_sigma, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(selected_indices, TensorType({DT_INT32}))
    .OUTPUT(selected_scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(valid_outputs, TensorType({DT_INT32}))
    .ATTR(pad_to_max_output_size, Bool, false)
    .REQUIRED_ATTR(T, Type)
    .OP_END_FACTORY_REG(NonMaxSuppressionV5)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of score,
pruning away boxes that have high intersection-over-union (IOU) overlap
with previously selected boxes . 

## Inputs

- boxes: A 2-D float tensor of shape `[num_boxes, 4]`.
- scores: A 1-D float tensor of shape `[num_boxes]` representing a single
score corresponding to each box (each row of boxes).
- max_output_size: A scalar integer tensor representing the maximum number of
boxes to be selected by non max suppression.
- iou_threshold: A 0-D float tensor representing the threshold for deciding whether
boxes overlap too much with respect to IOU.
- score_threshold: A 0-D float tensor representing the threshold for deciding when to
remove boxes based on score.
- soft_nms_sigma: A 0-D float tensor representing the sigma parameter for Soft NMS .

## Outputs

- selected_indices: A 1-D integer tensor of shape [M] representing the
selected indices from the boxes tensor, where M <= max_output_size.
- selected_scores: A 1-D float tensor of shape `[M]` representing the corresponding
scores for each selected box, where `M <= max_output_size`.
- valid_outputs: A 0-D integer tensor representing the number of valid
elements in selected_indices, with the valid elements appearing first . 

## Attributes

- pad_to_max_output_size: An optional bool. If true, the output `selected_indices` is padded to be of length
`max_output_size`. Defaults to false. If not specified, defaults to false.
- T: The data type of the output tensors. Can be float16, float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 boxes: float16,float32
- input1 scores: float16,float32
- input2 max_output_size: int32
- input3 iou_threshold: float16,float32
- input4 score_threshold: float16,float32
- input5 soft_nms_sigma: float16,float32
- output0 selected_indices: int32
- output1 selected_scores: float16,float32
- output2 valid_outputs: int32

## Third-party framework compatibility

Compatible with tensorflow NonMaxSuppressionV5 operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
