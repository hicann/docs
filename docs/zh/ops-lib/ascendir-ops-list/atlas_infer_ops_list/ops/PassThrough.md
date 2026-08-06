# PassThrough

```c
REG_OP(PassThrough)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16,
                          DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16,
                           DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
    .ATTR(stride, Int, 2)
    .ATTR(reverse, Bool, false)
    .OP_END_FACTORY_REG(PassThrough)
```

## Brief

Performs plane or channel conversion on YoloV2.
If reverse=true: (N, H, W, C)->(N, H* stride, W* stride, C/(stride* stride)),
If reverse=false: (N, H, W, C)->(N, H/stride, W/stride, C*(stride* stride)).

## Inputs

x: A 4D tensor with format "NHWC". Type is float16, float32, int8, uint8, int16,
uint16, int32, uint32, int64, uint64. 

## Outputs

y: A 4D tensor with format "NHWC". Has same type as "x" . 

## Attributes

- stride: An optional int, specifying the plane or channel scaling
factor. Defaults to "2".
- reverse: An optional bool, specifying the conversion mode. If "true",
depth to space conversion is performed. If "false", space to depth conversion
is performed. Defaults to "false" . 

## Attention Constraints

- If reverse=true: C/(stride* stride) yields an integer result.
- If reverse=false: W/stride and H/stride yield integer results.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
