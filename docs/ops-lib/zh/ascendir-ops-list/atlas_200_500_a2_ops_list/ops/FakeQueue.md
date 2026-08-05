# FakeQueue

```c
REG_OP(FakeQueue)
    .INPUT(resource, TensorType({DT_RESOURCE}))
    .OUTPUT(handle, TensorType({DT_STRING}))
    .OP_END_FACTORY_REG(FakeQueue)
```

## Brief

FakeQueue, support tf api FixedLengthRecordReader. 

## Inputs

Including:
resource: A Tensor of type DT_RESOURCE.

## Outputs

handle: A Tensor of type DT_STRING ref. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 resource: resource
- output0 handle: string

## Third-party framework compatibility

Compatible with the TensorFlow operator FakeQueue.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
