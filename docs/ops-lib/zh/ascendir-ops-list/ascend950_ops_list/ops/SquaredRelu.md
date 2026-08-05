# SquaredRelu

```c
REG_OP(SquaredRelu)
        .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OP_END_FACTORY_REG(SquaredRelu)
```

## Brief

SquaredRelu first applies ReLU to the input tensor x, and then squares the result of the ReLU operation.

## Inputs

x: A tensor of type float, bf16 or bfloat16. Shape support 0D ~ 8D.
The format must be ND.

## Outputs

y: A Tensor with the same type, shape, format as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core


---

[Back to Operator Specifications (Ascend950)](../README.md)
