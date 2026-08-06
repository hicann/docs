# Range

```c
REG_OP(Range)
    .INPUT(start, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_DOUBLE, DT_INT64, DT_BF16}))
    .INPUT(limit, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_DOUBLE, DT_INT64, DT_BF16}))
    .INPUT(delta, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_DOUBLE, DT_INT64, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_DOUBLE, DT_INT64, DT_BF16}))
    .ATTR(is_closed, Bool, false)
    .OP_END_FACTORY_REG(Range)
```

## Brief

Creates a sequence of numbers . 

## Inputs

Three inputs, including:
- start: A 0D tensor (scalar). Acts as first entry in the range if "limit"
  is not "None"; otherwise, acts as range limit and first entry defaults to "0".
  The supported types are:float16, float32, int32, double, int64, bfloat16, format supports ND.
- limit: A 0D tensor (scalar). Upper limit of sequence, exclusive. If "None",
  defaults to the value of "start" while the first entry of the range
  defaults to "0". The supported types are:float16, float32, int32, double, int64, bfloat16, format supports ND.
- delta: A 0D tensor (scalar). Number that increments "start".
  Defaults to "1". The supported types are:float16, float32, int32, double, int64, bfloat16, format supports ND. 

## Outputs

y: A 1D tensor which is the sequence of numbers, format supports ND.
   The supported types are:float16, float32, int32, double, int64, bfloat16. 
   The types of start/limit/delta and output should be the same when the dtypes are:float16, bfloat16, int64. 
   The auto inferred type of output is the same as input when the types of start/limit/delta are the same,
   otherwise the auto inferred type of output is float32. 
   The double type of y is not supported in Ascend950 AI Processor. 
   If the input parameters start, limit, delta are all of type double,
   the output parameters y is only supported as float32 in Ascend950 AI Processor. 

## Attributes

is_closed: An optional attribute of type bool, inducating upper limit is closed or not.
If true, upper limit is closed. If false, upper limit is opened. The default value is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 start: bfloat16,double,float16,float32,int32,int64
- input1 limit: bfloat16,double,float16,float32,int32,int64
- input2 delta: bfloat16,double,float16,float32,int32,int64
- output0 y: bfloat16,float16,float32,int32,int64
### AI CPU
- input0 start: double,float32,int32,int64
- input1 limit: double,float32,int32,int64
- input2 delta: double,float32,int32,int64
- output0 y: double,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator Range or PyTorch operator Range/Arange.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
