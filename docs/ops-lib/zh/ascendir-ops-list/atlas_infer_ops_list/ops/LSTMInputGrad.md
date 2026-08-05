# LSTMInputGrad

```c
REG_OP(LSTMInputGrad)
    .INPUT(w, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(init_c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(c, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(dh, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(dc, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(i, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(j, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(f, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(o, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(tanhct, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dh_prev, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dc_prev, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(dgate, TensorType({DT_FLOAT16}))
    .OP_END_FACTORY_REG(LSTMInputGrad)
```

## Brief

: LSTMInputGrad calculation.

## Inputs

eleven inputs:
- w:A 4D Tensor. Must be one of the following types: float16, float32.
- init_c:A 4D Tensor.
Must be one of the following types: float16, float32.
- c:A 4D Tensor. Must be one of the following types: float16, float32.
- dy:A 4D Tensor. Must be one of the following types: float16, float32.
- dh:A 4D Tensor. Must be one of the following types: float16, float32.
- dc:A 4D Tensor. Must be one of the following types: float16, float32.
- i:A 4D Tensor. Must be one of the following types: float16, float32.
- j:A 4D Tensor. Must be one of the following types: float16, float32.
- f:A 4D Tensor. Must be one of the following types: float16, float32.
- o:A 4D Tensor. Must be one of the following types: float16, float32.
- tanhct:A optional 4D Tensor.
Must be one of the following types: float16, float32.  

## Outputs

four outputs:
- dx:A 4D Tensor. Must be one of the following types: float16, float32.
- dh_prev:A 4D Tensor.
Must be one of the following types: float16, float32.
- dc_prev:A 4D Tensor.
Must be one of the following types: float16, float32.
- dgate:A 4D Tensor. Must be one of the following types: float16.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 w: float16
- input1 init_c: float16
- input2 c: float16
- input3 dy: float16
- input4 dh: float16
- input5 dc: float16
- input6 i: float16
- input7 j: float16
- input8 f: float16
- input9 o: float16
- input10 tanhct: float16
- output0 dx: float16
- output1 dh_prev: float16
- output2 dc_prev: float16
- output3 dgate: float16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
