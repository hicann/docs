# ThresholdV2

```c
REG_OP(ThresholdV2)
     .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT8, DT_INT32, DT_UINT8, DT_INT64, DT_BF16}))
     .INPUT(threshold, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT8, DT_INT32, DT_UINT8, DT_INT64, DT_BF16}))
     .OPTIONAL_INPUT(value, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT8, DT_INT32, DT_UINT8, DT_INT64, DT_BF16}))
     .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT8, DT_INT32, DT_UINT8, DT_INT64, DT_BF16}))
     .OP_END_FACTORY_REG(ThresholdV2)
```

## Brief

Thresholds each element of the input Tensor: y = (x > threshold) ? x : value

## Inputs

Three inputs, including:
- x: A ND Tensor. Support 1D~8D.
Must be one of the following types: float16, float32, int8, int32, uint8, int64, bfloat16. 
- threshold: A Tensor which should have the shape (1,), the value to threshold at.
Must be one of the following types: float16, float32, int8, int32, uint8, int64, bfloat16. 
- value: A Tensor which should have the shape (1,), the value to replace with. default value is 0.
Must be one of the following types: float16, float32, int8, int32, uint8, int64, bfloat16. 

## Outputs

y: A Tensor which has the same shape, format and type as the input x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int32,int64,uint8
- input1 threshold: bfloat16,float16,float32,int8,int32,int64,uint8
- input2 value: bfloat16,float16,float32,int8,int32,int64,uint8
- output0 y: bfloat16,float16,float32,int8,int32,int64,uint8

## Third-party framework compatibility

Compatible with the Pytorch operator Threshold.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
