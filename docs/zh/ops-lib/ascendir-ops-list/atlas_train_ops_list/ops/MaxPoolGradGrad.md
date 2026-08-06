# MaxPoolGradGrad

```c
REG_OP(MaxPoolGradGrad)
    .INPUT(x1, TensorType::RealNumberType())
    .INPUT(x2, TensorType::RealNumberType())
    .INPUT(grad, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(MaxPoolGradGrad)
```

## Brief

Computes second-order gradients of the maxpooling function .

## Inputs

- x1: Original forward input tensor. Supported type:float, double, int32,
uint8, int16, int8, int64, uint16, float16, uint32, uint64.
- x2: Has the same type and format as input "x1".
- grad:Has the same type and format as input "x1" .

## Outputs

y: Has the same type and format as input "x1" . 

## Attributes

- ksize: A required list or tuple,
specifying the size of the sliding window.
- strides: A required list or tuple,
specifying the stride of the sliding window.
- padding: A required string, window sliding mode. Either SAME or VALID.
- data_format: An optional string.
Format of the original input, either NCHW or NHWC. Defaults to NHWC . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16
- input1 x2: float16
- input2 grad: float16
- output0 y: float16

## Attention Constraints

- Only Atlas Training Series Product is supported.
- "x1" and "grads" must have the same shape.
- "x2" and "y" must have the same shape. Otherwise, an error is reported.
- "x1", "x2", "grads", and "y" must be 5D tensors.
- ksize[H] and ksize[W] is in the range [1, 255].
- strides[H] and strides[W] is in the range [1, 63].
- Other dimensions of ksize and strides is 1 .

## Third-party framework compatibility

- Compatible with the TensorFlow operator MaxPoolGradGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
