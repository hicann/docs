# GridSampler2DGrad

```c
REG_OP(GridSampler2DGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(grid, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OUTPUT(dgrid, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(interpolation_mode, String, "bilinear")
    .ATTR(padding_mode, String, "zeros")
    .ATTR(align_corners, Bool, false)
    .OP_END_FACTORY_REG(GridSampler2DGrad)
```

## Brief

Computes the gradients of GridSampler2D.

## Inputs

- grad: A 4-D tensor with shape `[batch, out_height, out_width, channels]`.
The gradient of the output of the previous layer during backpropagation.
Must be one of the following types: `[float16, float32, bfloat16, double]`.
The format must be NHWC.
- x: A 4-D tensor with shape `[batch, height, width, channels]`.
Input tensor representing backpropagation.
Must be one of the following types: `[float16, float32, bfloat16, double]`.
The format must be NHWC.
- grid: Flow field grid, 4-D tensor with shape `[batch, out_height, out_width, 2]`. Must be one of the following types:
`[float16, float32, bfloat16, double]`.
The format must be ND.

## Outputs

- dx: Indicates the output gradient of backpropagation. Returns 4-D tensor with the same dtype, format and shape as `x`.
- dgrid: Indicates the grid gradient. Returns 4-D tensor with the same dtype, format and shape as `grid`.

## Attributes

- interpolation_mode: An optional string specifying the interpolation method.
'bilinear' and 'nearest' are supported now. Defaults to "bilinear".
- padding_mode: An optional string specifying the pad method, either "zeros" or "border".
Defaults to "zeros".
- align_corners: An optional bool. Indicates the mapping mode between the coordinates of the feature map and the feature value.
If "true", the centers of the corner pixels of the input and output tensors are aligned. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 grid: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32
- output1 dgrid: bfloat16,float16,float32
### AI CPU
- input0 grad: double,float16,float32
- input1 x: double,float16,float32
- input2 grid: double,float16,float32
- output0 dx: double,float16,float32
- output1 dgrid: double,float16,float32

## Third-party framework compatibility

Compatible with pytorch GridSampler2DGrad operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
