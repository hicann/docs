# AdaptiveAvgPool3dGrad

```c
REG_OP(AdaptiveAvgPool3dGrad)
    .INPUT(y_grad, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(x_grad, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(AdaptiveAvgPool3dGrad)
```

## Brief

Applies a 3D adaptive average pooling backward over
an input signal composed of several input planes.

## Inputs

Two input, including:
- y_grad: A Tensor. Must be one of the following data types:
    float16, bfloat16, float32. 
- x: A Tensor. Must be one of the following data types:
    float16, bfloat16, float32. 

## Outputs

    x_grad: A Tensor. Has the same data type as "x". 

## Attributes

    data_format: An optional string, Specify the data format of the input and
output data. With the default format "NDHWC". 
For Ascend 950PR/Ascend 950DT, both "NDHWC" and "NCDHW" are supported. All other platforms support only "NDHWC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- output0 x_grad: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator AdaptiveAvgPool3dGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
