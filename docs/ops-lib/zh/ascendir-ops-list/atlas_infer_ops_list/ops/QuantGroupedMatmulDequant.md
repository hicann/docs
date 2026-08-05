# QuantGroupedMatmulDequant

```c
REG_OP(QuantGroupedMatmulDequant)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(quantized_weight, TensorType({DT_INT8}))
    .INPUT(weight_scale, TensorType({DT_FLOAT, DT_INT64}))
    .INPUT(group_list, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(bias, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(x_scale, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OPTIONAL_INPUT(x_offset, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OPTIONAL_INPUT(smooth_scale, TensorType({DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16}))
    .ATTR(x_quant_mode, String, "pertoken")
    .ATTR(transpose_weight, Bool, true)
    .OP_END_FACTORY_REG(QuantGroupedMatmulDequant)
```

## Brief

QuantGroupedMatmulDequant operator interface implementation.

## Inputs

- x: A tensor. Quantized input data in combination operations. Support dtype: float16, dimension must be 2, support format: ND.
- quantized_weight: A tensor. Weights used for quantitative calculations. Support dtype: int8, dimension must be 3, support format: NZ.
- weight_scale: A tensor. Quantization coefficient for weight. Support dtype: float32 and int64, support format: ND.
- group_list: A tensor. The cumsum result (cumulative sum) of the matmul size distribution representing the x and out group axis direction.
Support dtype: int64, support format: ND.
- bias: An optional input bias tensor. Support dtype: int32, support format: ND.
- x_scale: A optional tensor. Indicates the quantization coefficient of x. Support dtype: float32 and float16, support format: ND.
- x_offset: A optional tensor. Indicates the offset of the input x. Support dtype: float32 and float16, support format: ND.
- smooth_scale: A optional tensor. The smoothing coefficient for x. Support dtype: float16, support format: ND.

## Outputs

y: A tensor. The result of the combination operation. Has the same dtype and format as x.
The shape supports 2D, with each dimension representing: (m, n). Where m is consistent with the m of x,
and n is consistent with the n of quantized_weight.

## Attributes

- x_quant_mode: dtype: String. Quantization mode for input x.
- transpose_weight: dtype: Bool. Indicates whether the input weight is transposed.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 quantized_weight: int8
- input2 weight_scale: float32,int64
- input3 group_list: int64
- input4 bias: int32
- input5 x_scale: float16,float32
- input6 x_offset: float16,float32
- input7 smooth_scale: float16
- output0 y: float16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
