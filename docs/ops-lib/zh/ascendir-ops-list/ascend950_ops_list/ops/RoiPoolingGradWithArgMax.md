# RoiPoolingGradWithArgMax

```c
REG_OP(RoiPoolingGradWithArgMax)
    .INPUT(grad, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(rois, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OPTIONAL_INPUT(roi_actual_num, TensorType({DT_INT32}))
    .INPUT(argmax, TensorType({DT_INT32}))
    .REQUIRED_ATTR(pooled_h, Int)
    .REQUIRED_ATTR(pooled_w, Int)
    .REQUIRED_ATTR(spatial_scale_h, Float)
    .REQUIRED_ATTR(spatial_scale_w, Float)
    .REQUIRED_ATTR(pool_channel, Int)
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(RoiPoolingGradWithArgMax)
```

## Brief

Performs the backpropagation of ROI Pooling . 

## Inputs

Five inputs, including:
- grad: A tensor of type float16 or float32, describing the gradient input,
with shape [batch, C, pooled_h, pooled_w].
- x: A tensor of type float16 or float32, describing the feature
map, with shape [N, H, W, C]. Note that shape[0] N should not exceed 1024.
- rois: A tensor of type float16 or float32, with 2D shape
[batch, 5], describing the ROIs. Each ROI consists of five
elements: "batch_id", "x1", "y1", "x2", and "y2", which "batch_id" indicates
the index of the input feature map, "x1", "y1", "x2", or "y2" must be
greater than or equal to "0.0". Note x1 should be less than x2, and
y1 should be less than y2. T hat shape[0] batch should not exceed 1024.
- roi_actual_num: An optional tensor of type int32, specifying
the number of ROIs per batch.
- argmax: A tensor of type int32, describing the index of grad,
with shape [batch, C, pooled_h, pooled_w]. Each value of argmax must be
within the corresponding pooling region. 

## Outputs

- y: A tensor of type float16 or float32, describing the result.

## Attributes

- pooled_h: A required int32, specifying the pooled H. Must be greater
than 0.
- pooled_w: A required int32, specifying the pooled W. Must be greater
than 0.
- spatial_scale_h: A required float32, scaling factor for mapping the input
coordinates of height to the ROI coordinates.
- spatial_scale_w: A required float32, scaling factor for mapping the input
coordinates of width to the ROI coordinates .
- pool_channel: A required int32, secifying the pooling channel.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: float16,float32
- input1 x: float16,float32
- input2 rois: float16,float32
- input3 roi_actual_num: int32
- input4 argmax: int32
- output0 y: float16,float32

## Attention Constraints

- "pool_channel" only support equal to the channel of "x".
- "roi_actual_num" only support equal to the number of "rois".
- NPU not support Channel of "x" being unaligned to 16.

## Third-party framework compatibility

It has a corresponding operator in MMCV.


---

[Back to Operator Specifications (Ascend950)](../README.md)
