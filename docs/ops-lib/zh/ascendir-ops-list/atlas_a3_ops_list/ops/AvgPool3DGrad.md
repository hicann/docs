# AvgPool3DGrad

```c
REG_OP(AvgPool3DGrad)
    .INPUT(orig_input_shape, TensorType({DT_INT32}))
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(output, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(ksize, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(count_include_pad, Bool, true)
    .ATTR(divisor_override, Int, 0)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(AvgPool3DGrad)
```

## Brief

Computes average pooling3d backwards gradients.

## Inputs

- orig_input_shape: An one-dim tensor of type int32, which describes the
original input shape [N,C,D,H,W] of forward AvgPool3D.
- grads: A 5D Tensor of backwards gradient. With the format "NDHWC",
grads supports data type float16/float32/bfloat16.

## Outputs

output: A mutable tensor with the same shape as "orig_input_shape" and same type as "grads".

## Attributes

- ksize: List of ints. Describes the size of the window for each dimension of the input tensor.
Restriction: "ksize" value is in the range [1, 255] and <= "orig_input_shape" for DHW dimensions. 
For Atlas Inference Series Product: "ksize" length is 5. 
For Atlas Training Series Product: "ksize" length is 5. 
For Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component: "ksize" length is 3. 
For Atlas A3 Training Series Product/Atlas A3 Inference Series Product: "ksize" length is 3. 
For Ascend 950 AI Processor: "ksize" length is 3, without the limit of [1, 255] and must be greater than 0. 
- strides: List of ints. The stride of the sliding window for each dimension of the input tensor.
Restriction: "strides" value is in the range [1, 63]. 
For Atlas Inference Series Product: "strides" length is 5. 
For Atlas Training Series Product: "strides" length is 5. 
For Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component: "strides" length is 3. 
For Atlas A3 Training Series Product/Atlas A3 Inference Series Product: "strides" length is 3. 
For Ascend 950 AI Processor: "strides" length is 3, without the limit of [1, 63] and must be greater than 0. 
- pads: List of ints, implicit zero paddings on both sides of the input.
Restriction: "pads" is in the range [0, ksize/2]. 
For Atlas Inference Series Product: "pads" length is 6. 
For Atlas Training Series Product: "pads" length is 6. 
For Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component: "pads" length is 3. 
For Atlas A3 Training Series Product/Atlas A3 Inference Series Product: "pads" length is 3. 
For Ascend 950 AI Processor: "pads" length is 3. 
- ceil_mode: An optional bool. When true, will use ceil instead of floor in the formula to
compute the output shape. Default value false.
- count_include_pad: An optional bool. When true, will include the zero-padding in the
averaging calculation. Otherwise, not include paddings in averaging. Default value true.
- divisor_override: An optional int, if specified, it will be used as divisor, otherwise
size of the pooling region will be used. Default value 0, which means this attribute does not take effect.
- data_format: An optional string, the format of the input "grads". Defaults to "NDHWC".
For Atlas Inference Series Product: support "NDHWC" and "NCDHW". 
For Atlas Training Series Product: support "NDHWC" and "NCDHW". 
For Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component: only support "NDHWC". 
For Atlas A3 Training Series Product/Atlas A3 Inference Series Product: only support "NDHWC". 
For Ascend 950 AI Processor: only support "NDHWC". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 orig_input_shape: int32
- input1 grads: bfloat16,float16,float32
- output0 output: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator AvgPoolGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
