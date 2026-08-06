# PlaceHolder

```c
REG_OP(PlaceHolder)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(peerIndex, Int, 0) // the index of the corresponding 'end' node it's connected to
    .ATTR(parentId, String, "")     // check if these node are from save parent node
    .ATTR(parentOpType, String, "") // op type of original node
    .ATTR(anchorIndex, Int, 0)  // check if these node are from save anchor
    .OP_END_FACTORY_REG(PlaceHolder)
```

## Brief

Inserts a placeholder for a tensor that will be always fed. 

## Inputs

x: A tensor. 

## Outputs

y: The created placeholder tensor. 

## Attributes

- peerIndex: An integer type. The index of the corresponding "end" node connected to.
- parentId: A string, used to check if the nodes are from the saved parent node.
- parentOpType: A string. Op type of the original node.
- anchorIndex: An integer, used to check if the node is from the saved anchor.

## Third-party framework compatibility

Compatible with the TensorFlow operator PlaceHolder.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
