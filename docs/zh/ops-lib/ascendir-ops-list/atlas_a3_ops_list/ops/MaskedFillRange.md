# MaskedFillRange

```c
REG_OP(MaskedFillRange)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32}))
    .INPUT(start, TensorType({DT_INT32}))
    .INPUT(end, TensorType({DT_INT32}))
    .INPUT(value, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32}))
    .REQUIRED_ATTR(axis, Int)
    .OP_END_FACTORY_REG(MaskedFillRange)
```

## Brief

masked fill tensor along with one axis by range.
boxes. It is a customized masked fill range operator . 

## Inputs

Four inputs, including:
- x: input tensor. A ND Tensor of float32/float16/int32/int8 with shapes
1-D (D,), 2-D(N, D), 3-D(N, C, D)
- start: masked fill start pos. A 2D Tensor of int32 with
shape (num, N). "num" indicates the number of loop masked fill, and the value N
indicates the batch of ND Tensor, if input x shape is 1-D, N = 1.
- end: masked fill end pos. A 2D Tensor of int32 with
shape (num, N). "num" indicates the number of loop masked fill, and the value N
indicates the batch of ND Tensor.
- value: masked fill value. A 1D Tensor of float32/float16/int32/int8 with
shape (num,). "num" indicates the number of loop masked fill. 

## Outputs

y: A ND Tensor of float32/float16/int32/int8 with shapes 1-D (D,), 2-D(N, D), 3-D(N, C, D)

## Attributes

- axis: axis with masked fill of int32. Defaults to -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32
- input1 start: int32
- input2 end: int32
- input3 value: float16,float32,int8,int32
- output0 y: float16,float32,int8,int32

## Attention Constraints

Warning: input shape's length must not be bigger than 1024 * 1024 * 1024.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
