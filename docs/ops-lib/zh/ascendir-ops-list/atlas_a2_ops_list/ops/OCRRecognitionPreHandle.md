# OCRRecognitionPreHandle

```c
REG_OP(OCRRecognitionPreHandle)
    .INPUT(imgs_data, TensorType({DT_UINT8}))
    .INPUT(imgs_offset, TensorType({DT_INT32}))
    .INPUT(imgs_size, TensorType({DT_INT32}))
    .INPUT(langs, TensorType({DT_INT32}))
    .INPUT(langs_score, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(imgs, TensorType({DT_UINT8}))
    .OUTPUT(imgs_relation, TensorType({DT_INT32}))
    .OUTPUT(imgs_lang, TensorType({DT_INT32}))
    .OUTPUT(imgs_piece_fillers, TensorType({DT_INT32}))
    .ATTR(batch_size, Int, 8)
    .ATTR(data_format, String, "NHWC")
    .ATTR(pad_mode, String, "REPLICATE")
    .OP_END_FACTORY_REG(OCRRecognitionPreHandle)
```

## Brief

batch input x acording to attr batch_size and enqueue.

## Inputs

- imgs_data: A Tensor of type uint8. Multi img data value.
- imgs_offset:A Tensor of type int32. Offset of every img data in input imgs_data.
- imgs_size:A Tensor of type int32. Shape of every img data.
- langs:A Tensor of type int32. Lang of every img data.
- langs_score:A Tensor of type int32. Lang score of every img data.

## Outputs

- imgs: A Tensor of type uint8. Multi imgs data after reconition pre handle.
- imgs_relation: A Tensor of type int32. Output imgs orders in input imgs.
- imgs_lang: A Tensor of type int32. Output batch imgs langs.
- imgs_piece_fillers: A Tensor of type int32. Output batch imgs piece fillers.

## Attributes

- batch_size: An optional int. Defaults to 8. Batch size.
- data_format: An optional string from: '"NHWC", "NCHW"'. Defaults to
"NHWC". Data format.
- pad_mode: An optional string from: '"REPLICATE", "ZERO"'. Defaults to
"REPLICATE". Pad mode.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 imgs_data: uint8
- input1 imgs_offset: int32
- input2 imgs_size: int32
- input3 langs: int32
- input4 langs_score: float16,float32
- output0 imgs: uint8
- output1 imgs_relation: int32
- output2 imgs_lang: int32
- output3 imgs_piece_fillers: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
