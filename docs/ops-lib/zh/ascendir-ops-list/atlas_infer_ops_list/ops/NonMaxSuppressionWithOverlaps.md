# NonMaxSuppressionWithOverlaps

```c
REG_OP(NonMaxSuppressionWithOverlaps)
    .INPUT(overlaps, TensorType({DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT}))
    .INPUT(max_output_size, TensorType({DT_INT32}))
    .INPUT(overlap_threshold, TensorType({DT_FLOAT}))
    .INPUT(score_threshold, TensorType({DT_FLOAT}))
    .OUTPUT(selected_indices, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(NonMaxSuppressionWithOverlaps)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of
score . 

## Inputs

Input overlaps and  scores must be float type. Inputs include:
- overlaps: A 2-D float tensor of shape [num_boxes, num_boxes]
representing the n-by-n box overlap values.
- scores: A 1-D float tensor of shape [num_boxes] representing a single
score corresponding to each box (each row of boxes).
- max_output_size: A scalar integer tensor representing the maximum number
of boxes to be selected by non max suppression.
- overlap_threshold: A 0-D float tensor representing the threshold for
deciding whether boxes overlap too.
- score_threshold: A 0-D float tensor representing the threshold for
deciding when to remove boxes based on score . 

## Outputs

selected_indices: A 1-D integer tensor of shape [M] representing the
selected indices from the boxes tensor, where M <= max_output_size . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 overlaps: float32
- input1 scores: float32
- input2 max_output_size: int32
- input3 overlap_threshold: float32
- input4 score_threshold: float32
- output0 selected_indices: int32

## Third-party framework compatibility

Compatible with tensorflow NonMaxSuppressionWithOverlaps operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
