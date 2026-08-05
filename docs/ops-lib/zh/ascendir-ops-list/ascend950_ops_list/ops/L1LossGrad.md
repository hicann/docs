# L1LossGrad

```c
REG_OP(L1LossGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(predict, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(label, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(reduction, String, "mean")
    .OP_END_FACTORY_REG(L1LossGrad)
```

## Brief

Computes l1_loss_grad or l1_loss_backward.

## Inputs

Three inputs, including:
- grads: A Tensor. Must be one of the following types: float16, float32, bfloat16.
Required.
- predict: A Tensor. Has the same type as "grads". Required.
- label: A Tensor. Has the same type as "grads". Required.

## Outputs

y: A Tensor. Has the same type as "grads". 

## Attributes

reduction: An optional attribute of type String. Defaults to "mean". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 predict: bfloat16,float16,float32
- input2 label: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

- In Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component and
Atlas A3 Training Series Product/Atlas A3 Inference Series Product,
broadcasting is not allowed between input grads, input predict and input label, the three inputs must have the same shape. 

## Third-party framework compatibility

Compatible with the Pytorch operator L1LossGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
