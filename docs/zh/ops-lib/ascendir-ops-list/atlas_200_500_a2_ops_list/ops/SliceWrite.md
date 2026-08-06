# SliceWrite

```c
REG_OP(SliceWrite)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64}))
    .INPUT(begin, TensorType({DT_INT32, DT_INT64}))
    .INPUT(value, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64}))
    .OUTPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(SliceWrite)
```

## Brief

write tensor value to tensor x.

## Inputs

x: A Tensor of type float16/float/double/int32/int64. 
begin:A Tensor of type int32/int64. 
value: A Tensor of type float16/float/double/int32/int64.

## Outputs

x: same tensor with input x.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int32,int64
- input1 begin: int32,int64
- input2 value: double,float16,float32,int32,int64
- output0 x: double,float16,float32,int32,int64


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
