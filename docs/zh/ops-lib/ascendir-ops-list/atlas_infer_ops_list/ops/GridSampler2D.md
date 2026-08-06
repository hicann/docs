# GridSampler2D

```c
REG_OP(GridSampler2D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(grid, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(interpolation_mode, String, "bilinear")
    .ATTR(padding_mode, String, "zeros")
    .ATTR(align_corners, Bool, false)
    .OP_END_FACTORY_REG(GridSampler2D)
```

## Brief

This operation samples input x by using interpolation based on flow
field grid, which is usually gennerated by affine_grid. The grid of shape
[N, H, W, 2] is the concatenation of (x, y) coordinates with shape [N, H, W]
each, where x is indexing the 4th dimension (in width dimension) of input
data x and y is indexng the 3rd dimention (in height dimension), finally
results is the interpolation value of 4 nearest corner points. The output
tensor shape will be [N, C, H, W].

## Inputs

- x: 4-D Tensor with shape `[batch, channels, height, width]`. Must be one
of the following types: float16, float, double.
- grid: flow field grid, 4-D Tensor with shape `[batch, height, width, 2]`
and has same dtype as `x`. 

## Outputs

y: Returns 4-D Tensor with the same dtype as `x`. 

## Attributes

- interpolation_mode: An optional string specifying the interpolation
method, either 'bilinear', 'nearest' and 'bicubic'. Defaults to
"bilinear".
- padding_mode: An optional string specifying the pad method, either
"zeros", "border", or "reflection". Defaults to "zeros".
- align_corners: An optional bool. If "true", the centers of the corner
pixels of the input and output tensors are aligned. Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- input1 grid: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with pytorch GridSampler2D operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
