# SwiGluQuant

```c
REG_OP(SwiGluQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(smooth_scales, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(offsets, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT4}))
    .OUTPUT(scale, TensorType({DT_FLOAT}))
    .ATTR(activate_left, Bool, false)
    .ATTR(quant_mode, String, "dynamic")
    .ATTR(group_list_type, Int, 0)
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(SwiGluQuant)
```

## Brief

SwiGlu and DynamicQuant are integrated to implement quantization. Only MOE group quantization is supported.

## Inputs

- x: A matrix tensor. Must be one of the following types: float32,float16,bfloat16, has format ND.
- smooth_scales: A optional tensor. Describing the result of dynamic quantize scales.
A tensor of type float32, has format ND.
- offsets: A optional tensor, describing the data of offsets, a tensor of type float32, has format ND.
- group_index: A optional tensor, described grouping data, a tensor of type int32, has format ND.

## Outputs

- y: A tensor ,type is int8 or int4, the size of the last dimension of output y is half of the size of input x.
And the size of other dimensions is the same as that of input x, now only support DT_INT8.
- scale: A tensor. Type is float32.
The shape of scale matches the shape of x across all dimensions except for the last dimension.

## Attributes

- activate_left: A optional bool.
    The SwiGlu activate_left algorithm to use:
    'false' (activate right) or 'true' (activate left), defalut is 'false' (activate right).
- quant_mode: Optional parameter, which formula used for quantized computation.
Type is String, the value must be "dynamic" or "static" or "dynamic_msd", "static" indicates static quantization,
"dynamic" indicates dynamic quantization, and "dynamic_msd" indicates dynamic mean squared displacement quantization, defaults to dynamic.
Now only support "dynamic" and "static" mode.
- group_list_type: Optional parameter, which used to describe group_index mode.
Type is Int, the value must be 0 or 1, 0 indicates "cumsum" mode, 1 indicates "count" mode.
Now only support "cumsum" and "count" mode.
- dst_type: Optional parameter, which used to describe quant output mode.
Type is Int, the value must be 2(DT_INT8 enum value) or 29(DT_INT4 enum value), 2 indicates "int8 quant output" mode, 29 indicates "int4 quant output" mode.
Now only support "int8 quant output" and "int4 quant output" mode.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 smooth_scales: float32
- input2 offsets: float32
- input3 group_index: int32
- output0 y: int4,int8
- output1 scale: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
