# DrawBoundingBoxesV2

```c
REG_OP(DrawBoundingBoxesV2)
    .INPUT(images, TensorType({DT_FLOAT}))
    .INPUT(boxes, TensorType({DT_FLOAT}))
    .INPUT(colors, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(DrawBoundingBoxesV2)
```

## Brief

Draw bounding boxes on a batch of images . 

## Inputs

- images: 4-D with shape `[batch, height, width, depth]`.
A batch of images.
- boxes: 3-D with shape `[batch, num_bounding_boxes, 4]`
containing bounding boxes.
- colors: 2-D. A list of RGBA colors to cycle through for the boxes .

## Outputs

y: Returns 4-D with the same shape as `images`.
The batch of input images with bounding boxes drawn on the images . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float32
- input1 boxes: float32
- input2 colors: float32
- output0 y: float32

## Third-party framework compatibility

Compatible with tensorflow DrawBoundingBoxesV2 operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
