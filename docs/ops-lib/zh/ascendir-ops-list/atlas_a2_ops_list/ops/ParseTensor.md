# ParseTensor

```c
REG_OP(ParseTensor)
    .INPUT(serialized, TensorType({DT_STRING}))
    .OUTPUT(output, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
                          DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_UINT32,
                          DT_UINT64, DT_BOOL, DT_DOUBLE, DT_STRING,
                          DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(out_type, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(ParseTensor)
```

## Brief

Convert serialized tensorflow.TensorProto prototype to Tensor. 

## Inputs

serialized: A Tensor of string type. Scalar string containing serialized
TensorProto prototype. 

## Outputs

output: A Tensor of type out_type. 

## Attributes

out_type: The type of the serialized tensor. The provided type must match the
type of the serialized tensor and no implicit conversion will take place. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 serialized: string
- output0 output: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16,uint32,uint64

## Attention Constraints

The implementation for StringToNumber on Ascend uses AICPU,
with badperformance. 

## Third-party framework compatibility

- compatible with tensorflow ParseTensor operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
