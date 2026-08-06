# YUVToRGB

```c
REG_OP(YUVToRGB)
    .INPUT(x, TensorType({DT_UINT8}))
    .OPTIONAL_INPUT(matrix, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_UINT8}))
    .ATTR(matrix_type, Int, 0)
    .ATTR(rb_swap, Int, 0)
    .OP_END_FACTORY_REG(YUVToRGB)
```

## Brief

YUVToRGB

## Inputs

- x: A 4-D uint8 Tensor.
       Must set the format, supported format list ["NYUV"].
- matrix: A 1-D float tensor of 2x3x3 elements

## Outputs

- y: A 4-D uint8 Tensor.
       Must set the format, supported format list ["NCHW, NHWC"].

## Attributes

- matrix_type: An Int attr, Defaults to 0.
                 support list [ 0: CSC_MATRIX_BT601_WIDE,
                                1: CSC_MATRIX_BT601_NARROW,
                                2: CSC_MATRIX_BT709_WIDE,
                                3: CSC_MATRIX_BT709_NARROW,
                                4: CSC_MATRIX_BT2020_WIDE,
                                5: CSC_MATRIX_BT2020_NARROW,
                                6: CSC_MATRIX_USR_DEFINE ]
- rb_swap: An Int attr, Defaults to 0.
             support list [ 0: RGB, 1: BGR ]

## Attention Constraints

- Only support in dvpp


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
