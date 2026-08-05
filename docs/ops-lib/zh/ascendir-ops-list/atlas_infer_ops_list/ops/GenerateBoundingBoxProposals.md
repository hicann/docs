# GenerateBoundingBoxProposals

```c
REG_OP(GenerateBoundingBoxProposals)
    .INPUT(scores, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(bbox_deltas, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(image_info, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(anchors, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(nms_threshold, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(pre_nms_topn, TensorType({DT_INT32}))
    .INPUT(min_size, TensorType({DT_FLOAT}))
    .OUTPUT(rois, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(rois_probabilities, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(post_nms_topn, Int, 300)
    .OP_END_FACTORY_REG(GenerateBoundingBoxProposals)
```

## Brief

Select top 'pre_nms_topn' scoring boxes, decodes them with respect to anchors, applies non-maximal suppression
on overlapping boxes with higher than 'nms_threshold' intersection-over-union (IoU) value, discarding boxes where
shorter side is less than 'min_size'. 

## Inputs

scores: 4-D tensor with shape of [num_images, height, width, num_anchors], containing the scores of the boxes for
given anchors, can be unsorted. Must be one of the following types: float16, float32 . 
bbox_deltas: 4-D tensor with shape of [num_images, height, width, 4 * num_anchors], encoding boxes with respect to
each anchor. Coordinates are given in the form [dy, dx, dh, dw].
Must be one of the following types: float16, float32.. 
image_info: 2-D tensor with shape of [num_images, 5], containing image information Height, Width, Scale. Must be one
of the following types: float16, float32. 
anchors: 3-D tensor with shape of [height, width, 4 * num_anchors], describing the anchor boxes. Boxes are formatted
in the form [y1, x1, y2, x2]. Must be one of the following types: float16, float32. 
nms_threshold: A scalar of type float16 or float32, non-maximal suppression threshold. 
pre_nms_topn: A scalar of type int32, number of top scoring boxes to be used as input. 
min_size: A scalar of type float32, Any boxes that has a smaller size than min_size will be discarded. 

## Outputs

- rois: 3-D tensor with shape of [num_images, post_nms_topn, 4], padded by 0 if less than 'post_nms_topn'. Must be
one of the following types: float16, float32 . 
- rois_probabilities: 2-D tensor with shape of [num_images, post_nms_topn], probability of each roi in 'rois'
padded by 0 if needed, sorted by scores. Must be one of the following types: float16, float32. 

## Attributes

post_nms_topn: An optional int32. Maximum number of rois in the output. Defaults to be 300. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 scores: float16
- input1 bbox_deltas: float16
- input2 image_info: float16
- input3 anchors: float16
- input4 nms_threshold: float16
- input5 pre_nms_topn: int32
- input6 min_size: float32
- output0 rois: float16
- output1 rois_probabilities: float16

## Attention Constraints:+

Only supports 2864 input boxes at one time.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
