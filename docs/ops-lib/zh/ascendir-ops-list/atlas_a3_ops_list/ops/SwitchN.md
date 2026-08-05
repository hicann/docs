# SwitchN

```c
REG_OP(SwitchN)
    .INPUT(data, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32,
        DT_UINT64, DT_BOOL}))
    .INPUT(pred_value, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(output, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
        DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32,
        DT_UINT64, DT_BOOL}))
    .OP_END_FACTORY_REG(SwitchN)
```

## Brief

Forwards "data" to the output port determined by "pred_value" .

## Inputs

- data: The tensor to be forwarded.
         Must be one of the following types: float16, float32, float64,
         int8, int16, int32, int64, uint8, uint16, uint32, uint64, bool.
- pred_value: An int64 tensor which determines the output port that will receive data .

## Outputs

output: The output tensors, one of which will become available.
       Has the same type as "data". It's a dynamic output.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
