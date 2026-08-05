# IdentityN

```c
REG_OP(IdentityN)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .DYNAMIC_OUTPUT(y, TensorType::ALL())
    .OP_END_FACTORY_REG(IdentityN)
```

## Brief

Returns a list of tensors with the same shapes and contents as the input tensors. 

## Inputs

x: A list of input tensors. It's a dynamic input. Must be one of the following types:
float32、float16、int8、int16、uint16、uint8、int32、int64、uint32、uint64、bool、double、string.

## Outputs

y: A list of Tensor objects, with the same length、shape、data type and contents as the input tensor list.
It's a dynamic output. 

## Third-party framework compatibility

Compatible with the TensorFlow operator IdentityN.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
