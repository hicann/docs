# Normal

```c
REG_OP(Normal)
    .INPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(std, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(Normal)
```

## Brief

Output random value from  separate normal distribution. 

## Inputs

Inputs include:
mean: The mean is a tensor with the mean of each output element’s normal distribution .
std: The std is a tensor with the standard deviation of each output element’s normal distribution. 

## Outputs

y: A Tensor of type dtype . 

## Attention Constraints

The implementation for Normal on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with Pytorch Normal operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
