# TensorArrayGradWithShape

```c
REG_OP(TensorArrayGradWithShape)
    .INPUT(handle, TensorType({ DT_RESOURCE }))
    .INPUT(flow_in, TensorType({ DT_FLOAT }))
    .INPUT(shape_to_prepend, TensorType({ DT_INT32 }))
    .OUTPUT(grad_handle, TensorType({ DT_RESOURCE }))
    .OUTPUT(flow_out, TensorType({ DT_FLOAT }))
    .ATTR(source, String, "")
    .OP_END_FACTORY_REG(TensorArrayGradWithShape)
```

## Brief

Creates a TensorArray for storing multiple gradients of values in
the given handle. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: A Tensor of type resource. The handle to the forward TensorArray.
- flow_in: A Tensor of type float. A float scalar that enforces proper
chaining of operations.
- shape_to_prepend: A Tensor of type int32. An int32 vector representing
a shape. 

## Outputs

- grad_handle: A Tensor of type resource.
- flow_out: A Tensor of type float.

## Attributes

source: A string. The gradient source string, used to decide which gradient
TensorArray to return. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 flow_in: float32
- input2 shape_to_prepend: int32
- output0 grad_handle: resource
- output1 flow_out: float32

## Third-party framework compatibility

Compatible with tensorflow TensorArrayGradWithShape operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
