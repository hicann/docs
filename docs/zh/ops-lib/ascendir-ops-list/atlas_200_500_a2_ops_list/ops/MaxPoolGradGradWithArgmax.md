# MaxPoolGradGradWithArgmax

```c
REG_OP(MaxPoolGradGradWithArgmax)
    .INPUT(x, TensorType::RealNumberType())
    .INPUT(grad, TensorType::RealNumberType())
    .INPUT(argmax, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .OP_END_FACTORY_REG(MaxPoolGradGradWithArgmax)
```

## Brief

Computes second-order gradients of the maxpooling function .

## Inputs

- x: Original forward input tensor. Supported type: float16, Support format: NC1HWC0.
- grad: Gradient tensor. Supported type: float16, Support format: NC1HWC0.
- argmax: An tensor of type uint16 or int64, Support format: NC1HWC0.

## Outputs

y:Result tensor. Supported type: float16, Support format: NC1HWC0.

## Attributes

- ksize: A required list, specifying the size of the sliding window.
- strides: A required list, specifying the stride of the sliding window.
- padding: A required string, window sliding mode. Either SAME or VALID.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 grad: float16,float32
- input2 argmax: int64,uint16
- output0 y: float16,float32

## Attention Constraints

- Only the cloud platform is supported.
- "x1" and "grads" must have the same shape.
- length of the shape of x, grads, argmax, y must be 5.
- shape of argmax must be (fmap_n, fmap_c1, kernel_h * kernel_w,
(shape_max_pool[2] * shape_max_pool[3] + 15) // 16 * 16, 1),
or (fmap_n, fmap_c1, kernel_h * kernel_w,
(shape_max_pool[2] * shape_max_pool[3] + 31) // 16, 16), else failed . 

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolGradGradWithArgmax.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
