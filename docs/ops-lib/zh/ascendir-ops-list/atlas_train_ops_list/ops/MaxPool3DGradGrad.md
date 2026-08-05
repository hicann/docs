# MaxPool3DGradGrad

```c
REG_OP(MaxPool3DGradGrad)
    .INPUT(orig_x, TensorType::RealNumberType())
    .INPUT(orig_y, TensorType::RealNumberType())
    .INPUT(grads, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(MaxPool3DGradGrad)
```

## Brief

Computes second-order gradients of the maxpooling3d function .

## Inputs

- orig_x: Original forward input tensor(NCDHW, NDHWC) with datatype TensorType::RealNumberType().
- orig_y: Original forward output tensor(NCDHW, NDHWC) with datatype TensorType::RealNumberType().
- grads: Gradient tensor(NCDHW, NDHWC) with datatype TensorType::RealNumberType().

## Outputs

- y: Result tensor of type float16

## Attributes

- ksize: A required list or tuple,
specifying the size of the sliding window.
- strides: A required list or tuple,
specifying the stride of the sliding window.
- pads: A required list or tuple
- data_format: An optional string. Format of the original input, either NCDHW or NDHWC. Defaults to NDHWC .

## Attention Constraints

- Only Atlas Training Series Product is supported.
- "orig_x" and "grads" must have the same shape.
- "orig_y" and "y" must have the same shape. Otherwise, an error is reported.
- "orig_x", "orig_y", "grads", and "y" must be 5D tensors .

## Third-party framework compatibility

- Compatible with the TensorFlow operator MaxPool3DGradGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
