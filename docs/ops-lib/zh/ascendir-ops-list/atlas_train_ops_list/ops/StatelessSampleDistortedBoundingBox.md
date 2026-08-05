# StatelessSampleDistortedBoundingBox

```c
REG_OP(StatelessSampleDistortedBoundingBox)
    .INPUT(image_size, TensorType({ DT_UINT8, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64 }))
    .INPUT(bounding_boxes, TensorType({ DT_FLOAT }))
    .INPUT(min_object_covered, TensorType({ DT_FLOAT }))
    .INPUT(seed, TensorType({ DT_INT32, DT_INT64 }))
    .OUTPUT(begin, TensorType({ DT_UINT8, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64 }))
    .OUTPUT(size, TensorType({ DT_UINT8, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64 }))
    .OUTPUT(bboxes, TensorType({ DT_FLOAT }))
    .ATTR(aspect_ratio_range, ListFloat, { 0.75f, 1.33f })
    .ATTR(area_range, ListFloat, { 0.05f, 1.0f })
    .ATTR(max_attempts, Int, 100)
    .ATTR(use_image_if_no_bounding_boxes, Bool, false)
    .OP_END_FACTORY_REG(StatelessSampleDistortedBoundingBox)
```

## Brief

Generate a single randomly distorted bounding box for an image. 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- image_size: 1-D, containing [height, width, channels].
- bounding_boxes: 3-D with shape [batch, N, 4] describing the N bounding
boxes associated with the image.
- min_object_covered: The cropped area of the image must contain at least
this fraction of any bounding box supplied. The value of this parameter should
be non-negative. In the case of 0, the cropped area does not need to overlap
any of the bounding boxes supplied.
- seed: A shape [2] Tensor, the seed to the random number generator.

## Outputs

- begin: 1-D, containing [offset_height, offset_width, 0].
- size: 1-D, containing [target_height, target_width, -1].
- bboxes: 3-D with shape [1, 1, 4] containing the distorted bounding box.

## Attributes

- aspect_ratio_range: The cropped area of the image must have an aspect
ratio = width / height within this range.
- area_range: An optional list of `floats`. Defaults to `[0.05, 1]`. The
cropped area of the image must contain a fraction of the supplied image
within this range.
- max_attempts: Number of attempts at generating a cropped region of the
image of the specified constraints. After max_attempts failures, return the
entire image.
- use_image_if_no_bounding_boxes: Controls behavior if no bounding boxes
supplied. If true, assume an implicit bounding box covering the whole input.
If false, raise an error. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 image_size: int8,int16,int32,int64,uint8
- input1 bounding_boxes: float32
- input2 min_object_covered: float32
- input3 seed: int32,int64
- output0 begin: int8,int16,int32,int64,uint8
- output1 size: int8,int16,int32,int64,uint8

## Attention Constraints

Input images can be of different types but output images are always float. 

## Third-party framework compatibility

Compatible with tensorflow StatelessSampleDistortedBoundingBox operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
