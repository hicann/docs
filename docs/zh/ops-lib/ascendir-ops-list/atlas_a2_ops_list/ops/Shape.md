# Shape

```c
REG_OP(Shape)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64}))
    .ATTR(dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(Shape)
```

## Brief

Returns the shape of a tensor. 

## Inputs

x: A tensor. Must be one of the following types: float32、float16、int8、
int16、uint16、uint8、int32、int64、uint32、uint64、bool、double、string、bfloat16. 

## Outputs

y: A tensor. The shape of the input tensor. 

## Attributes

dtype: An optional int32 or int64. The output data type. Defaults to int32. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Size.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
