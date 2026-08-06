# MaxPoolV3Grad

```c
REG_OP(MaxPoolV3Grad)
    .INPUT(orig_input, TensorType::RealNumberType())
    .INPUT(orig_output, TensorType::RealNumberType())
    .INPUT(grad, TensorType::RealNumberType())
    .OUTPUT(out_grad, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .ATTR(padding_mode, String, "CALCULATED")
    .ATTR(pads, ListInt, {0, 0, 0, 0})
    .ATTR(data_format, String, "NCHW")
    .ATTR(global_pooling, Bool, false)
    .ATTR(ceil_mode, Bool, false)
    .OP_END_FACTORY_REG(MaxPoolV3Grad)
```

## Brief

Computes gradients of the maxpooling function .

## Inputs

- orig_input: Original forward input tensor. Support type: float16, float32, Support format:[NCHW, NHWC].
- orig_output: Has the same shape and type as "x1", Support format:[NCHW, NHWC].
- grad: Has the same shape and type as "x1", Support format:[NCHW, NHWC].

## Outputs

out_grad: A mutable tensor. Has the same shape, type and format as "x1" . 

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor.
No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of
the input tensor. No default value.
- padding_mode: A required string. Defaults to "CALCULATED".
- pads:A required list of int8, int16, int32, or int64 values,
a data to caculate when padding_mode is "CALCULATED".
- data_format: An optional string. Defaults to "NHWC" .
- global_pooling: An optional bool. Whether to use the global pooling.
If global_pooling = true, kernel size and paddings will be ignored.
Default False. When the input parameters are set to float16, global_pooling does not support being set to true.
- ceil_mode: An optional bool. Whether to use the ceil function to calculate output
height and width. If it is set to False, the floor function will be used. Default False 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 orig_input: float16,float32
- input1 orig_output: float16,float32
- input2 grad: float16,float32
- output0 out_grad: float16,float32

## Attention Constraints

- Computing gradients of global pooling is not supported, which means
"ksize < x1".
- "ksize" is in the range [1, 255]. "strides" is in the range [1, 63]
- in static situation, orig_input, orig_output, grad and y cannot support float32.

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
