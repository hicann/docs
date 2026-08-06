# LpLoss

```c
REG_OP(LpLoss)
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(p, Int)
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(LpLoss)
```

## Brief

Computes loss of lp, p=1,2,3....

## Inputs

- predict: An ND tensor of type float16, float32 or bfloat16. The predicted value.
- label: An ND tensor of type float16, float32 or bfloat16. The golden value.

## Outputs

 y: An ND tensor tensor with the same shape and type as "predict".

## Attributes

- p: A required int attribute that decides which loss to compute, now the p only can be 1 to compute l1_loss.
- reduction: An optional string which specifies the reduction to apply to the output. It can be "mean","sum" or "none". Defaults to "mean".
"none": no reduction will be applied.
"mean": the sum of the output will be divided by the number of elements in the output.
"sum": the output will be summed.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 predict: bfloat16,float16,float32
- input1 label: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator LpLoss.


---

[Back to Operator Specifications (Ascend950)](../README.md)
