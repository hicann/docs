# ToAbsoluteBBox

```c
REG_OP(ToAbsoluteBBox)
    .INPUT(normalized_boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(shape_hw, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(reversed_box, Bool, false)
    .OP_END_FACTORY_REG(ToAbsoluteBBox)
```

## Brief

To absolute the bounding box .

## Inputs

- normalized_boxes: A 3D Tensor of type float16 or float32. Must be the format "ND".
- shape_hw: A 1D Tensor of type int32. Must be the format "ND".

## Outputs

y: A Tensor. Has the same type and shape as "normalized_boxes" . 

## Attributes

reversed_box: An optional bool, specifying the last two dims is "4,num" or
"num,4", "true" for "4,num", "false" for "num,4". Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 normalized_boxes: float16,float32
- input1 shape_hw: int32
- output0 y: float16,float32

## Attention Constraints

"normalized_boxes"'s shape must be (batch,num,4) or (batch,4,num).
"shape_hw"'s shape must be (4,)


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
