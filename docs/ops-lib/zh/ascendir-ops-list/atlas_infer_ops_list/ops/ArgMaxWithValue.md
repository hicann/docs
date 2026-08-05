# ArgMaxWithValue

```c
REG_OP(ArgMaxWithValue)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT64, DT_INT32}))
    .OUTPUT(indice, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT64, DT_INT32}))
    .REQUIRED_ATTR(dimension, Int)
    .ATTR(keep_dims, Bool, false)
    .ATTR(indice_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(ArgMaxWithValue)
```

## Brief

Returns the maximum value of all elements in the input in the given
dimension.

## Inputs

One input:
x: A multi-dimensional tensor of type bfloat16, float16, float32, int64, int32. 

## Outputs

- indice: A multi-dimensional tensor of type int32 or int64, specifying the index.
(If "keep_dims" is set to "false", the output dimensions are reduced by
"dimension" compared with that of "x". Otherwise, the output keeps the dimensions, but
the length of corresponding dimension will be set to "1".)
- values: A ND tensor, specifying the maximum value. Has the same dimensions
as "indice" and the same dtype as "x". 

## Attributes

- dimension: An integer of type int32, specifying the axis information of
the index with the maximum value. Required and no default value.
- keep_dims: A bool, specifying whether to keep dimensions for the output
tensor. Optional and defaults to "false".
- indice_dtype: A Type, The output type, either "int32" or "int64". Defaults to "int32".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 indice: int32
- output1 values: float16,float32

## Attention Constraints

- If there are multiple maximum values, the index of the first maximum
value is used.
- The value range of "dimension" is [-dims, dims - 1]. "dims" is the
dimension length of "x". 

## Third-party framework compatibility

Compatible with the two output scenarios of PyTorch operator Max (the output
sequence is opposite to that of PyTorch).


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
