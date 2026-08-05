# LinSpace

```c
REG_OP(LinSpace)
    .INPUT(start, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT8, DT_UINT8, DT_INT32, DT_INT16, DT_FLOAT16, DT_BF16}))
    .INPUT(stop, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT8, DT_UINT8, DT_INT32, DT_INT16, DT_FLOAT16, DT_BF16}))
    .INPUT(num, TensorType::IndexNumberType())
    .OUTPUT(output, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT8, DT_UINT8, DT_INT32, DT_INT16, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(LinSpace)
```

## Brief

Generates values in an interval .

## Inputs

Three ND inputs, including:
- start: A 1D Tensor, for the first entry in the range.
Type must be one of the following types:
float32, float16, double, bfloat16, int32, int16, int8, uint8.
- stop: A 1D Tensor, for the last entry in the range.
Type must be one of the following types:
float32, float16, double, bfloat16, int32, int16, int8, uint8.
- num: A 1D Tensor of type int32 or int64, for the common difference of the entries .

## Outputs

output: A 1D Tensor, Type is same with "start". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 start: bfloat16,float16,float32,int8,int16,int32,uint8
- input1 stop: bfloat16,float16,float32,int8,int16,int32,uint8
- input2 num: int32,int64
- output0 output: bfloat16,float16,float32,int8,int16,int32,uint8
### AI CPU
- input0 start: double,float32
- input1 stop: double,float32
- input2 num: int32,int64
- output0 output: double,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator lin_space.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
