# SeluGrad

```c
REG_OP(SeluGrad)
    .INPUT(gradients, TensorType::RealNumberType())
    .INPUT(outputs, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(SeluGrad)
```

## Brief

Computes SeluGrad backprops: gradients * (outputs + scale * alpha)
   if outputs < 0, scale * gradients otherwise .

## Inputs

Two inputs, including:
- gradients: A Tensor of type RealNumberType .
- outputs: A Tensor of type RealNumberType .

## Outputs

y: A Tensor. Must have the same type as "gradients" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: float16,float32,int8,int32,uint8
- input1 outputs: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8

## Third-party framework compatibility

Compatible with the TensorFlow operator SeluGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
