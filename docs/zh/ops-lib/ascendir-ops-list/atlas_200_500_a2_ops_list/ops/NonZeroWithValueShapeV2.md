# NonZeroWithValueShapeV2

```c
REG_OP(NonZeroWithValueShapeV2)
    .INPUT(value, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16,
                            DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .INPUT(index, TensorType({DT_INT32}))
    .INPUT(count, TensorType({DT_INT32}))
    .OUTPUT(value, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16,
                              DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .OUTPUT(index, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(NonZeroWithValueShapeV2)
```

## Brief

Returns a tensor with updated shape from NonZeroWithValue. 

## Inputs

value: A Tensor. The output of NonZeroWithValue. 
index: A Tensor. The output of NonZeroWithValue. 
count: A Tensor. The type is INT32, means count for non_zero ele in input. 

## Outputs

value: A Tensor. The output value is the updated shape of the input value. 
index: A Tensor. The output index is the updated shape of the input index. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 value: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 index: int32
- input2 count: int32
- output0 value: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 index: int32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
