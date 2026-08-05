# CheckValid

```c
REG_OP(CheckValid)
    .INPUT(bbox_tensor, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(img_metas, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(valid_tensor, TensorType({DT_INT8}))
    .OP_END_FACTORY_REG(CheckValid)
```

## Brief

Judges whether the bounding box is valid. It is a customized
FasterRcnn operator .

## Inputs

Two inputs, including:
- bbox_tensor: Bounding box. A 2D Tensor of type float16 or float32 with shape (N, 4).
"N" indicates the number of bounding boxes, the value "4" indicates "x0",
"x1", "y0", and "y1".
- img_metas: Valid boundary value of the image. A 1D Tensor of type float16 or float32
with shape (16,) 

## Outputs

valid_tensor: A bool with shape (N, 1), specifying whether an input anchor is
in an image. "1" indicates valid, while "0" indicates invalid . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 bbox_tensor: float16,float32
- input1 img_metas: float16,float32
- output0 valid_tensor: bool,int8

## Attention Constraints

16 "img_metas" are input. The first three numbers (height, width, ratio) are
valid, specifying the valid boundary (heights x ratio, weights x ratio).


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
