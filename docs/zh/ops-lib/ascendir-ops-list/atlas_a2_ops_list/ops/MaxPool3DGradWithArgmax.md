# MaxPool3DGradWithArgmax

```c
REG_OP(MaxPool3DGradWithArgmax)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .INPUT(argmax, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(dilation, ListInt, {1, 1, 1})
    .ATTR(ceil_mode, Bool, false)
    .ATTR(data_format, String, "NCDHW")
    .OP_END_FACTORY_REG(MaxPool3DGradWithArgmax)
```

## Brief

Performs the backpropagation of MaxPool3DGradWithArgmax.

## Inputs

Three inputs, including:
- x: An 5D Tensor. Supported type:float16, bfloat16, float32
Must set the format, supported format list ["NCDHW, NDHWC"].
- grad: An 5D Tensor. Supported type:float16, bfloat16, float32
Must set the format, supported format list ["NCDHW, NDHWC"].
- argmax: An 5D Tensor. Supported type:int32, int64
Must set the format, supported format list ["NCDHW, NDHWC"]. 

## Outputs

y: A Tensor. Has the same dtype, shape and format as input "x".

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension (D/H/W) of the input tensor.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the strides of the sliding window for each dimension (D/H/W) of the input tensor.
- pads: A required list of int8, int16, int32, or int64 values,
specifying the pads of the sliding window for each dimension of the input tensor.
- dilation: An optional list of int8, int16, int32, or int64 values,
specifying the dilation of the sliding window for each dimension of the input tensor, default value [1, 1, 1].
- ceil_mode: An optional Boolean value. When true, will use ceil instead of floor
in the formula to compute the output shape. Defaults to false.
- data_format: An optional string, supported values: ["NCDHW", "NDHWC"],
default value: ["NCDHW"]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 grad: bfloat16,float16,float32
- input2 argmax: int32
- output0 y: bfloat16,float16,float32

## Attention Constraints

- "ksize" is a list that has length 1 or 3(one value for each of D/H/W),
every element in the list must be a numeric greater than 0.
- "strides" is a list that has length 0 or 1 or 3(one value for each of D/H/W),
length 0 means use default ksize for each of D/H/W,
every element in the list must be a numeric greater than 0.
- "pads" is a list that has length 1 or 3(one value for each of D/H/W),
every element in the list must be a numeric greater than or equal to 0.
additionally, two strict size limits apply: 
1. Each pads value (pD/pH/pW for D/H/W dimensions) must be less than or equal to half of the corresponding "ksize" value (kD/kH/kW / 2). 
2. Each pads value (pD/pH/pW) must be less than or equal to ((corresponding ksize - 1) * corresponding dilation + 1) / 2
(i.e., pD ≤ ((kD - 1) * dD + 1) / 2, pH ≤ ((kH - 1) * dH + 1) / 2, pW ≤ ((kW - 1) * dW + 1) / 2).
- "dilation" is a list that has length 1 or 3(one value for each of D/H/W),
every element in the list must be a numeric greater than 0.
- "ceil_mode": This operator currently supports ceil_mode = false or true.

## Third-party framework compatibility

Compatible with the Torch operator MaxPool3DGradWithArgmax.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
