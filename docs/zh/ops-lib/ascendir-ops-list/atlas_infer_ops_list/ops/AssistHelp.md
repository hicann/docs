# AssistHelp

```c
REG_OP(AssistHelp)
    .DYNAMIC_INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16,
        DT_UINT8, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE }))
    .DYNAMIC_OUTPUT(y, TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, DT_UINT16,
        DT_UINT8, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE}))
    . REQUIRED_ATTR (func_name, String)
    . OP_END_FACTORY_REG(AssistHelp)
```

## Brief

aicpu assit help op for auxiliary matrix generation. 

## Inputs

x: The input is dynamic for attribute func_name. Must be one of the following types:
float32, float16, int8, int16, uint8, uint16, int32, int64, uint32, uint64, double, bool. 

## Outputs

y: The output is dynamic for attribute func_name. The output type is the same as the x type.

## Attributes

- func_name: An required param, for example "topkv2". Dtype is string.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
