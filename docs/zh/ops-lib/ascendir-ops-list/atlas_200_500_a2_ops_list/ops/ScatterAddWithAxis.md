# ScatterAddWithAxis

```c
REG_OP(ScatterAddWithAxis)
    .INPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .INPUT(indices, TensorType::IndexNumberType())
    .INPUT(updates, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .OUTPUT(var, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32,DT_INT8,DT_UINT8}))
    .REQUIRED_ATTR(axis, Int)
    .OP_END_FACTORY_REG(ScatterAddWithAxis)
```

## Brief

Adds sparse "updates" to a variable reference .

## Inputs

Three inputs, including:
- var: An ND Tensor .
Must be one of the following types: float16, float32, int32, int8, uint8
- indices: An ND Tensor of type int32 or int64
- updates: An ND Tensor .
Must be one of the following types: float16, float32, int32, int8, uint8

## Outputs

var: A Tensor. Has the same type and format as input "var" . 

## Attributes

axis: An required int. The axis along which to index. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 var: bfloat16,float16,float32,int8,int32,uint8
- input1 indices: int32,int64
- input2 updates: bfloat16,float16,float32,int8,int32,uint8
- output0 var: bfloat16,float16,float32,int8,int32,uint8

## Third-party framework compatibility

Compatible with the pytorch operator ScatterAdd.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
