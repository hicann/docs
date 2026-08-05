# Pooling

```c
REG_OP(Pooling)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_INT32}))
    .ATTR(mode, Int, 0)                 // 0:max pooling or 1:avg pooling
    .ATTR(global_pooling, Bool, false)
    .ATTR(window, ListInt, {1,1})       // kernel size
    .ATTR(stride, ListInt, {1,1})       // stride size
    .ATTR(pad, ListInt, {0,0,0,0})      // pad size
    .ATTR(dilation, ListInt, {1,1,1,1})
    .ATTR(ceil_mode, Int, 0)
    .ATTR(data_format, String, "NCHW")
    .OP_END_FACTORY_REG(Pooling)
```

## Brief

Performs pooling on the input.

## Inputs

x: An NCHW tensor of type float16, float32, int8.

## Outputs

y: An NCHW tensor of type float16, float32, int32. 
The shape relationship between y and x as follows: 
Ny = Nx 
Cy = Cx 
Hy = (ceil_mode(Hx + pad[0] + pad[1] - window[0]) / stride[0]) + 1 
Wy = (ceil_mode(Wx + pad[2] + pad[3] - window[1]) / stride[1]) + 1 

## Attributes

- mode: An optional int32, specifying the pooling algorithm, either "0" (max
pooling) or "1" (avg pooling). Defaults to "0".
- global_pooling: An optional bool. Defaults to "false".
- window: Optional, including:
window[0]: An optional int32, specifying the window size along in the H
dimension. The value range is [1, 32768]. Defaults to "1".
window[1]: An optional int32, specifying the window size along in the W
dimension. The value range is [1, 32768]. Defaults to "1".
- stride: Optional, including:
stride[0]: An optional int32, specifying the stride along in the H dimension.
The value range is [1, 63]. Defaults to "1".
stride[1]: An optional int32, specifying the stride along in the W dimension.
The value range is [1, 63]. Defaults to "1".
- pad: Optional, including:
pad[0]: An optional int32, specifying the up padding. Defaults to "0".
pad[1]: An optional int32, specifying the bottom padding. Defaults to "0".
pad[2]: An optional int32, specifying the left padding. Defaults to "0".
pad[3]: An optional int32, specifying the right padding. Defaults to "0".
- dilation: Optional, including:
dilation[0]: An optional int32, specifying the up dilation. Defaults to "1".
dilation[1]: An optional int32, specifying the bottom dilation. Defaults to
"1".
dilation[2]: An optional int32, specifying the left dilation. Defaults to "1".
dilation[3]: An optional int32, specifying the right dilation. Defaults to
"1".
- ceil_mode: An optional int32, either "0" (ceil mode) or "1" (floor mode).
Defaults to "0".
- data_format: An optional string, Specify the data format of the input and
output data. With the default format "NCHW".

## Attention Constraints

- Type float32 is only for dynamic shape.
- window[0] * window[1] < 256.
- 1<=Hx<=4096,1<=Wx<=4096.
- If input tensor N is a prime number, it should be less than 65535.

## Third-party framework compatibility

- Compatible with the Caffe operator Pooling.
- Compatible with the TensorFlow operator Pooling.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
