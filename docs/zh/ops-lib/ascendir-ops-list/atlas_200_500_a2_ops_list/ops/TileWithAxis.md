# TileWithAxis

```c
REG_OP(TileWithAxis)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT64, DT_INT32,
    DT_INT16, DT_INT8, DT_UINT64, DT_UINT32, DT_UINT16, DT_UINT8}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT64, DT_INT32,
    DT_INT16, DT_INT8, DT_UINT64, DT_UINT32, DT_UINT16, DT_UINT8}))
    .ATTR(axis, Int, 1)
    .REQUIRED_ATTR(tiles, Int)
    .OP_END_FACTORY_REG(TileWithAxis)
```

## Brief

Extends the input with copies of data along a specified dimension. For example: 
(1) If x = [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], with shape (2, 3, 2); 
(2) axis = 1; 
(3) tiles = 2; 
(4) Then, y = [[[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]], [[7, 8],
[9, 10], [11, 12], [7, 8], [9, 10], [11, 12]]],
with shape (2, 6, 2).

## Inputs

One input:
x: A Tensor with any format. Must be one of the following types:
bfloat16, float16, float32, int8, int16, int32, int64, uint8, uint16, uint32, uint64 . 

## Outputs

y: A Tensor with the same type and format of x. 

## Attributes

- axis: An optional int, specifying the axis to tile. Defaults to 1.
- tiles: A required int, specifying the number of copies (tiles) to output .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- "axis" must be within the rank of the input tensor.
- "tiles" must be greater than 1.

## Third-party framework compatibility

Compatible with the Caffe operator Tile.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
