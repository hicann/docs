# Scale

```c
REG_OP(Scale)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(axis, Int, 1)
    .ATTR(num_axes, Int, 1)
    .ATTR(scale_from_blob, Bool, true)
    .OP_END_FACTORY_REG(Scale)
```

## Brief

Scales the input .

## Inputs

Three inputs, including:
- x: An ND tensor of type float16 or float32 or bfloat16.
- scale: An ND tensor of type float16 or float32 or bfloat16
- bias: An optional ND tensor of type float16 or float32 or bfloat16.

## Outputs

y: An ND tensor of type float16 or float32 or bfloat16. 

## Attributes

- axis: An optional int32 used to compute the shape of scale and bias input from the online bottoms.
Defaults to "1".
- num_axes: An optional int32 used to compute the shape of scale and bias input from a Caffe model trained offline.
Defaults to "1".
- scale_from_blob: An optional bool. If "true", scale and bias are input from a Caffe model trained offline.
If "false", scale and bias are input from online bottoms. Defaults to "true" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 scale: float16,float32
- input2 bias: float16,float32
- output0 y: float16,float32

## Attention Constraints

Assume that the shape length of "x" is "n" and that of "scale" is "m".
- "axis" is within the range [-n, n-1]. num_axes >= -1.
- If "scale_from_blob = true", "num_axes = -1", and "axis >= 0",
the ith axis of "scale" and the (i+"axis")th axis of "x" must have the same size (0 <= i < n-axis).
If "axis < 0", the ith axis of "scale" and the (i+n+"axis")th axis of "x" must have the same size (0 <= i < -axis).
- If "scale_from_blob = true" and "num_axes = 0", "scale" is a scalar with shape length 1 and dimension size 1.
- If "scale_from_blob = true", "num_axes > 0, and "axis >= 0", "axis + num_axes" must be less than or equal to "n"
and the ith axis of "scale" and the (i+"axis")th axis of "x" must have the same size (0 <= i < num_axes).
If "axis < 0", "n + axis + num_axes" must be less than or equal to "n" and the ith axis of "scale"
and the (i+n+"axis")th axis of "x" must have the same size (0 <= i < num_axes).
- If "scale_from_blob = false", "scale" is not a scalar, and "axis >= 0","axis + m" must be less than or
equal to "n" and the ith axis of "scale" and the (i+"axis")th axis of "x" must have the same size (0 <= i < m).
If "axis < 0", "n + axis + m" must be less than or equal to "n" and the ith axis of "scale" and
the (i+n+"axis")th axis of "x" must have the same size (0 <= i < m).
- If "bias" is not None, the constraints for "bias" is the same as that for "scale".

## Third-party framework compatibility

Compatible with the Caffe operator Scale.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
