# Failure in Verifying the Input Size of the Dynamic-Shape Model

## Symptom

The input size of the dynamic-shape model fails to be verified. The plog contains the following key information: "tensor size mismatches. expected: ..., but given ..."

```text
17480:[ERROR] GE(187626,python3):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [execution_engine.cc:450]191154 ValidInputTensor:ErrorNo: 1343225860(Internal errors) [EXEC][EXEC][Check][Size] for [PartitionedCall_14(PartitionedCall)] Input[40]:tensor size mismatches.expected: 768032, but given 32.
```

## Possible Cause

In the dynamic-shape scenario, each node infers the shape during execution. The possible cause is that the shape verification of the operator is invalid.

## Solution

Check the shape source according to the connections in the model and find out the improper shape inference.

Enable the debug-level log. After running the application again, you can search for the following keywords in the plog:

"before\_infershape when running": displays the input and output shape information before operator shape inference.

"after\_infershape when running": displays the input and output shape information after operator shape inference.

Check whether the shape inference result of the current node is correct \(that is, whether the output shape inferred based on the input shape meets the expectation\). If the input shape is incorrect, use the same method to check the shape inference of the input node.

![](figures/image_0000001927835337.png)

>**NOTE:**
>After running the  **export ASCEND\_GLOBAL\_LOG\_LEVEL=0**  command to enable the debug-level log and completing the debugging, run the  **export ASCEND\_GLOBAL\_LOG\_LEVEL=3**  command to enable the error-level log. For details about the log levels, see  [Log Reference](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/maintenref/logreference/logreference_0001.html).
