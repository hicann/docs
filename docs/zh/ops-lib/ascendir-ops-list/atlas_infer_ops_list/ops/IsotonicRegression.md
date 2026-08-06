# IsotonicRegression

```c
REG_OP(IsotonicRegression)
    .INPUT(input, TensorType::RealNumberType())
    .OUTPUT(output, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(segments, TensorType({DT_INT32}))
    .ATTR(output_dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(IsotonicRegression)
```

## Brief

Solves a batch of isotonic regression problems. 

## Inputs

- input: A Tensor.

## Outputs

- output: A Tensor. A Tensor of type float16, float32, double.
- segments: A Tensor. A Tensor of type int32.

## Attributes

- output_dtype: The data type of output. Defaults to float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 output: double,float16,float32
- output1 segments: int32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
