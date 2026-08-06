# CheckNumerics

```c
REG_OP(CheckNumerics)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .REQUIRED_ATTR(message, String)
    .OP_END_FACTORY_REG(CheckNumerics)
```

## Brief

Checks a tensor for NaN and Inf values. 

## Inputs

x: A k-dimensional tensor. 

## Outputs

y: The output tensor. 

## Attributes

message: Prefix of the error message. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Attention Constraints

CheckNumerics runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator CheckNumerics.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
