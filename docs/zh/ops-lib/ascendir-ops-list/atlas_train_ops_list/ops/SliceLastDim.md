# SliceLastDim

```c
REG_OP(SliceLastDim)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT16, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT16, DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(start, Int)
    .REQUIRED_ATTR(end, Int)
    .ATTR(stride, Int, 1)
    .OP_END_FACTORY_REG(SliceLastDim)
```

## Brief

Slice a tensor at its last dim, e.x. a[..., begin:end:stride].

## Inputs

One input, including:
x: A ND Tensor, Support 1D ~ 8D.
Type must be one of the following types: float16, float32, double, int8, int16, int32, int64.

## Outputs

y: A Tensor. Has the same type as "x". 

## Attributes

- start: An attribute of type Int, start index of last dim.
- end: An attribute of type Int, end index of last dim.
- stride: An attribute of type Int, stride of slice, default to 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int16,int32
- output0 y: float16,float32,int16,int32

## Third-party framework compatibility

No compatibility


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
