# DecodeBboxV2

```c
REG_OP(DecodeBboxV2)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(anchors, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(scales, ListFloat, {1.0, 1.0, 1.0, 1.0})
    .ATTR(decode_clip, Float, 0.0)
    .ATTR(reversed_box, Bool, false)
    .OP_END_FACTORY_REG(DecodeBboxV2)
```

## Brief

Computes decode bboxv2 function.

## Inputs

Inputs include:
- boxes: A Tensor. Must be float16 or float32. Supported format list ["ND"].
- anchors: A Tensor. Must be float16 or float32. Supported format list ["ND"].

## Outputs

y: A Tensor. Must have the same type as box_predictions. Supported format list ["ND"].

## Attributes

- scales: optional, listfloat. Default value is [1.0,1.0,1.0,1.0].
- decode_clip: optional, float, threahold of decode process. Default value is 0.0
- reversed_boxes: optional, bool. Default value is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float16
- input1 anchors: float16
- output0 y: float16


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
