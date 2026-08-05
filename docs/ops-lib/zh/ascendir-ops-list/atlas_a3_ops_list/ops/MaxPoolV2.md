# MaxPoolV2

```c
REG_OP(MaxPoolV2)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(ksize, TensorType({DT_INT32}))
    .INPUT(strides, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(MaxPoolV2)
```

## Brief

Performs max_pool_ext2 on the input .

## Inputs

Three inputs:
- x: A Tensor of type float16.
- strides: A required type of int32 values,
specifying the stride of the sliding window for each dimension of the input tensor. No default value.
- ksize: A required type of int32 values,
specifying the size of the window for each dimension of the input tensor. No default value. 

## Outputs

y: A Tensor. Has the same type and format as input "x" . 

## Attributes

- padding: A required string. No default value.
- data_format: An optional string. Defaults to "NHWC" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,qint8,uint8,uint16
- input1 ksize: int32
- input2 strides: int32
- output0 y: double,float16,float32,int8,int16,int32,int64,qint8,uint8,uint16

## Attention Constraints

- "ksize" is a list that has length 4: ksize[0] = 1 or ksize[3] = 1, ksize[1] * ksize[2] <= 255.
- "stride" is a list that has length 4: strides[0] = 1 or strides[3] = 1, strides[1] <= 63, strides[0] >= 1,
strides[2] <= 63, strides[2] >= 1.
- "padding" is either "SAME" or "VALID" .

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolV2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
