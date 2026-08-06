# ToBool

```c
REG_OP(ToBool)
    .INPUT(input, TensorType({DT_INT64, DT_INT32, DT_INT16, DT_INT8, \
        DT_UINT8, DT_FLOAT, DT_DOUBLE, DT_STRING, DT_BOOL}))
    .OUTPUT(output, DT_BOOL)
    .OP_END_FACTORY_REG(ToBool)
```

## Inputs

input: The input tensors. Must be one of the following types: int32, int64, int16, int8, uint8,float32, float64, bool, string. 

## Outputs

output: The output tensors. Must be one of the following types: bool. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: bool,double,float32,int8,int16,int32,int64,string,uint8
- output0 output: bool


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
