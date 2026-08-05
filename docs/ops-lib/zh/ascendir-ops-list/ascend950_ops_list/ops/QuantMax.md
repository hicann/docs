# QuantMax

```c
REG_OP(QuantMax)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scale, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OUTPUT(amax, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(round_mode, String, "rint")
    .ATTR(dst_type, Int, DT_FLOAT8_E5M2)
    .OP_END_FACTORY_REG(QuantMax)
```

## Brief

Quantizes the input tensor x with the given scale and calculates the
       absolute maximum value (amax) of x.

## Inputs

- x: A required tensor of type FLOAT32, FLOAT16 or BFLOAT16, specifying the input tensor
       to be quantized. The format must be ND. Shape supports 1D to 8D. 
- scale: A required 1D tensor of type FLOAT32 with shape [1], specifying the
           quantization scaling factor. 

## Outputs

- y: A required tensor of type HIFLOAT8, FLOAT8_E5M2 or FLOAT8_E4M3FN,
       specifying the quantized output. The format must be ND.
       Shape is the same as input "x". Data type is determined by dst_type. 
- amax: A required 1D tensor of type FLOAT32, FLOAT16 or BFLOAT16 with shape [1],
          specifying the absolute maximum value of input "x".
          Data type must be the same as input "x". 

## Attributes

- round_mode: An optional string, specifying the rounding mode for the cast operation.
                Default value: "rint". Valid values depend on dst_type:
                - For FLOAT8_E5M2 (35) or FLOAT8_E4M3FN (36): only "rint" is supported.
                - For HIFLOAT8 (34): "round" or "hybrid" is supported. 
- dst_type: An optional int64, specifying the output quantized data type.
              Default value: 35 (FLOAT8_E5M2).
              Valid values: 34 (HIFLOAT8), 35 (FLOAT8_E5M2), 36 (FLOAT8_E4M3FN). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 scale: float32
- output0 y: float8_e4m3fn,float8_e5m2,hifloat8
- output1 amax: bfloat16,float16,float32

## Third-party framework compatibility

It is a custom operator on Ascend NPU.


---

[Back to Operator Specifications (Ascend950)](../README.md)
