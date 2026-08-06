# DrawBoundingBoxes

```c
REG_OP(DrawBoundingBoxes)
    .INPUT(images, TensorType({DT_FLOAT}))
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(DrawBoundingBoxes)
```

## Brief

Draw bounding boxes on a batch of images . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- images: A Tensor. Must be one of the following types: float. 4-D with
shape [batch, height, width, depth]. A batch of images. The format must be NHWC.
- boxes: A Tensor of type float32. 3-D with shape [batch,
num_bounding_boxes, 4] containing bounding boxes . 

## Outputs

A Tensor. Has the same type as images. The format must be NHWC. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float32
- input1 boxes: float32
- output0 y: float32

## Attention Constraints

Input images must be a 4-D tensor . 

## Third-party framework compatibility

Compatible with tensorflow DrawBoundingBoxes operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
