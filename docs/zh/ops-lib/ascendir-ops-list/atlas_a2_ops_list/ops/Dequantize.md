# Dequantize

```c
REG_OP(Dequantize)
    .INPUT(x, TensorType(DT_QINT8, DT_QUINT8, DT_QINT32, DT_QINT16, DT_QUINT16))
    .INPUT(min_range, TensorType{DT_FLOAT})
    .INPUT(max_range, TensorType{DT_FLOAT})
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(mode, String, "MIN_COMBINED")
    .OP_END_FACTORY_REG(Dequantize)
```

## Brief

Dequantizes the input tensor into a float tensor.
[min_range, max_range] are float32 tensors that specify the range
for "y".
The "mode" attribute controls exactly which calculations are used to convert
the float values to their quantized equivalents.

## Inputs

- x: A Tensor. Must be one of the following types: qint8, quint8, qint32, quint16, qint16.
Shape suport 1D ~ 8D. The format support ND or NC1HWC0.
- min_range: A Tensor of type float32.
Specifies the minimum scalar value possibly produced for the input. Shape suport 1D ~ 8D.
The format support ND or NC1HWC0. Has the same format as "x".
- max_range: A Tensor of type float32.
Specifies the maximum scalar value possibly produced for the input. The format support ND or NC1HWC0.
Shape suport 1D ~ 8D. "max_range" has the same shape as "min_range". Has the same format as "x". 

## Outputs

y: A dictionary of type float32. The format support ND or NC1HWC0.
"y" has the same shape and format as "x". 

## Attributes

mode: An optional string from: "MIN_COMBINED", "MIN_FIRST", and "SCALED".
Defaults to "MIN_COMBINED" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int8,int32,uint8
- input1 min_range: float32
- input2 max_range: float32
- output0 y: float32
### AI CPU
- input0 x: qint8,qint16,qint32,quint8,quint16
- input1 min_range: float32
- input2 max_range: float32
- output0 y: float32

## Attention Constraints

- "min_range" and "max_range" have the same shapes.
- "x" and "y" have the same shapes.

## Third-party framework compatibility

Compatible with the TensorFlow operator Dequantize.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
