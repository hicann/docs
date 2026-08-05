# MVN

```c
REG_OP(MVN)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(normalize_variance, Bool, true)
    .ATTR(across_channels, Bool, false)
    .ATTR(eps, Float, 1e-9f)
    .OP_END_FACTORY_REG(MVN)
```

## Brief

Normalizes the input .

## Inputs

One input:
x: An NCHW tensor of type float16 or float32 . 

## Outputs

y: An NCHW tensor of type float16 or float32. 

## Attributes

- normalize_variance: An optional bool specifying whether to normalize the
variance, either "true" (default) or "false"
the value "false" indicates only to subtract the mean.
- across_channels: An optional bool specifying whether to perform
across-channel MVN, either "true" or "false" (default)
The value "true" indicates "CHW" is treated as a vector.
- eps: An optional float32 epsilon for not dividing by zero. Defaults to
"1e-9" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

The input tensor must have the NCHW format, whose shape length must be 4.

## Third-party framework compatibility

Compatible with the Caffe operator MVN.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
