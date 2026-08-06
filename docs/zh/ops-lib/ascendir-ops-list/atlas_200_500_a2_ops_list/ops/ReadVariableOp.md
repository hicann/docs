# ReadVariableOp

```c
REG_OP(ReadVariableOp)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(ReadVariableOp)
```

## Brief

Reads and returns the value of the input variable tensor. 

## Inputs

x: A tensor must have numeric type. 

## Outputs

y: A tensor must have numeric type. 

## Attributes

dtype: Same as the input data type. The output data type. Defaults to int32. 

## Third-party framework compatibility

Compatible with the TensorFlow operator ReadVariableOp.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
