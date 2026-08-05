# TransDataRNN

```c
REG_OP(TransDataRNN)
    .INPUT(src, TensorType::BasicType())
    .OUTPUT(dst, TensorType::BasicType())
    .REQUIRED_ATTR(src_format, String)
    .REQUIRED_ATTR(dst_format, String)
    .REQUIRED_ATTR(input_size, Int)
    .REQUIRED_ATTR(hidden_size, Int)
    .OP_END_FACTORY_REG(TransDataRNN)
```

## Brief

TransDataRNN is specifically designed for format conversion during the RNN calculation process and will not be used alone. 
| src_format ===> dst_format | dtype            | src_shape ===> dst_shape                                                                                                                             |
| :------------------------: |----------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------: |
| ND ====> FRACTAL_ZN_RNN    | float16          | (input_size + hidden_size, n * hidden_size) ==> (align(input_size, 16) / 16 + align(hidden_size, 16) / 16, n * align(hidden_size, 16) / 16, 16, 16)  |
| ND ====> FRACTAL_ZN_RNN    | float16          | (input_size, n * hidden_size) ==> (align(input_size, 16) / 16 , n * align(hidden_size, 16) / 16, 16, 16)                                             |
| ND ====> FRACTAL_ZN_RNN    | float16          | (hidden_size, n * hidden_size) ==> (align(hidden_size, 16) / 16 , n * align(hidden_size, 16) / 16, 16, 16)                                           |
| FRACTAL_ZN_RNN ====> ND    | float16          | (align(input_size, 16) / 16 + align(hidden_size, 16) / 16, n * align(hidden_size, 16) / 16, 16, 16) ==> (input_size + hidden_size, n * hidden_size)  |
| FRACTAL_ZN_RNN ====> ND    | float16          | (align(input_size, 16) / 16 , n * align(hidden_size, 16) / 16, 16, 16) ==> (input_size, n * hidden_size)                                             |
| FRACTAL_ZN_RNN ====> ND    | float16          | (align(hidden_size, 16) / 16 , n * align(hidden_size, 16) / 16, 16, 16) ==> (hidden_size, n * hidden_size)                                           |
| ND ====> ND_RNN_BIAS       | float16, float32 | (n * hidden_size) ==> (n * align(hidden_size, 16))                                                                                                   |
| ND_RNN_BIAS ====> ND       | float16, float32 | (n * align(hidden_size, 16)) ==> (n * hidden_size)                                                                                                   |
| FRACTAL_ZN_RNN ====> NHWC  | float16          | (align(input_size, 16) / 16 + align(hidden_size, 16) / 16, n * align(hidden_size, 16) / 16, 16, 16) ==> (input_size + hidden_size, n * hidden_size)  |
| FRACTAL_ZN_RNN ====> NHWC  | float16          | (align(input_size, 16) / 16 , n * align(hidden_size, 16) / 16, 16, 16) ==> (input_size, n * hidden_size)                                             |
| FRACTAL_ZN_RNN ====> NHWC  | float16          | (align(hidden_size, 16) / 16 , n * align(hidden_size, 16) / 16, 16, 16) ==> (hidden_size, n * hidden_size)                                           |
In the above table, n represents the number of gates, align(input_size, 16) represents input_size align up to 16, and align(hidden_size, 16) represents hidden_size align up to 16. 

## Inputs

src: A Tensor. Must be one of the following types: float16, float32.

## Outputs

dst: A Tensor. Has the same type as "src".

## Attributes

- src_format: A required string source data format,
can be "ND", "ND_RNN_BIAS", "FRACTAL_ZN_RNN".
- dst_format: A required string target data format,
can be "ND", "ND_RNN_BIAS", "FRACTAL_ZN_RNN", "NHWC".
- input_size: A required int32 identifying the size of input layer, and the value is supposed to be greater than 0.
- hidden_size: A required int32 identifying the size of hidden layer, and the value is supposed to be greater than 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 src: float16,float32
- output0 dst: float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
