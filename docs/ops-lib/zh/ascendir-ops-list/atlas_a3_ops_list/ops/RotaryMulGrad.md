# RotaryMulGrad

```c
REG_OP(RotaryMulGrad)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .INPUT(r1, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .INPUT(r2, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .ATTR(need_backward, Bool, true)
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .OUTPUT(dr1, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .OUTPUT(dr2, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BFLOAT16}))
    .OP_END_FACTORY_REG(RotaryMulGrad)
```

## Brief

Calculate the inverse gradient of RotaryMul.

## Inputs

- x: A 4-dimensions tensor with layout BNSD, BSND or SBND, where B, N < 1000 and D is multiples of 64.
Must be one of the following types: float16, float, bfloat16. 
- r1: A 4-dimensions tensor with layout 11SD/BNSD, 1S1D/BSND or S11D/SBND, indicates cos value.
When r1 broadcasts to x, the product of the broadcast axes needs to be less than 1024. The dtype must be same as "x". 
- r2: A 4-dimensions tensor with layout 11SD/BNSD, 1S1D/BSND or S11D/SBND, indicates sin value.
Has the same shape and dtype as "r1". 
- dy: A 4-dimensions tensor. Data of grad increment. Has the same shape and dtype as "x".

## Outputs

- dx: A tensor. The grad of input x and has the same shape and dtype as "x".
- dr1: A tensor. The grad of input r1 and has the same shape and dtype as "r1".
- dr2: A tensor. The grad of input r2 and has the same shape and dtype as "r2".

## Attributes

need_backward: An optional bool. Need to calculate dr1 and dr2 when need_backward is "true". Defaults to "true".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 r1: bfloat16,float16,float32
- input2 r2: bfloat16,float16,float32
- input3 dy: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32
- output1 dr1: bfloat16,float16,float32
- output2 dr2: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
