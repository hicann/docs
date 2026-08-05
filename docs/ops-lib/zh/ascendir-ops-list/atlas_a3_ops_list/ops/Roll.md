# Roll

```c
REG_OP(Roll)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_UINT32, DT_INT8, DT_UINT8, DT_BF16, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_UINT32, DT_INT8, DT_UINT8, DT_BF16, DT_INT64}))
    .REQUIRED_ATTR(shifts, ListInt)
    .ATTR(dims, ListInt, {})
    .OP_END_FACTORY_REG(Roll)
```

## Brief

Roll the tensor along the given dimension(s).
Elements that are shifted beyond the last position are re-introduced at the first position.
If a dimension is not specified, the tensor will be flattened before rolling and then restored to the original shape.

## Inputs

One input, including:
x: A tensor. Must be one of the following types:
    float16, bfloat16, float32, int32, uint32, int8, uint8, int64. 

## Outputs

y: A Tensor with the same type and shape of x. 

## Attributes

- shifts: A required listInt. The number of places by which the elements of the tensor are shifted.
     The length of the array must be equal to dims, but if dims is empty, the array must be one-dimensional. 
- dims: An optional listInt. Defaults to "None". Axis along which to roll. The value of the range is [0, number of dimensions for input -1] or [-number of dimensions for self, -1].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int16,int32,int64,uint8,uint32
- output0 y: bfloat16,float16,float32,int8,int16,int32,int64,uint8,uint32

## Third-party framework compatibility

Compatible with the Pytorch operator Roll. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
