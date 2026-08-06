# DIoUGrad

```c
REG_OP(DIoUGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(bboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gtboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dbboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dgtboxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(trans, Bool, false)
    .ATTR(is_cross, Bool, true)
    .ATTR(mode, String, "iou")
    .OP_END_FACTORY_REG(DIoUGrad)
```

## Brief

Calculate the inverse gradient of DIoU. 

## Inputs

- dy : data of grad increment, a 1D Tensor of type float16 or float32 with
shape (N,).
- bboxes: Bounding boxes, a 2D Tensor of type float16 or float32 with
shape (4, N). "N" indicates the number of bounding boxes, and the value
"4" refers to [x1, y1, x2, y2] or [x, y, w, h].
- gtboxes: Ground-truth boxes, a 2D Tensor of type float16 or float32
with shape (4, M). "M" indicates the number of ground truth boxes, and
the value "4" refers to [x1, y1, x2, y2] or [x, y, w, h] . 

## Outputs

- dbboxes: A 2D Tensor of type float16 or float32 with shape [4, N].
- dgtboxes: A 2D Tensor of type float16 or float32 with shape [4, M].

## Attributes

- trans: An optional attr, true for 'xywh', false for 'xyxy', only support true now.
- is_cross: An optional attr, if false M equals N, only support false now.
- mode: An optional attr, a character string with the value range of ['iou', 'iof'],
         only support 'iou' now. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float32
- input1 bboxes: float32
- input2 gtboxes: float32
- output0 dbboxes: float32
- output1 dgtboxes: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
