# StackPush

```c
REG_OP(StackPush)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(element, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT16, \
                     DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, \
                     DT_DOUBLE, DT_UINT32, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT16, \
                     DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, \
                     DT_DOUBLE, DT_UINT32, DT_UINT64}))
    .ATTR(swap_memory, Bool, false)
    .OP_END_FACTORY_REG(StackPush)
```

## Brief

Push an element onto the stack. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: A Tensor of type resource. The handle to a stack.
- elem: A Tensor. The tensor to be pushed onto the stack.

## Outputs

y:A Tensor. Has the same type as elem. 

## Attributes

swap_memory: An optional bool. Defaults to False. Swap elem to CPU. Default
to false. 

## Third-party framework compatibility

Compatible with tensorflow StackPush operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
