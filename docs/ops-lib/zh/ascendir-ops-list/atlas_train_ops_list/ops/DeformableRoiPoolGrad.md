# DeformableRoiPoolGrad

```c
REG_OP(DeformableRoiPoolGrad)
    .INPUT(grad, TensorType({DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OUTPUT(grad_x, TensorType({DT_FLOAT}))
    .OUTPUT(grad_offset, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(output_size, ListInt)
    .ATTR(spatial_scale, Float, 1.0)
    .ATTR(sampling_ratio, Int, 0)
    .ATTR(gamma, Float, 0.1f)
    .OP_END_FACTORY_REG(DeformableRoiPoolGrad)
```

## Brief

Performs the backpropagation of DeformableRoiPool for training scenarios . 

## Inputs

Four inputs, including:
- grad_output: A 5HD gradient input of type float32
- feature_map: A 5HD Tensor of type float32.
- rois: ROI position. A 2D Tensor of float32 with shape (N, 5). "N" indicates the number of ROIs,
the value "5" indicates the indexes of images where the ROIs are located, "x0", "x1", "y0" and "y1".
- offset: An optional 5HD Tensor input, specifying the offset of sampled points .

## Outputs

- grad_fm: Gradient added to input "features". Has the same 5HD shape as input "features".
- grad_offset: Gradient added to input "offset". Has the same 4D shape as input "offset".

## Attributes

Four attributes, including:
- output_size: A required list of 2 ints, obtained based on the shape of "output" of DeformableRoiPool.
- spatial_scale: A optional attribute of type float, specifying the scaling ratio of "feature_map"
to the original image.
- sample_ratio: An optional attribute of type int, specifying the horizontal and vertical sampling
frequency of each output.
If this attribute is set to "0", the sampling frequency is equal to the rounded up value of "rois",
which is a floating point number. Defaults to "0".
- gamma: An optional attribute of type float, specfying the scaling factor of offset .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: float32
- input1 x: float32
- input2 rois: float32
- input3 offset: float32
- output0 grad_x: float32
- output1 grad_offset: float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
