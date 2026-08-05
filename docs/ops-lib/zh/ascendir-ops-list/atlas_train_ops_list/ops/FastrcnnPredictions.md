# FastrcnnPredictions

```c
REG_OP(FastrcnnPredictions)
    .INPUT(rois, TensorType({DT_FLOAT16}))
    .INPUT(score, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(nms_threshold, Float)
    .REQUIRED_ATTR(score_threshold, Float)
    .REQUIRED_ATTR(k, Int)
    .OUTPUT(sorted_rois, TensorType({DT_FLOAT16}))
    .OUTPUT(sorted_scores, TensorType({DT_FLOAT16}))
    .OUTPUT(sorted_classes, TensorType({DT_FLOAT16}))
    .OP_END_FACTORY_REG(FastrcnnPredictions)
```

## Brief

Computes Fastrcnn Predictions function.

## Inputs

Inputs include:
- rois: A Tensor. Must be float16. N-D with shape [N*C, 4].
- score: A Tensor. Must be float16. N-D with shape [N, C+1].

## Outputs

- sorted_rois: A Tensor. Must be float16. N-D with shape [N, 4].
- sorted_scores: A Tensor. Must be float16. N-D with shape [N, 1].
- sorted_classes: A Tensor. Must be float16. N-D with shape [N, 1].

## Attributes

- nms_threshold: required, float, threahold of nms process.
- score_threshold: required, float, threahold of topk process.
- k: required, Int, threahold of topk process.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 rois: float16
- input1 score: float16
- output0 sorted_rois: float16
- output1 sorted_scores: float16
- output2 sorted_classes: float16


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
