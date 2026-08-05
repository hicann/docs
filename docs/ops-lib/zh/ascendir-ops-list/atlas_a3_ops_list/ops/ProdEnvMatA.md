# ProdEnvMatA

```c
REG_OP(ProdEnvMatA)
    .INPUT(coord, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(type, TensorType({DT_INT32}))
    .INPUT(natoms, TensorType({DT_INT32}))
    .INPUT(box, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(mesh, TensorType({DT_INT32}))
    .INPUT(davg, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(dstd, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(descrpt, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(descrpt_deriv, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(rij, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(nlist, TensorType({DT_INT32}))
    .ATTR(rcut_a, Float, 1.0)
    .ATTR(rcut_r, Float, 1.0)
    .ATTR(rcut_r_smth, Float, 1.0)
    .ATTR(sel_a, ListInt, {})
    .ATTR(sel_r, ListInt, {})
    .OP_END_FACTORY_REG(ProdEnvMatA)
```

## Brief

Calculate ProdEnvMatA.

## Inputs

- coord: A Tensor. Must be one of the following types: float32, float64.
- type: A Tensor. Must be one of the following types: int32.
- natoms: A Tensor. Must be one of the following types: int32.
- box: A Tensor. Must be one of the following types: float32, float64.
- mesh: A Tensor. Must be one of the following types: int32.
- davg: A Tensor. Must be one of the following types: float32, float64.
- dstd: A Tensor. Must be one of the following types: float32, float64.

## Outputs

- descrpt: A Tensor. Must be one of the following types: float32, float64.
- descrpt_deriv: A Tensor. Must be one of the following types: float32,
float64.
- rij: A Tensor. Must be one of the following types: float32, float64.
- nlist: A Tensor. Must be one of the following types: int32.

## Attributes

- rcut_a: An optional float. Defaults to 1.0.
- rcut_r: An optional float. Defaults to 1.0.
- rcut_r_smth: An optional float. Defaults to 1.0.
- sel_a: An optional listInt. Defaults to {}.
- sel_r: An optional listInt. Defaults to {}.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 coord: float32
- input1 type: int32
- input2 natoms: int32
- input3 box: float32
- input4 mesh: int32
- input5 davg: float32
- input6 dstd: float32
- output0 descrpt: float32
- output1 descrpt_deriv: float32
- output2 rij: float32
- output3 nlist: int32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
