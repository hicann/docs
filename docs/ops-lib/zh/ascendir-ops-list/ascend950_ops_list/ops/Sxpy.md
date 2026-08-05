# Sxpy

```c
REG_OP(Sxpy)
    .INPUT(x1, "T1")
    .INPUT(x2, "T2")
    .OPTIONAL_INPUT(alpha, "T3")
    .OUTPUT(y, "T4")
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8,
                              DT_UINT16, DT_INT16, DT_INT32, DT_INT64,
                              DT_COMPLEX64, DT_COMPLEX128, DT_BF16, DT_COMPLEX32}))
    .DATATYPE(T2, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8,
                              DT_UINT16, DT_INT16, DT_INT32, DT_INT64,
                              DT_COMPLEX64, DT_COMPLEX128, DT_BF16, DT_COMPLEX32}))
    .DATATYPE(T3, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8,
                              DT_UINT16, DT_INT16, DT_INT32, DT_INT64,
                              DT_COMPLEX64, DT_COMPLEX128, DT_BF16, DT_COMPLEX32}))
    .DATATYPE(T4, Promote({"T1", "T2", "T3"}))
    .OP_END_FACTORY_REG(Sxpy)
```

## Brief

Computes the result of x1 - x2 * alpha. x1/x2 Support broadcasting operations.

## Inputs

- x1: An ND tensor of type float16, bfloat16, float32, double, uint8, int8, uint16,
 int16, int32, int64, complex32, complex64, complex128.
- x2: An ND tensor of type float16, bfloat16, float32, double, uint8, int8, uint16,
 int16, int32, int64, complex32, complex64, complex128.
- alpha: A optional tensor of type float16, bfloat16, float32, double, uint8, int8, uint16,
 int16, int32, int64, complex32, complex64, complex128. shape is [1] or [].

## Outputs

y: An ND tensor tensor with the same shape and type as "x1". 

## Third-party framework compatibility

Warning: THIS FUNCTION IS EXPERIMENTAL. Please do not use.


---

[Back to Operator Specifications (Ascend950)](../README.md)
