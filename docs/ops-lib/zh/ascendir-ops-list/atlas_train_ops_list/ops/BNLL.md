# BNLL

```c
REG_OP(BNLL)
    .INPUT(x, TensorType::FloatingDataType())
    .OUTPUT(y, TensorType::FloatingDataType())
    .OP_END_FACTORY_REG(BNLL)
```

## Brief

Computes the binomial normal log likelihood (BNLL) output:
if x>0, x+log(1+exp(-x)); otherwise log(1+exp(x)).

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:
double, float16, float32.

## Outputs

y: A tensor. Has the same type and format as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Caffe operator BNLL.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
