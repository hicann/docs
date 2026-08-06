# AvgPoolUpdate

```c
REG_OP(AvgPoolUpdate)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(x2, TensorType({DA_INT4, DT_INT8, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(padding_mode, String, "CALCULATED")
    .ATTR(pads, ListInt, {0, 0, 0, 0})
    .ATTR(data_format, String, "NHWC")
    .ATTR(ceil_mode, Bool, false)
    .ATTR(exclusive, Bool, true)
    .OP_END_FACTORY_REG(AvgPoolUpdate)
```

## Brief

Performs average pooling on the input. Used in the combination of conv + avgpoolupdate to replace avgpool

## Inputs

x1: Output of upstream Conv2d. A tensor of type float16, float32.
x2: Input feature map of upstream Conv2d. A tensor of type int8, float16, float32.

## Outputs

y: The average pooled output tensor. Has the same type and format as input "x1".

## Attributes

- ksize: A required list of 4 ints, specifying the size (N, C, H, and W) of the sliding window,
where N = C = 1, and H and W are positive integers within the range [1, 255].
- strides: A required list of 4 ints, specifying the stride of the sliding window.
The strides of the N and C dimensions are 1.
The strides of the H and W dimensions are positive integers within the range [1, 63].
- padding_mode: A required string, specifying the padding algorithm,
either "VALID", "SAME" and "CALCULATED".
With "SAME" means that the outputs will have the same spatial dimensions as its inputs.
With "VALID" means no padding.
- pads: Pad value when padding_mode is "CALCULATED".
- data_format: An optional string, specifying the data format of "ksize" and "strides",
either "NCHW", or "NHWC" (default).
- ceil_mode: Use ceil or floor to calculate the output size when padding_mode is "CALCULATED".
- exclusive: Ignore padding area or not when calculating average.

## Attention Constraints

- Only single input and single output are supported.
- "ksize_H" and "ksize_W" are positive integers within the range [1, 255]. ksize_H * ksize_W < 256
- Due to instruction restrictions,
the values of "strides_h" and "strides_w" are positive integers within the range [1, 63].

## Third-party framework compatibility

Compatible with the TensorFlow/Pytorch/Onnx operator AvgPoolV2.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
