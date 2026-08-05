# MaxPoolWithArgmax

```c
REG_OP(MaxPoolWithArgmax)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .OUTPUT(argmax, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(Targmax, Int, 9)
    .ATTR(include_batch_in_index, Bool, false)
    .ATTR(data_format, String, "NHWC")
    .ATTR(nan_prop, Bool, false)
    .OP_END_FACTORY_REG(MaxPoolWithArgmax)
```

## Brief

Performs max pooling on the input and outputs both max values and
indices .

## Inputs

One input:
x: An 4D Tensor. Supported type:float16, bfloat16, float32
Must set the format, supported format list ["NCHW, NHWC"]. 

## Outputs

- y: A Tensor. Has the same type and format as input "x".
- argmax: A Tensor. Has the same format as input "x", Supported format list ["NCHW, NHWC"].

## Attributes

- ksize: A required list of int8, int16, int32, or int64 values,
specifying the size of the window for each dimension of the input tensor.
No default value.
- strides: A required list of int8, int16, int32, or int64 values,
specifying the stride of the sliding window for each dimension of
the input tensor. No default value.
- padding: A required string. Must be ["SAME", "VALID"].
- Targmax: A required int32 or int64. Default value: 9(int64).
Specify the dtype for argmax output, currently not used(only int32 or int64).
- include_batch_in_index: A required bool. Must be false.
- data_format: A required string. Default value: [NHWC].
- nan_prop: A required bool. Default value: false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16
- output1 argmax: uint16
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output1 argmax: int32,int64

## Attention Constraints

- "ksize" is a list that has length 4: [NHWC] required ksize[0] = 1 and ksize[3] = 1,
[NCHW] required ksize[0] = 1 and ksize[1] = 1.
- "stride" is a list that has length 4: [NHWC] required strides[0] = 1 and strides[3] = 1,
[NCHW] required strides[0] = 1 and strides[1] = 1.
- "padding" is either "SAME" or "VALID" .
- Targmax: only is 3 and 9, int32 corresponds to 3, int64 corresponds to 9.
- include_batch_in_index: only support include_batch_in_index is false.

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolWithArgmax.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
