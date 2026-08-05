# Identity

```c
REG_OP(Identity)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .OP_END_FACTORY_REG(Identity)
```

## Brief

Return a tensor with the same shape and contents as input. 

## Inputs

x: A tensor. Must be one of the following types: float32、float16、int8、
int16、uint16、uint8、int32、int64、uint32、uint64、bool、double、string、bfloat16. 

## Outputs

y: A tensor with the same shape、data type and contents as input. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Identity.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
