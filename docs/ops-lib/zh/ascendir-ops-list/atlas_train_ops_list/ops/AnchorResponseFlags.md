# AnchorResponseFlags

```c
REG_OP(AnchorResponseFlags)
    .INPUT(gt_bboxes, TensorType({DT_FLOAT}))
    .OUTPUT(flags, TensorType({DT_UINT8}))
    .REQUIRED_ATTR(featmap_size, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(num_base_anchors, Int)
    .OP_END_FACTORY_REG(AnchorResponseFlags)
```

## Brief

Generate the responsible flags of anchor in a single feature map.

## Inputs

gt_bboxes: Ground truth box, 2-D Tensor of type float32 with shape `[batch, 4]`.

## Outputs

flags: The valid flags of each anchor in a single level, 1-D Tensor of type uint8.

## Attributes

- featmap_size: The size of feature maps. It is a listint and size is 2.
- strides: Stride of current level, listint.
- num_base_anchors: The number of base anchors.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gt_bboxes: float32
- output0 flags: uint8


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
