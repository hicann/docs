# ContinuationIndicator

```c
REG_OP(ContinuationIndicator)
    .REQUIRED_ATTR(time_step, Int)
    .REQUIRED_ATTR(batch_size, Int)
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(ContinuationIndicator)
```

## Brief

Outputs integers consisting of 0 and 1, used for lstm etc. 

## Inputs

- time_step: A tensor with data type int64. 0-D.
- batch_size: A tensor with data type int64. 0-D.

## Outputs

y: A Tensor. Has the  type float16 or float, 2-D, [time_step,batch_size]. 

## Attention Constraints

Compatible with the Caffe operator ContinuationIndicator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
