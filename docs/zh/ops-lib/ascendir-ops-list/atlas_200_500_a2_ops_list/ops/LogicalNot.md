# LogicalNot

```c
REG_OP(LogicalNot)
    .INPUT(x, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(LogicalNot)
```

## Brief

Returns the truth value of NOT "x" element-wise.

## Inputs

x: A ND Tensor of type bool. 

## Outputs

y: A ND Tensor of type bool. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool
- output0 y: bool
### AI CPU
- input0 x: bool
- output0 y: bool

## Attention Constraints

The input and output values are "1" or "0", corresponding to bool values "true" and "false". 

## Third-party framework compatibility

Compatible with the TensorFlow operator logical_not.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
