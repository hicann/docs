# OptionalGetValue

```c
REG_OP(OptionalGetValue)
  .INPUT(optional, TensorType({DT_VARIANT}))
  .DYNAMIC_OUTPUT(components, TensorType::BasicType())
  .REQUIRED_ATTR(output_types, ListType)
  .REQUIRED_ATTR(output_shapes, ListListInt)
  .OP_END_FACTORY_REG(OptionalGetValue)
```

## Brief

OptionalGetValue

## Inputs

optional: A tensor of type variant.

## Outputs

components: A list of Tensor objects of output_types. Must be one of the types:
complex128, complex64, double, float32, float16, int16, int32, int64, int8, qint16,
qint32, qint8, quint16, quint8, quint16, uint32, uint64, uint8, bfloat16, complex32.

## Attributes

output_types: A type list that indicates types of all outputs.
output_shapes: A int list list that indicates shapes of all outputs.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 optional: variant
- output0 components: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
