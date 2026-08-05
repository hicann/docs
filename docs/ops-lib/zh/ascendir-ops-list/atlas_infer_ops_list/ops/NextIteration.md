# NextIteration

```c
REG_OP(NextIteration)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32,
        DT_UINT64, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32,
        DT_UINT64, DT_BOOL}))
    .OP_END_FACTORY_REG(NextIteration)
```

## Brief

Makes the input available to the next iteration .

## Inputs

x: The tensor to be made available to the next iteration.
  Must be one of the following types: float16, float32, float64, int8,
  int16, int32, int64, uint8, uint16, uint32, uint64, bool . 

## Outputs

y: A Tensor. Has the same type as "x" . 

## Third-party framework compatibility

Compatible with the TensorFlow operator NextIteration.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
