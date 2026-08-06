# FSRDetectionOutput

```c
REG_OP(FSRDetectionOutput)
    .INPUT(rois, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(bbox_delta, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(score, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(im_info, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OPTIONAL_INPUT(actual_rois_num, TensorType({DT_INT32}))
    .OUTPUT(actual_bbox_num, TensorType({DT_INT32}))
    .OUTPUT(box, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(batch_rois, Int, 1)
    .REQUIRED_ATTR(num_classes, Int)
    .REQUIRED_ATTR(score_threshold, Float)
    .REQUIRED_ATTR(iou_threshold, Float)
    .OP_END_FACTORY_REG(FSRDetectionOutput)
```

## Brief

Returns detection result .

## Inputs

Five inputs, including:
- rois: An NCHW tensor of type floa16 or float32, output from operator
proposal_d at the preceding layer, used as the input of operator
FSRDetectionOutput.
- bbox_delta: An NCHWC0 tensor of type floa16 or float32, specifying the
prediction offset, used to update the coordinates [x1, y1, x2, y2] of each ROI.
- score: An NCHWC0 tensor of type floa16 or float32, specifying the
probability of each class. Class 0 is the background class.
- im_info: An ND tensor of type float16 or float32, specifying the Image
information.
- actual_rois_num: An optional NCHW tensor of type int32, specifying the
number of valid boxes per batch. 

## Outputs

- actual_bbox_num: A tensor of type int32 With shape [bacth, num_classes],
specifying the number of output boxes .
- box: A tensor of type float16 or float32 for proposal of actual output,
with output shape [batch, numBoxes,8].
8 means [x1, y1, x2, y2, score, label, batchID, NULL], the maximum value of
numBoxes is 1024.
That is, take min (the maximum number of input boxes, 1024) .

## Attributes

- batch_rois: An optional int, specifying the number of images to be
predicted. Defaults to "1".
- num_classes: An required int, specifying the number of classes to be
predicted. The value must be greater than 0.
- score_threshold: An required float, specifying the threshold for box
filtering. The value range is [0.0, 1.0].
- iou_threshold: An required float, specifying the confidence threshold for
box filtering, which is the output "obj" of operator Region. The value range
is (0.0, 1.0). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 rois: float16
- input1 bbox_delta: float16
- input2 score: float16
- input3 im_info: float16
- input4 actual_rois_num: int32
- output0 actual_bbox_num: int32
- output1 box: float16

## Attention Constraints

- totalnum < max_rois_num * batch_rois.
- "score" must be with shape (total_num, (num_classes+15)//16, 1, 1, 16),
where "total_num" indicates the number of valid input boxes of all images.
- "bbox_delta" must be with shape (total_num, (num_classes*4+15)//16, 1, 1,
16), where "total_num" indicates the number of valid input boxes of all
images. 

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
