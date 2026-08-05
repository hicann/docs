# ArgMinWithValue

```c
REG_OP(ArgMinWithValue)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT64, DT_INT32}))
    .OUTPUT(indice, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT64, DT_INT32}))
    .REQUIRED_ATTR(dimension, Int)
    .ATTR(keep_dims, Bool, false)
    .ATTR(indice_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(ArgMinWithValue)
```

## Brief

Returns the minimum value of all elements in the input in the given
dimension.

## Inputs

One input: 
x: A multi-dimensional Tensor of type bfloat16 float16 or float32 or int64 or int32.
Supported format list ["ND"]. 

## Outputs

- indice: A multi-dimensional Tensor of type int32 or int64, specifying the index.
Supported format list ["ND"].
(If "keep_dims" is set to "false", the output dimensions are reduced by
"dimension" compared with that of "x". Otherwise, the output has one fewer
dimension than "x".)
- values: A ND Tensor, specifying the minimum value. Has the same dimensions
as "indice" and the same dtype as "x".
Supported format list ["ND"]. 

## Attributes

- dimension: An integer of type int32, specifying the axis information of
the index with the maximum value.
- keep_dims: A bool, specifying whether to keep dimensions for the output
Tensor. Defaults to "false".
- indice_dtype: A Type, The output type, either "int32" or "int64". Defaults to "int32".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 indice: int32
- output1 values: float16,float32

## Attention Constraints

- If there are multiple minimum values, the index of the first minimum
value is used.
- The value range of "dimension" is [-dims, dims - 1]. "dims" is the
dimension length of "x".
- Performing the ArgMinWithValue operation on the last axis of float32 data
is not supported on a mini platform. 

## Third-party framework compatibility

Compatible with the two output scenarios of PyTorch operator Min (the output
sequence is opposite to that of PyTorch).


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
