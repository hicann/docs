# ShapeN

```c
REG_OP(ShapeN)
    .DYNAMIC_INPUT(x, TensorType::ALL())
    .DYNAMIC_OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(ShapeN)
```

## Brief

Returns shape of tensors. 

## Inputs

x: A list of input tensors. It's a dynamic input. 

## Outputs

y: A list of tensors with the same length as the input list of tensors.
It's a dynamic output. 

## Attributes

dtype: An optional int32 or int64. The output data type. Defaults to "int32". 

## Third-party framework compatibility

Compatible with the TensorFlow operator ShapeN.


---

[Back to Operator Specifications (Ascend950)](../README.md)
