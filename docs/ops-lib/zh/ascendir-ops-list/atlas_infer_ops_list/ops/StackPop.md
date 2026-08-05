# StackPop

```c
REG_OP(StackPop)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(element, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT16, \
                     DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, \
                     DT_DOUBLE, DT_UINT32, DT_UINT64}))
    .REQUIRED_ATTR(elem_type, Type)
    .OP_END_FACTORY_REG(StackPop)
```

## Brief

Pop the element at the top of the stack. 

## Inputs

The input handle must be type resource. Inputs include:
handle: A Tensor of type resource. The handle to a stack. 

## Outputs

element:A Tensor of type elem_type. 

## Attributes

elem_type: A DType. The type of the elem that is popped. 

## Third-party framework compatibility

Compatible with tensorflow StackPop operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
