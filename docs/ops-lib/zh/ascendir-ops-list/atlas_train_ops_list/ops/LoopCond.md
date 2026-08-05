# LoopCond

```c
REG_OP(LoopCond)
    .INPUT(x, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(LoopCond)
```

## Brief

Forwards the input to the output. This op represents the loop
      termination condition .

## Inputs

x: A boolean scalar. The condition of the Switch op . 

## Outputs

y: The tensor "x" . 
@see Switch()

## Third-party framework compatibility

Compatible with the TensorFlow operator LoopCond.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
