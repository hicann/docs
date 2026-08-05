# NormalizeBBox

```c
REG_OP(NormalizeBBox)
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(shape_hw, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(reversed_box, Bool, false)
    .OP_END_FACTORY_REG(NormalizeBBox)
```

## Brief

Computes Normalize bbox function.

## Inputs

Inputs include:
- boxes: A Tensor. Must be float16 or float32.
- shape_hw: A Tensor. Must be int32.

## Outputs

y: A Tensor. Must have the same type and shape as boxes.

## Attributes

reversed_box: optional, bool. Defaults to "False"

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 boxes: float16,float32
- input1 shape_hw: int32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
