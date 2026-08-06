# TensorScatterMin

```c
REG_OP(TensorScatterMin)
    .INPUT(input, TensorType::BasicType())
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType::BasicType())
    .OUTPUT(output, TensorType::BasicType())
    .OP_END_FACTORY_REG(TensorScatterMin)
```

## Brief

From the input tensor and updates tensor, select the minimum value according to indices to output.

## Inputs

Three inputs, including:
- input: Must be one of the following types:
double, float32, float16, bfloat16, complex32, complex64, complex128,
int8, uint8, int16, uint16, int32, uint32, int64, uint64, qint8, quint8, qint16, quint16, qint32.
- indices: Must be one of the following types:
      int32, int64.
- updates: Must have the same type as input.

## Outputs

output: A Tensor with the same type as input. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- input2 updates: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 output: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
