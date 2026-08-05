# MaxPool3DWithArgmax

```c
REG_OP(MaxPool3DWithArgmax)
    .INPUT(x, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .OUTPUT(argmax, TensorType::IndexNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilation, ListInt, {1, 1, 1, 1, 1})
    .ATTR(ceil_mode, Bool, false)
    .ATTR(data_format, String, "NCDHW")
    .ATTR(argmax_type, String, "bitmask")
    .OP_END_FACTORY_REG(MaxPool3DWithArgmax)
```

## Brief

Performs max pooling3d on both max values and indices.

## Inputs

 One input:
 x: An 6D tensor. Supported type: float16. Format as NDC1HWC0. 

## Outputs

- y: An 6D tensor. the maxpool3d output(max value), supported type: float16, format as NDC1HWC0.
- argmax: A 5D uint16 tensor. the indice output, format as NC1HWC0.

## Attributes

 @li ksize: A required list of int32 values,
  specifying the size of the window for each dimension of the input tensor.
  No default value.
 @li strides: A required list of int32 values,
  specifying the stride of the sliding window for each dimension of
  the input tensor. No default value.
 @li pads: A required 3*2-dimension-list of int32 values.
  specifying the pad of three dimension of input, implement with 0.
 @li dilation: dilation of kernel. default value is {1,1,1,1,1}.
 @li ceil_mode: default value is false.
 @li data_format: the format of torch input, default value is "NCDHW".
 @li argmax_type: the function of this field is to determine the type of
  output argmax, "bitmask" is the default value, the argmax will return
  a img2col bitmask. "index_int32" and "index_int64" represent the torch
  output indices. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16
- output1 argmax: uint16


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
