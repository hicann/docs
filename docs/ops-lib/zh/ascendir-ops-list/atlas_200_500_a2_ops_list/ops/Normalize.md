# Normalize

```c
REG_OP(Normalize)
     .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8}))
     .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8}))
     .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8}))
     .ATTR(across_spatial, Bool, true)
     .ATTR(channel_shared, Bool, true)
     .ATTR(eps, Float, 1e-10f)
     .OP_END_FACTORY_REG(Normalize)
```

## Brief

Normalizes the input "x1" .

## Inputs

Two inputs, including:
- x1: A required NCHW or NHWC tensor of type float32, float16, or int8.
- x2: A required ND tensor of type float32, float16, or int8, specifying
the scaling factor. If "channel_shared" is "true", "x2" is a [1]-dimensional
vector. If "channel_shared" is "false", "x2" is a [C]-dimensional vector . 

## Outputs

y: A Tensor. Has the same type and format as "x1" . 

## Attributes

- across_spatial: An optional bool, specifying the dimension of input "x1"
to be summed. The value "true" (default) indicates dimensions C, H, W, and
the value "false" indicates dimension C.
- channel_shared: An optional bool, specifying the dimension count of input
"x2". The value "true" (default) indicates 1, and the value "false" indicates
dimension C of "x1".
- eps: An optional float32, specifying the bias when "across_spatial" is
"true". Defaults to "1e-10" . 

## Third-party framework compatibility

Compatible with the Caffe operator Normalize.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
