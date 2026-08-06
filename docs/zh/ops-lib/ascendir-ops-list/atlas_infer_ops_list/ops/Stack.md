# Stack

```c
REG_OP(Stack)
    .INPUT(max_size, TensorType({DT_INT32}))
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(stack_name, String, "")
    .REQUIRED_ATTR(elem_type, Type)
    .OP_END_FACTORY_REG(Stack)
```

## Brief

Create a stack. 

## Inputs

The input max_size must be type int32. Inputs include:
max_size: A Tensor of type int32. The number of elements of a stack. 

## Outputs

handle: A Tensor of type resource. The handle to a stack. 

## Attributes

- stack_name: An optional string. Defaults to "".
- elem_type: The elements type of the created Stack.

## Third-party framework compatibility

Compatible with tensorflow Stack operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
