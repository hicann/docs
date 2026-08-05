# StringToNumber

```c
REG_OP(StringToNumber)
    .INPUT(x, TensorType({DT_STRING}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64}))
    .ATTR(out_type, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(StringToNumber)
```

## Brief

Converts each string in the input Tensor to the specified numeric type . 

## Inputs

Inputs include:
x: A Tensor. Must be one of the following types: string. 

## Outputs

y: A Tensor. Must be one of the following types: float, double, int32, int64. 

## Attributes

out_type: The numeric type to interpret each string in string_tensor as. Defaults to float. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: string
- output0 y: double,float32,int32,int64

## Attention Constraints

The implementation for StringToNumber on Ascend uses AICPU, with bad performance. 

## Third-party framework compatibility

- compatible with tensorflow StringToNumber operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
