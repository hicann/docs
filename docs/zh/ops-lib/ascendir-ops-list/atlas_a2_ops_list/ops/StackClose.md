# StackClose

```c
REG_OP(StackClose)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OP_END_FACTORY_REG(StackClose)
```

## Brief

Close the stack. 

## Inputs

The input handle must be type resource. Inputs include:
handle: A Tensor of type resource. The handle to a stack. 

## Third-party framework compatibility

Compatible with tensorflow StackClose operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
