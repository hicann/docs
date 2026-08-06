# Dilation2DBackpropInput

```c
REG_OP(Dilation2DBackpropInput)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64, DT_UINT8, DT_INT16, DT_INT8, DT_UINT16}))
    .INPUT(filter,
           TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64, DT_UINT8, DT_INT16, DT_INT8, DT_UINT16}))
    .INPUT(out_backprop,
           TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64, DT_UINT8, DT_INT16, DT_INT8, DT_UINT16}))
    .OUTPUT(y,
            TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_INT64, DT_UINT8, DT_INT16, DT_INT8, DT_UINT16}))
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(rates, ListInt)
    .ATTR(padding_mode, String, "SAME")
    .ATTR(pads, ListInt, {0, 0, 0, 0})
    .ATTR(ceil_mode, Bool, false)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(Dilation2DBackpropInput)
```

## Brief

Performs Dilation2DBackpropInput on the input.

## Inputs

- x: A tensor of shape is 4d, format is support NHWC.
- filter: A tensor of shape is 3d, the type is same with x, and the c dimension is same with x.
- out_backprop: Has the same type and format as input x and the c dimension is same with x.

## Outputs

y: The output tensor. Has the same type and format as input "x" . 

## Attributes

- strides: A required list of 4 ints, specifying the stride of the sliding window. The strides of the N and C dimension are 1.
- rates: A required list of 4 ints, the rates of the N and C dimensions are 1.
- padding_mode: A optional string. Defaults to "SAME", it support SAME and VALID.
- pads: A optional list of 4 ints. Defaults to {0, 0, 0, 0}.
- ceil_mode: An optional bool. Defaults to "false". Use ceil or floor to calculate the output size when padding_mode is "CALCULATED".
- data_format: An optional string, specifying the data format of "rates" and "strides", either "NCHW" or "NHWC" (default).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 filter: float32
- input2 out_backprop: float32
- output0 y: float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 filter: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 out_backprop: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator Dilation2DBackpropInput.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
