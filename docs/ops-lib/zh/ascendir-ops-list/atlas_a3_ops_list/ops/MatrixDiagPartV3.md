# MatrixDiagPartV3

```c
REG_OP(MatrixDiagPartV3)
    .INPUT(x, TensorType::BasicType())
    .INPUT(k, TensorType({DT_INT32}))
    .INPUT(padding_value, TensorType::BasicType())
    .OUTPUT(y, TensorType::BasicType())
    .ATTR(align,String ,"RIGHT_LEFT")
    .OP_END_FACTORY_REG(MatrixDiagPartV3)
```

## Brief

Returns the batched diagonal part of a batched tensor. 

## Inputs

- x: A Tensor. Rank r tensor where r >= 2.
- k: A Tensor of type int32. Diagonal offset(s). Positive value means superdiagonal,
0 refers to the main diagonal, and negative value means subdiagonals. k can be a
single integer (for a single diagonal) or a pair of integers specifying the low and
high ends of a matrix band. k[0] must not be larger than k[1].
- padding_value:A Tensor. Must have the same type as input. The value to fill the area
outside the specified diagonal band with. 

## Outputs

- y: A Tensor. Has the same type as "input".

## Attributes

- align:An optional string from: "LEFT_RIGHT", "RIGHT_LEFT", "LEFT_LEFT", "RIGHT_RIGHT". Defaults to "RIGHT_LEFT".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 k: int32
- input2 padding_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the Tensorflow  operator FillDiagonal.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
