# AxpyV2

```c
REG_OP(AxpyV2)
    .INPUT(x1, "T1")
    .INPUT(x2, "T2")
    .INPUT(alpha, "T3")
    .OUTPUT(y, "T4")
    .DATATYPE(T1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16, DT_INT64, DT_UINT8, DT_INT8, DT_BOOL}))
    .DATATYPE(T2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16, DT_INT64, DT_UINT8, DT_INT8, DT_BOOL}))
    .DATATYPE(T3, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_BF16, DT_INT64, DT_UINT8, DT_INT8, DT_BOOL}))
    .DATATYPE(T4, Promote({"T1", "T2", "T3"}))
    .OP_END_FACTORY_REG(AxpyV2)
```

## Brief

Computes the result of x2 * alpha + x1.

## Inputs

- x1: An ND tensor of type float16, bfloat16, float32, int32, int64, uint8, int8, bool.
- x2: An ND tensor of type float16, bfloat16, float32, int32, int64, uint8, int8, bool.
The shapes of "x1", "x2" must comply with the broadcast rule.
- alpha: A scalar tensor of type float16, bfloat16, float32, int32, int64, uint8, int8, bool. Shape must be [1].

## Outputs

y: An ND tensor with type is after 'x1', 'x2' and 'alpha' type promotion,
whose shape is generated after 'x1', 'x2' broadcast opratioan. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- input2 alpha: float16,float32,int32
- output0 y: float16,float32,int32

## Third-party framework compatibility

Compatible with the PyTorch operator Axpy.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
