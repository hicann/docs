# CombinedNonMaxSuppression

```c
REG_OP(CombinedNonMaxSuppression)
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT}))
    .INPUT(max_output_size_per_class, TensorType({DT_INT32}))
    .INPUT(max_total_size, TensorType({DT_INT32}))
    .INPUT(iou_threshold, TensorType({DT_FLOAT}))
    .INPUT(score_threshold, TensorType({DT_FLOAT}))
    .OUTPUT(nmsed_boxes, TensorType({DT_FLOAT}))
    .OUTPUT(nmsed_scores, TensorType({DT_FLOAT}))
    .OUTPUT(nmsed_classes, TensorType({DT_FLOAT}))
    .OUTPUT(valid_detections, TensorType({DT_INT32}))
    .ATTR(pad_per_class, Bool, false)
    .ATTR(clip_boxes, Bool, true)
    .OP_END_FACTORY_REG(CombinedNonMaxSuppression)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of score,
This operation performs non_max_suppression on the inputs per batch, across all classes.

## Inputs

- boxes: A 4-D float tensor of shape `[batch_size, num_boxes, q, 4]`. If `q` is 1 then
same boxes are used for all classes otherwise, if `q` is equal to number of
classes, class-specific boxes are used.
- scores: A 3-D float tensor of shape `[batch_size, num_boxes, num_classes]`
representing a single score corresponding to each box (each row of boxes).
- max_output_size_per_class: An int32 scalar integer tensor representing the maximum number of
boxes to be selected by non max suppression per class.
- max_total_size: An int32 scalar representing maximum number of boxes retained over all classes.
- iou_threshold: A 0-D float tensor representing the threshold for deciding whether
boxes overlap too much with respect to IOU.
- score_threshold: A 0-D float tensor representing the threshold for deciding when to remove
boxes based on score . 

## Outputs

- nmsed_boxes: Type is float
- nmsed_scores: Type is float
- nmsed_classes: Type is float
- valid_detections: Type is INT32

## Attributes

- pad_per_class: If false, the output nmsed boxes, scores and classes
are padded/clipped to `max_total_size`. If true, the
output nmsed boxes, scores and classes are padded to be of length
`max_size_per_class`*`num_classes`, unless it exceeds `max_total_size` in
which case it is clipped to `max_total_size`. Defaults to false.
- clip_boxes: If true, assume the box coordinates are between [0, 1] and clip the output boxes
if they fall beyond [0, 1]. If false, do not do clipping and output the box
coordinates as it is. If not specified, defaults to true . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float16,float32
- input1 scores: float16,float32
- input2 max_output_size_per_class: int32
- input3 max_total_size: int32
- input4 iou_threshold: float32
- input5 score_threshold: float32
- output0 nmsed_boxes: float16,float32
- output1 nmsed_scores: float16,float32
- output2 nmsed_classes: float16,float32
- output3 valid_detections: int32
### AI CPU
- input0 boxes: float32
- input1 scores: float32
- input2 max_output_size_per_class: int32
- input3 max_total_size: int32
- input4 iou_threshold: float32
- input5 score_threshold: float32
- output0 nmsed_boxes: float32
- output1 nmsed_scores: float32
- output2 nmsed_classes: float32
- output3 valid_detections: int32

## Third-party framework compatibility

Compatible with tensorflow CombinedNonMaxSuppression operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
