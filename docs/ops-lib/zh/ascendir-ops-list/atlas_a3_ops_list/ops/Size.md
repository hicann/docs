# Size

```c
REG_OP(Size)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType({DT_INT32,DT_INT64}))
    .ATTR(dtype, Int, DT_INT32)
    .OP_END_FACTORY_REG(Size)
```

## Brief

Returns the size of a tensor, that is, an integer of the number of elements of the tensor. 

## Inputs

x: A tensor. Must be one of the following types: float32、float16、int8、
int16、uint16、uint8、int32、int64、uint32、uint64、bool、double、string. 

## Outputs

y: A tensor. The size of the input tensor. 

## Attributes

dtype: An optional int32 or int64. The output data type. Defaults to "int32". 

## Third-party framework compatibility

Compatible with the TensorFlow operator Size.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
