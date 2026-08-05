# SSDDetectionOutput

```c
REG_OP(SSDDetectionOutput)
    .INPUT(bbox_delta, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(score, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(anchors, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(out_boxnum, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(num_classes, Int, 2)
    .ATTR(share_location, Bool, true)
    .ATTR(background_label_id, Int, 0)
    .ATTR(iou_threshold, Float, 0.3f)
    .ATTR(top_k, Int, 200)
    .ATTR(eta, Float, 1.0)
    .ATTR(variance_encoded_in_target, Bool, false)
    .ATTR(code_type, Int, 1)
    .ATTR(keep_top_k, Int, -1)
    .ATTR(confidence_threshold, Float, 0.0)
    .OP_END_FACTORY_REG(SSDDetectionOutput)
```

## Brief

Returns detection result .

## Inputs

Three inputs, including:
- bbox_delta: An ND tensor of type floa16 or float32, specifying the box
loc predictions, used as the input of operator SSDDetectionOutput.
- score: An ND tensor of type floa16 or float32, specifying the box
confidences data, used as the input of operator SSDDetectionOutput.
- anchors: An ND tensor of type floa16 or float32, output from operator
PriorBoxD, used as the input of operator SSDDetectionOutput. 

## Outputs

- out_boxnum: A tensor of type int32, specifying the number of output boxes.
- y: A tensor of type float16 or float32 with shape [batch,keep_top_k, 8],
describing the information of each output box.
In output shape, 8 means (batchID, label(classID), score (class probability),
xmin, ymin, xmax, ymax, null).
It is a custom operator. It has no corresponding operator in Caffe.

## Attributes

- num_classes: An optional int, specifying the number of classes to be
predicted. Defaults to "2". The value must be greater than 1 and lesser
than 1025.
- share_location: An optional bool, specify the shared location.
Defaults to true.
- background_label_id: An optional int, specify the background label id.
Must be 0.
- iou_threshold: An optional float, specify the nms threshold. Default to
0.3.
- top_k: An optional int, specify the topk value. Defaults to 200.
- eta: An optional float, specify the eta value. Defaults to 1.0.
- variance_encoded_in_target: An optional bool, specify whether variance
encoded in target or not. Defaults to false.
- code_type: An optional int, specify the code type. Defaults to 1.
The corner is 1, center_size is 2, corner_size is 3.
- keep_top_k: An optional int, specify the topk value after nms.
Defaults to -1.
- confidence_threshold: An optional float, specify the topk filter threshold.
Only consider detections with confidence greater than the threshold. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bbox_delta: float16
- input1 score: float16
- input2 anchors: float16
- output0 out_boxnum: int32
- output1 y: float16


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
