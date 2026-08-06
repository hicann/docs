# BNTrainingReduce

```c
REG_OP(BNTrainingReduce)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(sum, TensorType({DT_FLOAT}))
    .OUTPUT(square_sum, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BNTrainingReduce)
```

## Brief

Performs reduced batch normalization .

## Inputs

x: A 4D tensor of type float16 or float32 or bfloat16, with format NHWC or NCHW.
Indicates the input tensor, that is, the original data to be normalized.

## Outputs

- sum: A 1D tensor of type float32 for SUM reduced "x". It represents the sum of the input tensor "x" on the C
axis.
The shape of sum is consistent with the C axis of "x". Has the same format as "x".
- square_sum: A 1D tensor of type float32 for SUMSQ reduced "x". It represents the sum of squares of the input
tensor "x" on the C axis.
The shape of sum is consistent with the C axis of "x". Has the same format as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 sum: float32
- output1 square_sum: float32

## Attention Constraints

This operator is a BatchNorm fusion operator for updating the moving
averages for training.
This operator is used in conjunction with BNTrainingReduce.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
