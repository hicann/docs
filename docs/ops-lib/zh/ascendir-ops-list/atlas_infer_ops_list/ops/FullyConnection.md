# FullyConnection

```c
REG_OP(FullyConnection)
    .INPUT(x, TensorType({DT_FLOAT16, DT_INT8, DT_INT4, DT_FLOAT, DT_BF16}))
    .INPUT(w, TensorType({DT_FLOAT16, DT_INT8, DT_INT4, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(b, TensorType({DT_FLOAT16, DT_INT32, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8, DT_INT4}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT32, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(num_output, Int)
    .ATTR(transpose, Bool, false)
    .ATTR(axis, Int, 1)
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(FullyConnection)
```

## Brief

Also known as a "fully-connected" layer, computes an inner product
with a set of learned weights, and (optionally) adds biases.

## Inputs

Four inputs, including:
- x: A Tensor of type float16, int8, int4, bf16.
- w: A weight matrix of type float16, int8, int4, float32, bf16.
- b: An optional Tensor of type float16, int32, float32, bf16.
- offset_w: An optional Tensor of type int8, int4.
Reserved. Only None Supported. 

## Outputs

y: The result tensor of type float16, int32, float32, bf16. 

## Attributes

- num_output: Required. An int, output neuron number. Reserved.
- transpose: A bool, specifying weight whether to transpose input w,
either "true" or "false". Defaults to "false".
- axis: Optional. An int, 1 or 2, specifying which dimension the input
"K" starts from. Defaults to 1.
The product of the subsequent dimensions starting form first dimension
or the second dimension is "K".
- offset_x: An optional integer for quantized FullyConnection.
The negative offset added to the input image for int8 type. Ensure offset_x
within the effective range of int8 [-128, 127]. Defaults to "0". 

## Quantization supported or not

Yes

## Third-party framework compatibility

Compatible with the Caffe operator InnerProduct. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
