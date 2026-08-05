# YoloxBoundingBoxDecode

```c
REG_OP(YoloxBoundingBoxDecode)
    .INPUT(priors, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(decoded_bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(YoloxBoundingBoxDecode)
```

## Brief

Generates bounding boxes based on "priors" and "bboxes".
It is a customized yolox operator . 

## Inputs

Two inputs, including:
- priors: prior sample boxes of origin image
A 2D Tensor of type float32 or float16 with shape (N, 4).
"N" indicates the number of boxes, and the value "4" refers to "x0", "x1", "y0", and "y1".
- bboxes_input: bboxes predicted by the model. A 2D Tensor of type float32 or float16 with shape (B, N, 4).
"B" indicates the batch_size, N indicates the number of boxes, 4 indicates "dx", "dy", "dw", and "dh" . 

## Outputs

bboxes_output: Bboxes generated based on "priors" and "bboxes_input". Have the same format
and type as "bboxes_input".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 priors: float16,float32
- input1 bboxes: float16,float32
- output0 decoded_bboxes: float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
