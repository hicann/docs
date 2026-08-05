# Empty

```c
REG_OP(Empty)
    .INPUT(shape, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, DT_UINT8,
        DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_BF16, DT_STRING,
        DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(dtype, Int, DT_INT32)
    .ATTR(init, Bool, false)
    .OP_END_FACTORY_REG(Empty)
```

## Brief

Creates a tensor with the given "shape" and "dtype". 

## Inputs

shape: The shape of the output tensor. 

## Outputs

y: A tensor. 

## Attributes

- dtype: Optional. The data type of the output tensor. Defaults to "int32".
- init: An optional bool. If true, initializes the returned tensor with the default value of "dtype". Defaults to "false".

## Third-party framework compatibility

Compatible with the TensorFlow operator Empty.


---

[Back to Operator Specifications (Ascend950)](../README.md)
