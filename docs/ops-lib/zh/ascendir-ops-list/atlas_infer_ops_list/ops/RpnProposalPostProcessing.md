# RpnProposalPostProcessing

```c
REG_OP(RpnProposalPostProcessing)
    .INPUT(sorted_proposal, TensorType({DT_FLOAT16}))
    .INPUT(proposal_num, TensorType({DT_UINT32}))
    .OUTPUT(sorted_box, TensorType({ DT_FLOAT16}))
    .REQUIRED_ATTR(img_size, ListInt)
    .REQUIRED_ATTR(score_threshold, Float)
    .REQUIRED_ATTR(k, Int)
    .REQUIRED_ATTR(min_size, Float)
    .REQUIRED_ATTR(nms_threshold, Float)
    .REQUIRED_ATTR(post_nms_num, Int)
    .ATTR(box_filter, Bool, true)
    .ATTR(core_max_num, Int, 8)
    .OP_END_FACTORY_REG(RpnProposalPostProcessing)
```

## Brief

Computes Score Filte Pre-Sort function.

## Inputs

Inputs include:
- sorted_proposal: A Tensor. Must be float16.
                     N-D with shape [8*6002, 8].
- proposal_num: A Tensor. Must be uint32. N-D with shape [8, 8].

## Outputs

sorted_box: A Tensor. Must be float16. N-D with shape [N, 1].

## Attributes

- min_size: required, float, threahold of nms process.
- score_threshold: required, float, threahold of topk process.
- k: required, Int, threahold of topk process.
- min_size: required, float, threahold of nms process.
- nms_threshold: required, float, threahold of nms process.
- post_nms_num: required, float, threahold of nms process.
- box_filter: bool, mark of box_filter. Defaults to "true"
- core_max_num: int, max number of core. Defaults to "8"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 sorted_proposal: float16
- input1 proposal_num: uint32
- output0 sorted_box: float16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
