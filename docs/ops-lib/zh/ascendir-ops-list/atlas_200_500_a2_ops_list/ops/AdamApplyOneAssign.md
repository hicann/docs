# AdamApplyOneAssign

```c
REG_OP(AdamApplyOneAssign)
    .INPUT(input0, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(input1, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(input2, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(input3, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(input4, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mul0_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mul1_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mul2_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mul3_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(add2_y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(input1, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(input2, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(input3, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(AdamApplyOneAssign)
```

## Brief

Performs one step of Adam optimizer parameter update, with 10 inputs and 3 outputs. Supports broadcast.

## Inputs

Ten inputs, including:
- input0: A ND Tensor . Must be of type float16, float32.
- input1: A ND Tensor . Must be of type float16, float32.
- input2: A ND Tensor . Must be of type float16, float32.
- input3: A ND Tensor . Must be of type float16, float32.
- input4: A ND Tensor . Must be of type float16, float32.
- mul0_x: A ND Tensor . Must be of type float16, float32.
- mul1_x: A ND Tensor . Must be of type float16, float32.
- mul2_x: A ND Tensor . Must be of type float16, float32.
- mul3_x: A ND Tensor . Must be of type float16, float32.
- add2_y: A ND Tensor . Must be of type float16, float32.

## Outputs

input1: A ND Tensor. Intermediate result: input1 x mul2_x + input0^2 x mul3_x. Type float16, float32.
input2: A ND Tensor. Intermediate result: mul0_x x input2 + mul1_x x input0. Type float16, float32.
input3: A ND Tensor. Parameter update result: input3 - out_input2 / (sqrt(out_input1) + add2_y) x input4. Type
float16, float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input0: float16,float32
- input1 input1: float16,float32
- input2 input2: float16,float32
- input3 input3: float16,float32
- input4 input4: float16,float32
- input5 mul0_x: float16,float32
- input6 mul1_x: float16,float32
- input7 mul2_x: float16,float32
- input8 mul3_x: float16,float32
- input9 add2_y: float16,float32
- output0 input1: float16,float32
- output1 input2: float16,float32
- output2 input3: float16,float32

## Attention Constraints

All input and output data types must be consistent.
The maximum input dimension is 8.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
