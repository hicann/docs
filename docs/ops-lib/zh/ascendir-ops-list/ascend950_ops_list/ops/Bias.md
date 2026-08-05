# Bias

```c
REG_OP(Bias)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(axis, Int, 1)
    .ATTR(num_axes, Int, 1)
    .ATTR(bias_from_blob, Bool, true)
    .OP_END_FACTORY_REG(Bias)
```

## Brief

Add 'bias' to 'x'.

## Inputs

Two inputs, including:
- x: An ND tensor of type bfloat16, float16 or float32.
- bias: An ND tensor of type bfloat16, float16 or float32. Shape rule see attention Constraints.

## Outputs

y: An ND tensor of type bfloat16, float16 or float32.

## Attributes

- axis: An optional int32 used to compute the shape of bias input from the online bottoms. Defaults to "1".
- num_axes: An optional int32 used to compute the shape of
bias input from a Caffe model trained offline. Defaults to "1".
- bias_from_blob: An optional bool. If "true", bias is input from a Caffe model trained offline.
If "false", bias is input from online bottoms. Defaults to "true".

## Attention Constraints

Assume that the shape length of "x" is "n" and that of "bias" is "m".
- "axis" is within the range [-n, n-1]. num_axes >= -1.
- If "bias_from_blob = true", "num_axes = -1", and "axis >= 0",
the ith axis of "bias" and the (i+"axis")th axis of "x" must have the same size (0 <= i < n-axis).
If "axis < 0", the ith axis of "bias" and the (i+n+"axis")th axis of "x" must have the same size (0 <= i < -axis).
- If "bias_from_blob = true" and "num_axes = 0", "bias" is a scalar with shape length 1 and dimension size 1.
- If "bias_from_blob = true", "num_axes > 0, and "axis >= 0",
"axis + num_axes" must be less than or equal to "n" and the ith axis of "bias" and
the (i+"axis")th axis of "x" must have the same size (0 <= i < num_axes).
If "axis < 0", "n + axis + num_axes" must be less than or equal to "n" and
the ith axis of "bias" and the (i+n+"axis")th axis of "x" must have the same size (0 <= i < num_axes).
- If "bias_from_blob = false", "bias" is not a scalar, and "axis >= 0",
"axis + m" must be less than or equal to "n" and the ith axis of "bias" and
the (i+"axis")th axis of "x" must have the same size (0 <= i < m).
If "axis < 0", "n + axis + m" must be less than or equal to "n" and
the ith axis of "bias" and the (i+n+"axis")th axis of "x" must have the same size (0 <= i < m). 

## Third-party framework compatibility

Compatible with the Caffe operator Bias.


---

[Back to Operator Specifications (Ascend950)](../README.md)
