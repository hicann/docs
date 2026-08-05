# Addcdiv

```c
REG_OP(Addcdiv)
    .INPUT(input_data, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT64}))
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT64}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT64}))
    .INPUT(value, TensorType({ DT_FLOAT16, DT_BF16, DT_FLOAT, DT_INT32, DT_DOUBLE, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT64}))
    .OP_END_FACTORY_REG(Addcdiv)
```

## Brief

Performs the element-wise division of tensor x1 by tensor x2,
multiply the result by the scalar value and add it to tensor input_data.

## Inputs

Four inputs, including:
- input_data: A ND mutable input tensor. Must be one of the following types:
    float16, bfloat16, float32, double, int64.
- x1: A ND mutable input tensor of the same dtype as input_data.
- x2: A ND mutable input tensor of the same dtype as input_data.
- value: A ND mutable input tensor which includes only one element.
           Must be one of the following types: float16, bfloat16, float32, double, int64, int32.
           Type combination of [input_data(bf16)/value(int32)] is not supported. 

## Outputs

y: A mutable tensor. Has the same dtype as input_data. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_data: double,float16,float32,int64
- input1 x1: double,float16,float32,int64
- input2 x2: double,float16,float32,int64
- input3 value: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int64

## Third-party framework compatibility

Compatible with the PyTorch operator Addcdiv(version-1.5.0).


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
