# YoloV5DetectionOutputD

```c
REG_OP(YoloV5DetectionOutputD)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .DYNAMIC_INPUT(windex, TensorType({DT_FLOAT16, DT_FLOAT}))
    .DYNAMIC_INPUT(hindex, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(biases, ListFloat)
    .ATTR(boxes, Int, 3)
    .ATTR(coords, Int, 4)
    .ATTR(classes, Int, 80)
    .ATTR(relative, Bool, true)
    .ATTR(obj_threshold, Float, 0.5)
    .ATTR(post_nms_topn, Int, 512)
    .ATTR(score_threshold, Float, 0.5)
    .ATTR(iou_threshold, Float, 0.45f)
    .ATTR(pre_nms_topn, Int, 512)
    .ATTR(N, Int, 10)
    .ATTR(resize_origin_img_to_net, Bool, false)
    .ATTR(out_box_dim, Int, 3)
    .ATTR(alpha, Float, 2.0)
    .OUTPUT(box_out, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(box_out_num, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(YoloV5DetectionOutputD)
```

## Brief

Performs YOLO V5 detection.

## Inputs

16 Input, including:
- The outputs of operator Yolo at the preceding layer (that is, three Yolo operators on YOLO v5) are used as the inputs of operator Yolov5DetectionOutput.
A Yolo operator has three outputs: "coords", "obj", and "class". For details, see the description of operator Yolo.
- imginfo: A float16, describing the image information including the required image height and width
and the actual image height and width.
- windex: A windex tensor with shape [height,weight]. Has the same type as the inputs.
[[0,1,2...(weight-1)],[0,1,2...(w-1)]...[0,1,2...(weight-1)]] consisting of h groups of [0, 1, 2...(weight-1)]
is formed for the three Yolo outputs, respectively .It's a dynamic input. 
- hindex: A hindex tensor with shape [height,weight]. Has the same type as the inputs. [[0,0...0],[1,1...1],[2,2...2]...[height-1,height-1...,height-1]] is formed for the three Yolo outputs, respectively .

## Outputs

- boxout: A tensor of type float16 or float32 with shape [batch,6,post_nms_topn](out_box_dim == 3) or [batch, 6*post_nms_topn](out_box_dim == 2),
           describing the information of each output box.
In output shape, 6 means x1, y1, x2, y2, score, label(class). Output by the number of box_out_num.
- boxoutnum: A tensor of type int32 with shape [batch,8], specifying the number of output boxes.
The output shape means only the first one of the 8 numbers is valid, the number of valid boxes in each batch, the maximum number of valid boxes in each batch is 1024

## Attributes

- biases: A required float32. "biases = Number of Yolo operators at the preceding layer x 2 x boxes"
- boxes: A required int32, specifying the number of anchor boxes predicted for each Yolo layer.
- coords: Specifies the number of coordinate parameters. Must be 4.
- classes: A required int32, specifying the number of classes to be predicted. The value range is [1, 80].
- relative: An optional bool. Defaults to and must be "true".
- obj_threshold: A required float, specifying the confidence threshold for box filtering, which is the output "obj" of operator Yolo). The value range is [0.0, 1.0].
- post_nms_topn: An optional int32. This attribute is reserved.
- score_threshold: A required float, specifying the class score threshold for box filtering, which is the output "class" of operator Yolo). The value range is [0.0, 1.0].
- iou_threshold: A required float, specifying the intersection-over-union (IOU) threshold for box filtering. The value range is [0.0, 1.0].
- pre_nms_topn: An optional int, specifying the number of boxes for non-maximum suppression (NMS). Defaults to "512".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 box_out: float16
- output1 box_out_num: int32

## Attention Constraints

- This operator applies only to the YOLO v5 network.
- The preceding layer of operator Yolov5DetectionOutput must be three Yolo operators.
@see Yolo()

## Third-party framework compatibility

It is a custom operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
