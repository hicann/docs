# Cummax

```c
REG_OP(Cummax)
    .INPUT(x, TensorType({TensorType::BasicType(), DT_BF16}))
    .OUTPUT(y, TensorType({TensorType::BasicType(), DT_BF16}))
    .OUTPUT(indices, TensorType::BasicType())
    .REQUIRED_ATTR(dim, Int)
    .OP_END_FACTORY_REG(Cummax)
```

## Brief

Returns a namedtuple (values, indices) where values is the cumulative
the cumulative maximum of elements of input in the dimension dim.
And indices is the index location of each maximum value found in the dimension dim. 

## Inputs

One inputs, including:
x: A tensor . Must be one of the following types:
    float16, float32, int32, uint32, int8, uint8, bfloat16. 

## Outputs

- y: A Tensor with the same type and shape of x's.
- indices: A Tensor with the int32/int64 type and the same shape of x's.

## Attributes

dim: Axis along which to cummax. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 indices: int32,int64

## Third-party framework compatibility

Compatible with the Pytorch operator Cummax. 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
