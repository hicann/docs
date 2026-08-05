# BatchMultiClassNonMaxSuppression

```c
REG_OP(BatchMultiClassNonMaxSuppression)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(clip_window, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(num_valid_boxes, TensorType({DT_INT32}))
    .OUTPUT(nmsed_boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(nmsed_scores, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(nmsed_classes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(nmsed_num, TensorType({DT_INT32}))
    .REQUIRED_ATTR(score_threshold, Float)
    .REQUIRED_ATTR(iou_threshold, Float)
    .REQUIRED_ATTR(max_size_per_class, Int)
    .REQUIRED_ATTR(max_total_size, Int)
    .ATTR(change_coordinate_frame, Bool, false)
    .ATTR(transpose_box, Bool, false)
    .ATTR(image_size, ListInt, {})
    .OP_END_FACTORY_REG(BatchMultiClassNonMaxSuppression)
```

## Brief

Computes nms for input boxes and score, support multiple batch and classes.
will do clip to window, score filter, top_k, and nms

## Inputs

Four inputs, including:
- boxes: boxes, a 4D Tensor of type float16 or float32 with
shape (batch, num_anchors, num_classes, 4). "batch" indicates the batch size of image,
and "num_anchors" indicates num of boxes, and "num_classes" indicates classes of detect.
and the value "4" refers to "x0", "x1", "y0", and "y1".
- scores: boxes, a 4D Tensor of type float16 or float32 with
shape (batch, num_anchors, num_classes).
- clip_window: window size, a 2D Tensor of type float16 or float32 with
shape (batch, 4). 4" refers to "anchor_x0", "anchor_x1", "anchor_y0", and "anchor_y1".
- num_valid_boxes: valid boxes number for each batch, a 1D Tensor of type int32 with
shape (batch,) . 

## Outputs

- nmsed_boxes: A 3D Tensor of type float16 or float32 with shape (batch, max_total_size, 4),
specifying the output nms boxes per batch.
- nmsed_scores: A 2D Tensor of type float16 or float32 with shape (batch, max_total_size),
specifying the output nms score per batch.
- nmsed_classes: A 2D Tensor of type float16 or float32 with shape (batch, max_total_size),
specifying the output nms class per batch.
- nmsed_num: A 1D Tensor of type int32 with shape (batch), specifying the valid num of nmsed_boxes .

## Attributes

- score_threshold: A required attribute of type float32, specifying the score filter iou iou_threshold.
- iou_threshold: A required attribute of type float32, specifying the nms iou iou_threshold.
- max_size_per_class: A required attribute of type int, specifying the nms output num per class.
- max_total_size: A required attribute of type int, specifying the the nms output num per batch.
- change_coordinate_frame: A optional attribute of type bool, whether to normalize coordinates after clipping.
- transpose_box: A optional attribute of type bool, whether inserted transpose before this op. must be "false".
- image_size: A optional attribute of type ListInt, the size of the image.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float16
- input1 scores: float16
- input2 clip_window: float16
- input3 num_valid_boxes: int32
- output0 nmsed_boxes: float16
- output1 nmsed_scores: float16
- output2 nmsed_classes: float16
- output3 nmsed_num: int32

## Attention Constraints

Only computation of float16 or float32 data is supported.
Note: when the class num per image * max_size_per_class is too big, will compile fail with ERROR-insufficient memory


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
