# AscendRequantS16

```c
REG_OP(AscendRequantS16)
    .INPUT(x0, TensorType({DT_INT16}))
    .INPUT(req_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(x1, TensorType({DT_INT16}))
    .OUTPUT(y0, TensorType({DT_INT8}))
    .OUTPUT(y1, TensorType({DT_INT16}))
    .ATTR(dual_output, Bool, false)
    .ATTR(relu_flag, Bool, false)
    .OP_END_FACTORY_REG(AscendRequantS16)
```

## Brief

Requantizes the input of int16 . 

## Inputs

- x0: A tensor of type int16, specifying the input. The format must be
FRACTAL_NZ or NC1HWC0. Shape support 4D ~ 8D.
- req_scale: A tensor of type uint64, specifying the scaling ratio.
The format support NC1HWC0. Shape support 5D, must be 1 in n, h, w.
- x1: A tensor of type int16, specifying the input.
The format support NC1HWC0, FRACTAL_NZ. Shape support 4D ~ 8D.
Has the same format as x. 

## Outputs

- y0: The dequantized output tensor of type int8.
The format support FRACTAL_NZ and NC1HWC0. Shape support 4D ~ 8D.
Has the same format and shape as input "x0".
- y1: The dequantized output tensor of type int16.
The format support FRACTAL_NZ and NC1HWC0. Shape support 4D ~ 8D.
Has the same format and shape as input "x0". 

## Attributes

- dual_output: An optional bool, specifying whether to perform dual ouput,
either "True" or "False". Defaults to "False".
- relu_flag: An optional bool, specifying whether to perform ReLU,
either "True" or "False". Defaults to "False" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x0: int16
- input1 req_scale: uint64
- input2 x1: int16
- output0 y0: int8
- output1 y1: int16

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
