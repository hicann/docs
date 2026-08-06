# TensorArrayGrad

```c
REG_OP(TensorArrayGrad)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(flow_in, TensorType({DT_FLOAT}))
    .OUTPUT(grad_handle, TensorType({DT_RESOURCE}))
    .OUTPUT(flow_out, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(source, String)
    .OP_END_FACTORY_REG(TensorArrayGrad)
```

## Brief

Creates a TensorArray for storing the gradients of values in the
given handle. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: The handle to a TensorArray.
- flow_in: A float scalar that enforces proper chaining of operations.

## Outputs

- grad_handle: A Tensor of type resource.
- flow_out: A Tensor of type float.

## Attributes

source: The gradient source string, used to decide which gradient
TensorArray to return. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 flow_in: float32
- output0 grad_handle: resource
- output1 flow_out: float32

## Third-party framework compatibility

Compatible with tensorflow TensorArrayGrad operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
