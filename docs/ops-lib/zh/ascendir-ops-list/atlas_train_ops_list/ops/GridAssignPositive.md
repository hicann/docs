# GridAssignPositive

```c
REG_OP(GridAssignPositive)
    .INPUT(assigned_gt_inds, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(overlaps, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(box_responsible_flags, TensorType({ DT_UINT8 }))
    .INPUT(max_overlaps, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(argmax_overlaps, TensorType({ DT_INT32 }))
    .INPUT(gt_max_overlaps, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(gt_argmax_overlaps, TensorType({ DT_INT32 }))
    .INPUT(num_gts, TensorType({ DT_INT32 }))
    .OUTPUT(assigned_gt_inds_pos, TensorType({DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(pos_iou_thr, Float)
    .REQUIRED_ATTR(min_pos_iou, Float)
    .REQUIRED_ATTR(gt_max_assign_all, Bool)
    .OP_END_FACTORY_REG(GridAssignPositive)
```

## Brief

Performs Position Sensitive PS ROI Pooling Grad. 

## Inputs

- assigned_gt_inds: A tensor of type float16 or float32, shape (n, ).
 Indicates the assigned ground truth index for each predicted box.
- overlaps: A tensor. Datatype is same as assigned_gt_inds, IOU(Intersection over Union, between[0,1]) between gt_bboxes and bboxes, shape (k, n).
 Where k is the number of ground truths, n is the number of predicted boxes.
- box_responsible_flags: A tensor. Support uint8, shape (n, ).
 Flag to indicate whether the box is responsible for being assigned to a ground truth.
- max_overlaps: A tensor. Datatype is same as assigned_gt_inds, overlaps.max(axis=0), shape (n, ).
 Maximum IOU for each predicted box across all ground truths.
- argmax_overlaps: A tensor. Support int32, overlaps.argmax(axis=0), shape (n, ).
 Index of the ground truth with maximum IOU for each predicted box.
- gt_max_overlaps: A tensor. Datatype is same as assigned_gt_inds, overlaps.max(axis=1), shape (k, ).
 Maximum IOU for each ground truth across all predicted boxes.
- gt_argmax_overlaps: A tensor. Support int32, overlaps.argmax(axis=1), shape (k, ).
 Index of the predicted box with maximum IOU for each ground truth.
- num_gts: A tensor. Support int32, shape (1, ).
 Real number of ground truths 

## Outputs

assigned_gt_inds_pos: A tensor. Support float16/float32, shape (n, ).
  The final assigned ground truth indices for positive bboxes, used for gradient computation. 

## Attributes

- pos_iou_thr: float. IOU threshold for positive bboxes. Bboxes with IOU >= pos_iou_thr are considered positive.
- min_pos_iou: float. Minimum IOU for a bbox to be considered as a positive bbox.
- gt_max_assign_all: bool. Whether to assign all bboxes with the same highest overlap with some gt to that gt.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 assigned_gt_inds: float16,float32
- input1 overlaps: float16,float32
- input2 box_responsible_flags: uint8
- input3 max_overlaps: float16,float32
- input4 argmax_overlaps: int32
- input5 gt_max_overlaps: float16,float32
- input6 gt_argmax_overlaps: int32
- input7 num_gts: int32
- output0 assigned_gt_inds_pos: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
