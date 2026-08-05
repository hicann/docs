# CropAndResizeGradBoxes

```c
REG_OP(CropAndResizeGradBoxes)
    .INPUT(grads, TensorType({DT_FLOAT}))
    .INPUT(images, TensorType({DT_UINT8, DT_UINT16, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(box_index, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(method, String, "bilinear")
    .OP_END_FACTORY_REG(CropAndResizeGradBoxes)
```

## Brief

Computes the gradient of the crop_and_resize op wrt the input
boxes tensor . 

## Inputs

Input images and grads must be a 4-D tensor. Inputs include:
- grads: A 4-D tensor of shape [num_boxes, crop_height, crop_width, depth].
The format must be NHWC.
- images: A 4-D tensor of shape [batch, image_height, image_width, depth].
The format must be NHWC.
Both image_height and image_width need to be positive.
- boxes: A 2-D tensor of shape [num_boxes, 4]. The i-th row of the tensor
specifies the coordinates of a box in the box_ind[i] image and is specified in
normalized coordinates [y1, x1, y2, x2].
- box_index: A 1-D tensor of shape [num_boxes] with int32 values in
[0, batch). The value of box_ind[i] specifies the image that the i-th box
refers to . 

## Outputs

y:A 2-D tensor of shape [num_boxes, 4] . 

## Attributes

method: A string specifying the interpolation method. Only 'bilinear' is
supported for now . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grads: float32
- input1 images: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 boxes: float32
- input3 box_index: int32
- output0 y: float32

## Attention Constraints

Input images and grads must be a 4-D tensor . 

## Third-party framework compatibility

Compatible with tensorflow CropAndResizeGradBoxes operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
