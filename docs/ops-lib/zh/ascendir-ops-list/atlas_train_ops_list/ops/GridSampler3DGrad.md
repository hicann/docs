# GridSampler3DGrad

```c
REG_OP(GridSampler3DGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(grid, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(dgrid, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(interpolation_mode, String, "bilinear")
    .ATTR(padding_mode, String, "zeros")
    .ATTR(align_corners, Bool, false)
    .OP_END_FACTORY_REG(GridSampler3DGrad)
```

## Brief

Computes the gradients of GridSampler3D.

## Inputs

- grad: 5-D Tensor with shape `[batch, channels, depth, height, width]`.
- x: 5-D Tensor with shape `[batch, channels, depth, height, width]`.
- grid: flow field grid, 5-D Tensor with shape `[batch, depth, height, width, 3]`.

## Outputs

dx: Returns 5-D Tensor with the same dtype and shape as `x`.
dgrid: Returns 5-D Tensor with the same dtype and shape as `grid`.

## Attributes

- interpolation_mode: An optional string specifying the interpolation method.
- padding_mode: An optional string specifying the pad method.
- align_corners: An optional bool. If "true", the centers of the corner
pixels of the input and output tensors are aligned. Defaults to "false" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grad: double,float16,float32
- input1 x: double,float16,float32
- input2 grid: double,float16,float32
- output0 dx: double,float16,float32
- output1 dgrid: double,float16,float32

## Third-party framework compatibility

Compatible with pytorch GridSampler3DGrad operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
