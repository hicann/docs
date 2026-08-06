# LUT3D

```c
REG_OP(LUT3D)
    .INPUT(img, TensorType({DT_UINT8, DT_FLOAT}))
    .INPUT(lut_table, TensorType({DT_UINT8, DT_FLOAT}))
    .OUTPUT(lut_img, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(LUT3D)
```

## Brief

LUT3D
Find the corresponding optimal pixel value for the pixel values in the input img. 

## Inputs

Two inputs, including:
- img: A 3D or 4D Tensor of type uint8 or float32, with shape [H,W,C] or [N,H,W,C] respectively.
The format of the tensor is ND. The range of values for elements within the tensor is [0, 255].
- lut_table: A 4D Tensor of the same type as "img", with shape [lut_table_n, lut_table_n, lut_table_n, 3].
The format of the tensor is ND. The value of lut_table_n is limited to 17. 

## Outputs

lut_img: A 3D or 4D Tensor of type uint8 or float32. Has the same shape as "img" .
The format of the tensor is ND. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 img: float32,uint8
- input1 lut_table: float32,uint8
- output0 lut_img: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
