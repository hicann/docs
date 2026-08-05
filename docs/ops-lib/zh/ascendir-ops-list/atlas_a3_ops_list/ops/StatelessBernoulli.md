# StatelessBernoulli

```c
REG_OP(StatelessBernoulli)
    .INPUT(shape, TensorType({ DT_INT32, DT_INT64}))
    .INPUT(prob, TensorType({ DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(seed, TensorType({ DT_INT64 }))
    .INPUT(offset, TensorType({ DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32,
                            DT_INT64, DT_UINT64, DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(StatelessBernoulli)
```

## Brief

Generate bernoulli distribution for tensor input . 

## Inputs

include:
- shape: 1-D. The shape of the input tensor. A tensor of type int32, int64.
- prob: 0-D. A tensor of type float16, float32, double, bfloat16.
Probability of bernoulli distribution, the value range from 0 to 1.
- seed: If seed is set to be -1, and offset is set to be 0, the random number
generator is seeded by a random seed. Otherwise, it is seeded by the given seed.
A tensor of type int64.
- offset: To avoid seed collision. A tensor of type int64, must be a multiple of 4.

## Outputs

y: A tensor. The tensor of type support int8, uint8, int16, uint16,
 int32, uint32, int64, uint64, bool, float16, float, double, bf16. 

## Attributes

dtype: The data type for the elements of the output tensor.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 prob: bfloat16,double,float16,float32
- input2 seed: int64
- input3 offset: int64
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
