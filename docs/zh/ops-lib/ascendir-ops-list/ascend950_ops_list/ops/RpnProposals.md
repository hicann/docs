# RpnProposals

```c
REG_OP(RpnProposals)
    .INPUT(rois, TensorType({DT_FLOAT16}))
    .INPUT(cls_bg_prob, TensorType({DT_FLOAT16}))
    .INPUT(img_size, TensorType({DT_INT32}))
    .REQUIRED_ATTR(score_threshold, Float)
    .REQUIRED_ATTR(k, Int)
    .REQUIRED_ATTR(min_size, Float)
    .REQUIRED_ATTR(nms_threshold, Float)
    .REQUIRED_ATTR(post_nms_num, Int)
    .ATTR(score_filter, Bool, true)
    .ATTR(box_filter, Bool, true)
    .ATTR(score_sigmoid, Bool, false)
    .OUTPUT(sorted_box, TensorType({DT_FLOAT16}))
    .OP_END_FACTORY_REG(RpnProposals)
```

## Brief

Computes Fastrcnn RpnProposals function . 

## Inputs

Inputs include:
- rois: A Tensor. Must be float16. N-D with shape [N, 4].
- cls_bg_prob: A Tensor. Must be float16. N-D with shape [N, 1].
- img_size: A Tensor. Must be int32. shape [H, W] .

## Outputs

- sorted_rois: A Tensor. Must be float16. N-D with shape [N, 4].
- sorted_scores: A Tensor. Must be float16. N-D with shape [N, 1].
- sorted_classes: A Tensor. Must be float16. N-D with shape [N, 1] .

## Attributes

- score_threshold: required, float, threahold of topk process.
- k: required, Int, threahold of topk process.
- min_size: required, float, threahold of nms process.
- nms_threshold: required, float, threahold of nms process.
- post_nms_num: required, float, threahold of nms process.
- score_filter: bool, mark of score_filter. Defaults to "true"
- box_filter: bool, mark of box_filter. Defaults to "true"
- score_sigmoid: bool, mark of score_sigmoid. Defaults to "false"

## Third-party framework compatibility

Compatible with the TensorFlow operator Unpack.


---

[Back to Operator Specifications (Ascend950)](../README.md)
