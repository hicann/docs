# Yolo

```c
REG_OP(Yolo)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(coord_data, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(obj_prob, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(classes_prob, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(boxes, Int, 3)
    .ATTR(coords, Int, 4)
    .ATTR(classes, Int, 80)
    .ATTR(yolo_version, String, "V3")
    .ATTR(softmax, Bool, false)
    .ATTR(background, Bool, false)
    .ATTR(softmaxtree, Bool, false)
    .OP_END_FACTORY_REG(Yolo)
```

## Brief

Normalizes data. It is called Region on YOLO v2 and Yolo on YOLO v3 . 

## Inputs

x: An NCHW tensor of type float16 or float32. The data is with shape
(N, boxes*(coords+obj+classes), H, W),where, "obj" indicates the confidence of
an object, and only one confidence is supported. Boxes are arranged as
xx...xyy...yww...whh...hbb...bc0c0..c0c1c1...c1......cncn...cn . 

## Outputs

- coord_data: A float16 or float32 with shape [N, boxes*coords,
ceilx(height*width*2+32, 32)/2], where "ceil" indicates that a detected box is
aligned upwards with the second parameter. Specifies the coordinates of a
detected box.
- obj_prob: A float16 or float32 with
shape [N, ceilx(boxes*height*width *2+32, 32)/2], where "ceil" indicates that
a detected box is aligned upwards with the second parameter. Specifies the
confidence.
- classes_prob: A float16 or float32 with
shape [N, classes, ceilx(boxes*height*width *2+32, 32)/2], where "ceil"
indicates that a detected box is aligned upwards with the second parameter.
Specifies the prediction classes . 

## Attributes

- boxes: An optional int, specifying the number of anchor boxes. Defaults to
"3". when "yolo_version = V2", Defaults to "5".
- coords: An optional int, specifying the number of parameters required for locating
an object. The value is fixed at "4", corresponding to (x,y,w,h). Defaults to
"4".
- classes: An optional int, specifying the number of prediction classes. Defaults to
"80". The value range is [1, 1024].
- yolo_version: An optional string, specifying the YOLO version, either "V2" or "V3".
Defaults to "V3".
- softmax: An optional bool, specifying whether to perform softmax, valid only when
"yolo_version = V2". Defaults to "false".
- background: An optional bool, specifying the operation types of the obj and classes,
used in conjunction with "softmax" and valid only when "yolo_version = V2".
Defaults to "false".
- softmaxtree: An optional bool, Fixed to False, defined in Lite, but not used.
Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 coord_data: float16
- output1 obj_prob: float16
- output2 classes_prob: float16

## Attention Constraints

- This operator applies to YOLO v2 and v3 networks.
- The succeeding layer of the Yolo operator must be operator
Yolov3DetectionOutput.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
