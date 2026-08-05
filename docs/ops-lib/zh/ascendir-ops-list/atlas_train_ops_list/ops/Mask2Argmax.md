# Mask2Argmax

```c
REG_OP(Mask2Argmax)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(mask, TensorType::IndexNumberType())
    .OUTPUT(argmax, TensorType::IndexNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .REQUIRED_ATTR(originshape, ListInt)
    .OP_END_FACTORY_REG(Mask2Argmax)
```

## Brief

Performs transform mask to argmax .

## Inputs

Two inputs:
- x: A 4D Tensor of type float16. supported format list ["NC1HWC0"]
- mask: A 4D Tensor of type uint16. supported format list ["NC1HWC0"].

## Outputs

argmax: A 4D Tensor of type int32. supported format list ["NC1HWC0"]. 

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values, specifying the size of the window for each dimension of the input tensor.
- strides: A required list of int8, int16, int32, or int64 values, specifying the stride of the sliding window for each dimension of the input tensor.
- padding: A required string.
- originshape:A required list of int8, int16, int32, or int64 values.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 mask: uint16
- output0 argmax: float32

## Attention Constraints

- "ksize" is a list that has length 4: ksize[0] = 1 or ksize[3] = 1, ksize[1] * ksize[2] <= 255.
- "strides" is a list that has length 4: strides[0] = 1 or strides[3] = 1, strides[1] <= 63, strides[0] >= 1, strides[2] <= 63, strides[2] >= 1.
- "padding" is either "SAME" or "VALID" .

## Third-party framework compatibility

Compatible with the TensorFlow operator Mask2Argmax.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
