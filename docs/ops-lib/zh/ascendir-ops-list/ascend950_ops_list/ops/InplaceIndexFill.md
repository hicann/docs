# InplaceIndexFill

```c
REG_OP(InplaceIndexFill)
    .INPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BF16,
                          DT_INT8, DT_UINT8, DT_INT16, DT_INT32,
                          DT_INT64, DT_BOOL}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(value, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BF16,
                              DT_INT8, DT_UINT8, DT_INT16, DT_INT32,
                              DT_INT64, DT_BOOL}))
    .OUTPUT(x, TensorType({DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BF16,
                           DT_INT8, DT_UINT8, DT_INT16, DT_INT32,
                           DT_INT64, DT_BOOL}))
    .REQUIRED_ATTR(dim, Int)
    .OP_END_FACTORY_REG(InplaceIndexFill)
```

## Brief

Fills the elements of the input tensor `x` with `value` by selecting the
  indices in the order given in `indices` along the specified dimension `dim`.
  The operation is performed in-place. 

## Inputs

Three inputs, including:
- x: A Tensor. The input tensor to be filled. Its type must be one of
  the flowing types: DT_FLOAT, DT_DOUBLE, DT_FLOAT16, DT_BF16,
  DT_INT8, DT_UINT8, DT_INT16, DT_INT32, DT_INT64, DT_BOOL.
- indices: A Tensor. The indices of the input tensor to fill. Its type should be
  int32 or int64. The indices should be 1-dimensional.
- value: A Tensor. The value to fill into the input tensor. Must have the same
  data type as "x". 

## Outputs

x: A Tensor. Same as input "x", updated in-place.

## Attributes

- dim: A required int. Specifies the dimension along which to index and fill.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- input1 indices: int32,int64
- input2 value: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8


---

[Back to Operator Specifications (Ascend950)](../README.md)
