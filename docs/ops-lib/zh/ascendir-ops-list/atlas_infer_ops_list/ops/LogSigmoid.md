# LogSigmoid

```c
REG_OP(LogSigmoid)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(LogSigmoid)
```

## Brief

Calculate -ln(1+e^(-x)).

## Inputs

One inputs, including:
x: A tensor. Must be one of the following types:
      float16, float32, bfloat16. 

## Outputs

One outputs, including:
y: A tensor with the same type and shape of x's. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator LogSigmoid. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
