# FullyConnectionCompress

```c
REG_OP(FullyConnectionCompress)
    .INPUT(x, TensorType({DT_UINT8, DT_INT8}))
    .INPUT(w, TensorType({DT_INT8}))
    .INPUT(comress_index, TensorType({DT_INT8}))
    .OPTIONAL_INPUT(b, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(offset_w, TensorType({DT_INT8}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .REQUIRED_ATTR(num_output, Int)
    .ATTR(transpose, Bool, false)
    .ATTR(axis, Int, 1)
    .ATTR(offset_x, Int, 0)
    .OP_END_FACTORY_REG(FullyConnectionCompress)
```

## Brief

Also known as a "fully-connected-compress" layer, computes an inner
product with a set of learned weights, and (optionally) adds biases. 

## Inputs

Five inputs, including:
- x: A Tensor of type uint8, int8.
- w: A weight matrix of type int8.
- compress_index: A compress index matrix of type int8.
- b: A optional Tensor of type int32.
- offset_w: A optional Tensor of type int8.

## Outputs

y: The result tensor of type int32. 

## Attributes

- num_output: A int, specifying the number of outputs.
- transpose: A bool, specifying whether to transpose input w, either "true"
or "false". Defaults to "false".
- axis: Optional. A int, 1 or 2, specifying which dimension the input "K"
starts from. Defaults to "1".
The product of the subsequent dimensions starting form first dimension or the
second dimension is "K".
- offset_x: An optional integer for quantized FullyConnectionCompress.
The negative offset added to the input image for int8 type. Ensure offset_x
within the effective range of int8 [-128, 127]. Defaults to "0". 

## Quantization supported or not

Yes

## Third-party framework compatibility

Compatible with the Caffe operator InnerProduct. 


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
