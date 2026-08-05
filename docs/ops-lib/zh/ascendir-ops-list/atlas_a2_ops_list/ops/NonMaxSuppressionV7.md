# NonMaxSuppressionV7

```c
REG_OP(NonMaxSuppressionV7)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(max_output_size, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(iou_threshold, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(score_threshold, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(index_id, TensorType({DT_FLOAT16}))
    .OUTPUT(selected_indices, TensorType({DT_INT32}))
    .ATTR(center_point_box, Int, 0)
    .ATTR(max_boxes_size, Int, 0)
    .OP_END_FACTORY_REG(NonMaxSuppressionV7)
```

## Brief

Greedily selects a subset of bounding boxes in descending order of
score . 

## Inputs

- boxes: A input tensor with shape [num_batches,spatial_dimension,4].
The single box data format is indicated by center_point_box.
Support float16, float32 type.
- scores: A input tensor with shape [num_batches,num_classes,spatial_dimension]
Support float16, float32 type.
- max_output_size: A scalar integer tensor representing the maximum number
of boxes to be selected by non max suppression. Must be int32 type.
- iou_threshold: A 0-D float tensor representing the threshold for deciding
whether boxes overlap too much with respect to IOU. Must be float32 type.
- score_threshold: A 0-D float tensor representing the threshold for
deciding when to remove boxes based on score. Must be float32 type. 
- index_id: A input tensor with shape [num_batches,num_classes,spatial_dimension,3]
the last dim representing (batch_id,class_id,index_id). Must be float16 type. 

## Outputs

selected_indices: A 2-D integer tensor of shape [M] representing the
selected indices from the boxes tensor, where M <= max_output_size. Must be int32 type. 

## Attributes

- center_point_box:Integer indicate the format of the box data.
The default is 0. 0 - the box data is supplied as [y1, x1, y2, x2]
where (y1, x1) and (y2, x2) are the coordinates of any diagonal pair
of box corners and the coordinates can be provided as normalized
(i.e., lying in the interval [0, 1]) or absolute.Mostly used for TF models.
1 - the box data is supplied as [x_center, y_center, width, height].
Mostly used for Pytorch models. 
- max_boxes_size: An optional attribute integer representing the real maximum
number of boxes to be selected by non max suppression . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float16,float32
- input1 scores: float16,float32
- input2 max_output_size: int32
- input3 iou_threshold: float32
- input4 score_threshold: float32
- input5 index_id: float16
- output0 selected_indices: int32

## Attention Constraints

Input boxes and scores support float16, float32 type. 

## Third-party framework compatibility

Compatible with onnx NonMaxSuppression operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
