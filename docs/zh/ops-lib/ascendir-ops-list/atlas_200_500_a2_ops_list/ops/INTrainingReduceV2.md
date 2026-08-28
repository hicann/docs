# INTrainingReduceV2

```c
REG_OP(INTrainingReduceV2)
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(sum, TensorType({DT_FLOAT}))
    .OUTPUT(square_sum, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(INTrainingReduceV2)
```

## Brief

Performs reduce instance normalization.

## Inputs

x: A 4D tensor of type float16 or float32, format [NCHW, NHWC]

## Outputs

- sum: A 4D tensor of type float32 for SUM reduced "x", format [NCHW, NHWC], and HW=1.
- square_sum: A 4D tensor of type float32 for SUMSQ reduced "x", format [NCHW, NHWC], and HW=1.

## Attention Constraints

This operator is a InstanceNorm fusion operator for updating the moving averages for training.
This operator is used in conjunction with INTrainingUpdateV2.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
