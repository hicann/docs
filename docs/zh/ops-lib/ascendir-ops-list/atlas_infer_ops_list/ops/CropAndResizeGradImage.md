# CropAndResizeGradImage

```c
REG_OP(CropAndResizeGradImage)
    .INPUT(grads, TensorType({DT_FLOAT}))
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(box_index, TensorType({DT_INT32}))
    .INPUT(image_size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(method, String, "bilinear")
    .REQUIRED_ATTR(T, Type)
    .OP_END_FACTORY_REG(CropAndResizeGradImage)
```

## Brief

Computes the gradient of the crop_and_resize op wrt the input
images tensor . 

## Inputs

Input grads must be a 4-D tensor. Inputs include:
- grads: A 4-D tensor of shape [num_boxes, crop_height, crop_width, depth].
The format must be NHWC.
- boxes: A 2-D tensor of shape [num_boxes, 4]. The i-th row of the tensor
specifies the coordinates of a box in the box_ind[i] image and is specified
in normalized coordinates [y1, x1, y2, x2].
- box_index: A 1-D tensor of shape [num_boxes] with int32 values in
[0, batch). The value of box_ind[i] specifies the image that the i-th box
refers to.
- image_size: A 1-D tensor with value [batch, image_height, image_width,
depth] containing the original image size. Both image_height and image_width
need to be positive . 

## Outputs

y:A 4-D tensor of shape [batch, image_height, image_width, depth]. The format
must be NHWC. 

## Attributes

- method: A string specifying the interpolation method. Only 'bilinear' is
supported for now .
- T: output of type

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grads: float32
- input1 boxes: float32
- input2 box_index: int32
- input3 image_size: int32
- output0 y: double,float16,float32

## Attention Constraints

Input grads must be a 4-D tensor . 

## Third-party framework compatibility

Compatible with tensorflow CropAndResizeGradImage operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
