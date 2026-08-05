# TensorEqual

```c
REG_OP(TensorEqual)
    .INPUT(input_x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT32, DT_INT8, DT_UINT8, DT_BOOL, DT_BF16, DT_IN16, DT_UINT16, DT_UINT32, DT_UINT64}))
    .INPUT(input_y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT32, DT_INT8, DT_UINT8, DT_BOOL, DT_BF16, DT_IN16, DT_UINT16, DT_UINT32, DT_UINT64}))
    .OUTPUT(output_z, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(TensorEqual)
```

## Brief

Compare two tensors are totally equal or not, only output a bool value"

## Inputs

Two inputs, including:
- input_x: A ND tensor. the first tensor. Must be one of the following types: float16, float32, double,
int64, int32, int8, uint8, bool, bfloat16, int16, uint16, uint32, uint64. 
- input_y: A ND tensor of the same dtype as "input_x".

## Outputs

output_z: A ND tensor. Bool type, compare result of the two inputs. True if element in input_x is equal to input_y, False otherwise. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_x: bfloat16,bool,float16,float32,int8,int32,uint8
- input1 input_y: bfloat16,bool,float16,float32,int8,int32,uint8
- output0 output_z: bool
### AI CPU
- input0 input_x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 input_y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 output_z: bool

## Third-party framework compatibility

Compatible with the PyTorch equal operator. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
