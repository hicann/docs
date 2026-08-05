# MaxPool3DGrad

```c
REG_OP(MaxPool3DGrad)
    .INPUT(orig_x, TensorType::RealNumberType())
    .INPUT(orig_y, TensorType::RealNumberType())
    .INPUT(grads, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(padding, String, "SAME")
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(MaxPool3DGrad)
```

## Brief

Computes gradients of the MaxPool3D function .

## Inputs

- orig_x: Original forward input tensor, a mutable NDC1HWC0 tensor of type float16.
- orig_y: Original forward output tensor, a mutable NDC1HWC0 tensor of type float16.
- grads: Gradient tensor, a mutable NDC1HWC0 tensor of type float16 .

## Outputs

y: A mutable tensor. Has the same shape as "orig_x", but type is float32 . 

## Attributes

- ksize: A list that has length 5. The ksize of the H and W dimensions should be greater than 0.
The ksize of the N and C dimensions should be 1. e.g. For "data_format" is "NCDHW", ksize[0] = 1 and ksize[1] = 1.
For "data_format" is "NDHWC", ksize[0] = 1 and ksize[4] = 1.  
For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: The produce of the ksize in D, H and W dimensions
should be less than or equal to 255. e.g. For "data_format" is "NCDHW", ksize[2] * ksize[3] * ksize[4] <= 255. 
- strides: A list that has length 5. The stride of the N and C dimensions should be 1.
For Atlas Training Series Product, Atlas A2 Training Series Product/Atlas 800I A2 Inference Product,
Atlas A3 Training Series Product: The stride of the D, H and W dimensions should be greater than 0 and
smaller than 64.  
The stride of the D, H and W dimensions should be greater than 0.
- padding: A optional string. Defaults to "SAME", it support SAME and VALID.
- pads: A list of 6 ints. Supports only padding along the D,
H and W dimensions in sequence of head, tail, top, bottom, left and right.
to use.
- data_format: An optional string, Specify the data format of the input and
output data. Only support "NCDHW" and "NDHWC",With the default format "NDHWC" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 orig_x: float16
- input1 orig_y: float16
- input2 grads: float16
- output0 y: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPool3DGrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
