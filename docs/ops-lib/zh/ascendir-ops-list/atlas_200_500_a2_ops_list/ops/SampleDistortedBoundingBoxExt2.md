# SampleDistortedBoundingBoxExt2

```c
REG_OP(SampleDistortedBoundingBoxExt2)
    .INPUT(image_size, TensorType({ DT_UINT8, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64 }))
    .INPUT(bounding_boxes, TensorType({ DT_FLOAT }))
    .INPUT(min_object_covered, TensorType({ DT_FLOAT }))
    .OUTPUT(begin, TensorType({ DT_UINT8, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64 }))
    .OUTPUT(size, TensorType({ DT_UINT8, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64 }))
    .OUTPUT(bboxes, TensorType({ DT_FLOAT }))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .ATTR(aspect_ratio_range, ListFloat, { 0.75f, 1.33f })
    .ATTR(area_range, ListFloat, { 0.05f, 1.0f })
    .ATTR(max_attempts, Int, 100)
    .ATTR(use_image_if_no_bounding_boxes, Bool, false)
    .OP_END_FACTORY_REG(SampleDistortedBoundingBoxExt2)
```

## Brief

Generate a single randomly distorted bounding box for an image . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- image_size: 1-D, containing [height, width, channels].
- bounding_boxes: 3-D with shape [batch, N, 4] describing the N bounding
boxes associated with the image.
- min_object_covered: The cropped area of the image must contain at least
this fraction of any bounding box supplied. The value of this parameter should
be non-negative. In the case of 0, the cropped area does not need to overlap
any of the bounding boxes supplied . 

## Outputs

- begin: 1-D, containing [offset_height, offset_width, 0].
- size: 1-D, containing [target_height, target_width, -1].
- bboxes: 3-D with shape [1, 1, 4] containing the distorted bounding box .

## Attributes

- seed: An optional int, default is 0, if either seed or seed2 are set to non-zero, the random number
generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int, default is 0, a second seed to avoid seed collision.
- aspect_ratio_range: An optional list of `floats`. Defaults to `[0.75f, 1.33f]`,
The cropped area of the image must have an aspect , ratio = width / height within this range.
- area_range: An optional list of `floats`. Defaults to `[0.05, 1]`. The
cropped area of the image must contain a fraction of the supplied image
within this range.
- max_attempts: An optional int, default is 100, number of attempts at generating a cropped region of the
image of the specified constraints. After max_attempts failures, return the
entire image.
- use_image_if_no_bounding_boxes: An optional bool, default is false, controls behavior if no bounding boxes
supplied. If true, assume an implicit bounding box covering the whole input.
If false, raise an error . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 image_size: int8,int16,int32,int64,uint8
- input1 bounding_boxes: float32
- input2 min_object_covered: float32
- output0 begin: int8,int16,int32,int64,uint8
- output1 size: int8,int16,int32,int64,uint8
- output2 bboxes: float32

## Attention Constraints

Input images can be of different types but output images are always float . 

## Third-party framework compatibility

Compatible with tensorflow SampleDistortedBoundingBoxExt2 operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
