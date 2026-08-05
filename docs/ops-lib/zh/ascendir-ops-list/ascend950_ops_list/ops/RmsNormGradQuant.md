# RmsNormGradQuant

```c
REG_OP(RmsNormGradQuant)
    .INPUT(dy, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(rstd, TensorType({DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scales_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(offset_x, TensorType({DT_INT32}))
    .OUTPUT(dx, TensorType({DT_INT8, DT_HIFLOAT8}))
    .OUTPUT(dgamma, TensorType({DT_FLOAT}))
    .ATTR(quant_mode, String, "static")
    .ATTR(div_mode, Bool, true)
    .ATTR(dst_type, Int, DT_INT8)
    .OP_END_FACTORY_REG(RmsNormGradQuant)
```

## Brief

RmsNormGradQuant operator interface implementation.

## Inputs

- dy: The gradient returned backward.
        A Tensor. Support dtype: float32/float16/bfloat16, support format: ND.
- x: The input of the forward operator.
       A Tensor. Support dtype: float32/float16/bfloat16, support format: ND.
- rstd: The intermediate computation result of the forward operator.
          A Tensor. Support dtype: float32, support format: ND.
- gamma: The input of the forward operator.
           A Tensor. Support dtype: float32/float16/bfloat16, support format: ND.
- scales_x: A required input tensor. Describing the weight of the quant operation.
             Support dtype: float32/float16/bfloat16, support format: ND.
- offset_x: An optional input tensor. Describing the bias of the quant operation.
              Support dtype: int32, support format: ND.

## Outputs

- dx: The gradient of input "x" after quantization, Has the same type and shape as "x".
        A Tensor. Support dtype: hifloat8/int8, support format: ND.
- dgamma: The gradient of input "gamma". Has the same type and shape as "gamma".
            A Tensor. Support dtype: float32, support format: ND.

## Attributes

- quant_mode: Required string parameter. Which formula used for quantized computation.
                The type is String. Only support static.
- div_mode: A required attribute control static quant algorithm, the type is bool.
              When true, scales will be divided by normalization output, otherwise, uses multiplication.
- dst_type: An optional attribute. Output y data type enum value. Support DT_HIFLOAT8, DT_INT8.
Defaults to DT_INT8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 rstd: float32
- input3 gamma: bfloat16,float16,float32
- input4 scales_x: bfloat16,float16,float32
- input5 offset_x: int32
- output0 dx: hifloat8,int8
- output1 dgamma: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
