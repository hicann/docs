# MseLoss

```c
REG_OP(MseLoss)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(MseLoss)
```

## Brief

Computes mse loss.

## Inputs

two inputs, including:
 @li predict: An ND Tensor of dtype float16, float32 or bfloat16.
 @li label: An ND Tensor of dtype float16, float32 or bfloat16.

## Outputs

y: when reduction=sum/mean, y is scale. when reduction=none, y has
   same type and shape as "predict".

## Attributes

reduction:An optional str from sum, none, mean, Defaults to "mean".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 label: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
