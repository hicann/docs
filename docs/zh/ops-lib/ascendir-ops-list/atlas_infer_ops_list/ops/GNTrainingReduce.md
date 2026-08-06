# GNTrainingReduce

```c
REG_OP(GNTrainingReduce)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(sum, TensorType({DT_FLOAT}))
    .OUTPUT(square_sum, TensorType({DT_FLOAT}))
    .ATTR(num_groups, Int, 2)
    .OP_END_FACTORY_REG(GNTrainingReduce)
```

## Brief

Performs reduced group normalization.

## Inputs

x: A Tensor of type float16 or float32, with format NCHW NHWC . 

## Outputs

- sum: A Tensor of type float32 for SUM reduced "x". shape is [N, G, 1, 1, 1] for NCHW, [N, 1, 1, G, 1] for NHWC.
- square_sum: A Tensor of type float32 for SUMSQ reduced "x".shape is [N, G, 1, 1, 1] for NCHW, [N, 1, 1, G, 1]
for NHWC.

## Attributes

num_groups: A optional Int, specifying the num of groups. required, same to GNTrainingUpdate, default to 2 . 

## Attention Constraints

This operator is a GroupNorm fusion operator for updating the moving averages for training.
This operator is used in conjunction with GNTrainingUpdate.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
