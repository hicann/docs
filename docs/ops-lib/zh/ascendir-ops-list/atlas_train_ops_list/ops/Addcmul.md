# Addcmul

```c
REG_OP(Addcmul)
    .INPUT(input_data, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8, DT_DOUBLE, DT_INT64}))
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8, DT_DOUBLE, DT_INT64}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8, DT_DOUBLE, DT_INT64}))
    .INPUT(value, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8, DT_DOUBLE, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8, DT_DOUBLE, DT_INT64}))
    .OP_END_FACTORY_REG(Addcmul)
```

## Brief

Performs the element-wise multiplication of tensor x1 by tensor x2,
multiply the result by the scalar value and add it to tensor input_data

## Inputs

Four inputs, including:
- input_data: A mutable input Tensor. Must be one of the following types:
    float16, bfloat16, float32, double, int64, int8, int32, uint8.
- x1: A mutable input Tensor of the same dtype as input_data.
- x2: A mutable input Tensor of the same dtype as input_data.
- value: A ND mutable input tensor which includes only one element.
           Must be one of the following types:
           float16, bfloat16, float32, double, int64, int8, int32, uint8. 

## Outputs

y: A mutable output Tensor. Has the same dtype as input_data. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_data: double,float16,float32,int8,int32,int64,uint8
- input1 x1: double,float16,float32,int8,int32,int64,uint8
- input2 x2: double,float16,float32,int8,int32,int64,uint8
- input3 value: double,float16,float32,int8,int32,int64,uint8
- output0 y: double,float16,float32,int8,int32,int64,uint8

## Third-party framework compatibility

Compatible with the PyTorch operator Addcmul.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
