# Snapshot

```c
REG_OP(Snapshot)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
        DT_UINT8, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_STRING}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16, \
        DT_UINT8, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_STRING}))
    .OP_END_FACTORY_REG(Snapshot)
```

## Brief

Returns a copy of the input tensor. 

## Inputs

x: A tensor. 

## Outputs

y: A copy of input tensor. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Snapshot.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
