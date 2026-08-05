# TransArgb

```c
REG_OP(TransArgb)
    .INPUT(x, "T1")
    .OUTPUT(y, "T2")
    .DATATYPE(T1, TensorType({DT_FLOAT16}))
    .DATATYPE(T2, TensorType({DT_INT16}))
    .OP_END_FACTORY_REG(TransArgb)
```

## Brief

HDRNet and ISP direct data conversion
returned tensor's dimension will correspond to input dimension [0, 3, 4, 2, 1],
convert tensor dtype float16 to int16 . 

## Inputs

one inputs, including:
- x: A Tensor. Must be one of the following types: float16.

## Outputs

y: A Tensor. Must be one of the following types: int16. 

## Third-party framework compatibility

only for use by corresponding operators in HDRnet networks


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
