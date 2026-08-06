# RecordInput

```c
REG_OP(RecordInput)
    .OUTPUT(records, TensorType({DT_STRING}))
    .REQUIRED_ATTR(file_pattern, String)
    .ATTR(file_random_seed, Int, 301)
    .ATTR(file_shuffle_shift_ratio, Float, 0)
    .ATTR(file_buffer_size, Int, 10000)
    .ATTR(file_parallelism, Int, 16)
    .ATTR(batch_size, Int, 32)
    .ATTR(compression_type, String, "")
    .OP_END_FACTORY_REG(RecordInput)
```

## Brief

Emits randomized records. 

## Outputs

records: A Tensor of type string. 

## Attributes

- file_pattern: A string. Glob pattern for the data files.
- file_random_seed: An optional int. Defaults to 301. Random seeds used to
produce randomized records.
- file_shuffle_shift_ratio: An optional float. Defaults to 0. Shifts the
list of files after the list is randomly shuffled.
- file_buffer_size: An optional int. Defaults to 10000. The randomization
shuffling buffer.
- file_parallelism: An optional int. Defaults to 16. How many sstables are
opened and concurrently iterated over.
- batch_size: An optional int. Defaults to 32. The batch size.
- compression_type: An optional string. Defaults to "". The type of
compression for the file. Currently ZLIB and GZIP are supported. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 records: string

## Third-party framework compatibility

Compatible with tensorflow RecordInput operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
