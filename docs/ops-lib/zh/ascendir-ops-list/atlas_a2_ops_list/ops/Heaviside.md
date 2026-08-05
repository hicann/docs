# Heaviside

```c
REG_OP(Heaviside)
        .INPUT(input, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .INPUT(values, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OUTPUT(output, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OP_END_FACTORY_REG(Heaviside)
```

## Brief

Apply the heaviside step function element-wise to the input. 

## Inputs

- input: A tensor of type float32, float16 or bfloat16. Shape support 0D ~ 8D.
The format must be ND.
- values: A tensor of type float32, float16 or bfloat16. Shape support 0D ~ 8D.
The format must be ND.

## Outputs

output: A tensor has the same type, shape and format as "input". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input: bfloat16,float16,float32
- input1 values: bfloat16,float16,float32
- output0 output: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
