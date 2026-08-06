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

Slices the last dimension of a tensor from start to end with stride. 

## Inputs

x: A tensor of type float16, float32, double, int8, int16, int32, int64. 

## Outputs

y: A tensor with the same type as x. 

## Attributes

- start: Required. Start index of the last dimension.
- end: Required. End index of the last dimension.
- stride: Optional. Stride of slicing. Defaults to 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int16,int32
- output0 y: float16,float32,int16,int32

## Third-party framework compatibility

No compatibility


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
