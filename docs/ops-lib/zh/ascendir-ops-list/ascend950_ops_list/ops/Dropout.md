# Dropout

```c
REG_OP(Dropout)
    .INPUT(x, TensorType{DT_FLOAT})
    .OUTPUT(y, TensorType{DT_FLOAT})
    .ATTR(dropout_ratio, Float, 0.5)
    .ATTR(scale_train, Bool, true)
    .ATTR(alpha, Float, 1.0)
    .ATTR(beta, Float, 0.0)
    .OP_END_FACTORY_REG(Dropout)
```

## Brief

The dropout operator randomly sets (according to the given dropout probability)
the outputs of some units to zero, while others are remain unchanged. . 

## Inputs

One input, including:
- x:The input tensor variable. The data type is float32.

## Outputs

y: A Variable holding Tensor representing the dropout, has same shape and data type with x. 

## Attributes

- dropout_ratio:Float between 0 and 1. Fraction of the input units to drop.Defaults to "0.5".
- scale_train: Bool,default to true.
- alpha: An optional float32. A scaling factor. Defaults to "1.0".
- beta: An optional float32. An exponent. Defaults to "0.0".


---

[Back to Operator Specifications (Ascend950)](../README.md)
