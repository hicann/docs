# Proposal

```c
REG_OP(Proposal)
     .INPUT(cls_prob, TensorType({DT_FLOAT16, DT_FLOAT}))
     .INPUT(bbox_delta, TensorType({DT_FLOAT16, DT_FLOAT}))
     .INPUT(im_info, TensorType({DT_FLOAT16, DT_FLOAT}))
     .OUTPUT(rois, TensorType({DT_FLOAT16, DT_FLOAT}))
     .OUTPUT(actual_rois_num, TensorType({DT_INT32}))
     .ATTR(feat_stride, Float, 16)
     .ATTR(base_size, Float, 16)
     .ATTR(min_size, Float, 16)
     .ATTR(ratio, ListFloat, {0.5, 1, 2})
     .ATTR(scale, ListFloat, {8, 16, 32})
     .ATTR(pre_nms_topn, Int, 3000)
     .ATTR(post_nms_topn, Int, 304)
     .ATTR(iou_threshold, Float, 0.7)
     .ATTR(output_actual_rois_num, Bool, false)
     .OP_END_FACTORY_REG(Proposal)
```

## Brief

Performs object detection . 

## Inputs

- cls_prob: An NCHW tensor of type float16 or float32,
specifying the probability of the proposal is the background class.
- bbox_delta: An NCHW tensor of type float16 or float32, specifying the coordinates of the proposals bounding boxes.
- im_info: An ND tensor of type float16 or float32, specifying the Image information .

## Outputs

- rois: A Tensor with shape [batch, 5, post_nms_topn],
of type float16 or float32, specifying the output box information.
"post_nms_topn" must be a multiple of 16. The dimension "5" indicates (batchID, x1, y1, x2, y2).
The number of BBoxes output per batch is determined by "actual_rois_num".
- actual_rois_num: A Tensor with shape [batch, 8], of type int32, specifying the number of BBoxes output per batch.

## Attributes

- feat_stride: A optional float32, specifying the stride of the sliding window.
Must be greater than "0".Defaults to "16".
- base_size: A optional float32, specifying the size of the generated base box.
Must be greater than "0". Defaults to "16".
- min_size: A optional float32, specifying the minimum edge length of a proposal.
A box with any edge less than this value is removed. Must be greater than "0". Defaults to "16".
- ratio: A optional list of floats, specifying the aspect ratio of the generated base box. Defaults to [0.5, 1, 2].
- scale: A optional list of floats, specifying the ratio of the size of the generated base box to "base_size".
Defaults to [8, 16, 32].
- pre_nms_topn: A required int, specifying top K boxes before NMS.
For float16 input, pre_nms_topn <= 6000. For float32 input, pre_nms_topn <= 3000. Defaults to "3000".
- post_nms_topn: A required int, specifying the number of boxes to be output after NMS.
The value is a multiple of 16. For float16 input, post_nms_topn <= 6000. For float32 input,
post_nms_topn <= 3000 (the maximum multiple of 16 is 2992 within the range). Defaults to "304".
- iou_threshold: A required float32, specifying the NMS threshold. The value range is (0,1]. Defaults to "0.7".
- output_actual_rois_num: An optional bool. Defaults to "false" .

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
