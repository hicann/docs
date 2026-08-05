# NMSWithMask

```c
REG_OP(NMSWithMask)
    .INPUT(box_scores, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(selected_boxes, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(selected_idx, TensorType({DT_INT32}))
    .OUTPUT(selected_mask, TensorType({DT_UINT8}))
    .ATTR(iou_threshold, Float, 0.5)
    .OP_END_FACTORY_REG(NMSWithMask)
```

## Brief

Iteratively removes lower scoring boxes which have an IoU greater than
iou_threshold with higher scoring box according to their
intersection-over-union (IoU) . 

## Inputs

box_scores: 2-D tensor with shape of [N, 8], including proposal boxes and
corresponding confidence scores . Support dtype: [float16, float32, bfloat16], Support format: [ND]. 

## Outputs

- selected_boxes: 2-D tensor with shape of [N,5], representing filtered
boxes including proposal boxes and corresponding confidence scores.
Support dtype: [float16, float32, bfloat16], Support format: [ND]. 
- selected_idx: 1-D tensor with shape of [N], representing the index of
input proposal boxes. Support dtype: [int32], Support format: [ND]. 
- selected_mask: 1-D tensor with shape of [N], the symbol judging whether
the output proposal boxes is valid . Support dtype: [uint8,bool], Support format: [ND]. 

## Attributes

iou_threshold: An optional float. The threshold for deciding whether boxes
overlap too much with respect to IOU . Default value is 0.5 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 box_scores: bfloat16,float16,float32
- output0 selected_boxes: bfloat16,float16,float32
- output1 selected_idx: int32
- output2 selected_mask: bool,uint8

## Attention Constraints

The 2nd-dim of input box_scores must be equal to 8.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
