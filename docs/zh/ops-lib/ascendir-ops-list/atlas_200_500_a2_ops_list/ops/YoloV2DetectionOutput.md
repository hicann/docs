# YoloV2DetectionOutput

```c
REG_OP(YoloV2DetectionOutput)
    .INPUT(coord_data, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(obj_prob, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(classes_prob, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(img_info, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(biases, ListFloat)
    .ATTR(boxes, Int, 5)
    .ATTR(coords, Int, 4)
    .ATTR(classes, Int, 20)
    .ATTR(relative, Bool, true)
    .ATTR(obj_threshold, Float, 0.5)
    .ATTR(post_nms_topn, Int, 512)
    .ATTR(score_threshold, Float, 0.5)
    .ATTR(iou_threshold, Float, 0.45f)
    .ATTR(pre_nms_topn, Int, 512)
    .OUTPUT(box_out, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(box_out_num, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(YoloV2DetectionOutput)
```

## Brief

Performs YOLO V2 detection . 

## Inputs

Four inputs, including:
- The outputs of operator Yolo at the preceding layer (that is, one Yolo operator on YOLO v2) are used as the inputs of operator Yolov3DetectionOutput.
Each Yolo operator has three outputs: "coords", "obj", and "class". For details, see the description of operator Yolo.
- img_info: A float16 or float32, describing the image information including the required image height and width
and the actual image height and width.

## Outputs

- boxout: A tensor of type float16 or float32 with shape [batch,6,post_nms_topn]. describing the information of each output box,
In output shape, 6 means x1, y1, x2, y2, score, label(class). Output by the number of box_out_num.
- boxoutnum: A tensor of type int32 with shape [batch,8,1,1], specifying the number of output boxes. It means only the first one of the 8 numbers is valid,
the number of valid boxes in each batch, the maximum number of valid boxes in each batch is 1024

## Attributes

- biases: A required float. "biases = Number of Yolo operators at the preceding layer x 2 x boxes"
- boxes: A required int32, specifying the number of anchor boxes predicted for each Yolo layer.
- coords: Specifies the number of coordinate parameters. Must be 4.
- classes: A required int32, specifying the number of classes to be predicted. The value range is [1, 20].
- relative: An optional bool. Defaults to and must be "true".
- obj_threshold: A required float, specifying the confidence threshold for box filtering,
which is the output "obj" of operator Yolo). The value range is [0.0, 1.0] . 
- post_nms_topn: An optional int32. This attribute is reserved.
- score_threshold: A required float, specifying the class score threshold for box filtering,
which is the output "class" of operator Yolo). The value range is [0.0, 1.0].
- iou_threshold: A required float, specifying the intersection-over-union (IOU) threshold for box filtering. The value range is [0.0, 1.0].
- pre_nms_topn: An optional int, specifying the number of boxes for non-maximum suppression (NMS). Defaults to "512".

## Attention Constraints

- This operator applies only to the YOLO v2 network.
- The preceding layer of operator Yolov2DetectionOutput must be one Yolo operator.
@see Yolo()

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
