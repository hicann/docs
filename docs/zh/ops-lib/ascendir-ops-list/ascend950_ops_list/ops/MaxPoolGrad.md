# MaxPoolGrad

```c
REG_OP(MaxPoolGrad)
    .INPUT(x1, TensorType::RealNumberType())
    .INPUT(x2, TensorType::RealNumberType())
    .INPUT(grad, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(MaxPoolGrad)
```

## Brief

Computes gradients of the maxpooling function .

## Inputs

- x1: Original forward input tensor. Support type: float16, float32, Support Format:[NC1HWC0].
- x2: Original forward output tensor. Has the same type and format as input "x1".
- grad: Has the same type and format as input "x1".

## Outputs

y: A mutable tensor. Has the same shape, type and format as "x1" . 

## Attributes

- ksize: A required tuple or list of int values, specifying the size of the window for
each dimension of the input tensor.
- strides: A required tuple or list of int values, specifying the stride of the sliding
window for each dimension of the input tensor.
- padding: A required string, specifying the type of padding algorithm
to use.
- data_format: An optional string, Specify the data format of the input and
output data. With the default format "NHWC" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 grad: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x1: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input2 grad: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- ksize is limited by buffer with full tiling.
- "ksize" is in the range [1, 255]. "strides" is in the range [1, 63](valid situation: tik branch)
- In static situation, when atomic_flag is True, the output y only support float16.
- Atlas Inference Series Product and Atlas Training Series Product only support float16 input.
- Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component and
Atlas A3 Training Series Product/Atlas A3 Inference Series Product support float16 or float32 input.

## Third-party framework compatibility

Compatible with the TensorFlow operator MaxPoolGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
