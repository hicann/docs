# RefSwitch

```c
REG_OP(RefSwitch)
    .INPUT(data, TensorType::ALL())
    .INPUT(pred, TensorType({DT_BOOL}))
    .OUTPUT(output_false, TensorType::ALL())
    .OUTPUT(output_true, TensorType::ALL())
    .OP_END_FACTORY_REG(RefSwitch)
```

## Brief

Forwards "data" to the output port determined by "pred".
      If "pred" is "true", the data input is forwarded to "output_true".
      Otherwise, the data is forwarded to "output_false" .

## Inputs

- data: The ref tensor to be forwarded.
         Must be one of the following types: float16, float32, float64,
         int8, int16, int32, int64, uint8, uint16, uint32, uint64, bool, string.
- pred: A boolean scalar. The output port that will receive data .

## Outputs

- output_false: If "pred" is "false", data will be forwarded to this output.
                 Has the same type as "data".
- output_true: If "pred" is "true", data will be forwarded to this output.
                Has the same type as "data" . 
@see Merge() | Switch()

## Third-party framework compatibility

Compatible with the TensorFlow operator RefSwitch.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
