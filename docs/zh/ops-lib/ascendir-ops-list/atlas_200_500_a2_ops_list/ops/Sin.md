# Sin

```c
REG_OP(Sin)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Sin)
```

## Brief

Computes sine of "x" element-wise.

## Inputs

One input: 
x: An ND Tensor that supports the data type UnaryDataType. 

## Outputs

y: An ND Tensor with the same dtype and shape of input "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow operator Sin.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
