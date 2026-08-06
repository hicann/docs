# TensorRedirect

```c
REG_OP(TensorRedirect)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8,
                          DT_INT64, DT_INT16, DT_UINT16, DT_UINT64, DT_UINT32, DT_BF16}))
    .OUTPUT(output_x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8,
                                  DT_INT64, DT_INT16, DT_UINT16, DT_UINT64, DT_UINT32, DT_BF16}))
    .OP_END_FACTORY_REG(TensorRedirect)
```

## Brief

Copy data from x to output_x.

## Inputs

One input, including:
x: A ND Tensor. Must be one of the following types:
bfloat16, float16, float32, int8, uint8, int16, uint16, int32, uint32, int64, uint64. 
Format is ND, Support 1D ~ 8D. 

## Outputs

output_x: A ND Tensor. Has the same dtype and format as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 output_x: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
