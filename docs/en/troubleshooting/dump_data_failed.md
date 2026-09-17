# Data Dump Failure

## Analysis Result

If the  **info.txt**  file contains the following analysis conclusion, a data dump failure occurs:

```text
"**********************Root cause conclusion******************"
The input/output memory address of the operator is abnormal (or the original dumped data fails). Check the framework or application.
```

In addition, the following information is displayed in  **Dump info**  in the  **info.txt**  file:

```text
***********************5. Operator Dump File Parsing*************************
tiling data in int32: [1, 1, 64, 1, 2, 1, 1]
tiling data in int64: Cannot decode in this dtype
tiling data in float16: [5.960464477539063e-08, 0.0, 5.960464477539063e-08, 0.0, 3.814697265625e-06, 0.0, 5.960464477539063e-08, 0.0, 1.1920928955078125e-07, 0.0, 5.960464477539063e-08, 0.0, 5.960464477539063e-08, 0.0]

Failed to get dump data of error op!
```

## Fault Root Causes

After an AI Core error occurs, the framework attempts to dump data based on the input/output address and size in the error callback for developers to locate the fault. If the dump fails, it can be inferred that the input/output address of the operator is incorrect: the AI Core cannot read the address, causing the AI Core error. In addition, the dump function in the error callback cannot read the address, causing the dump data failure.

## Solution

If the preceding information is displayed, perform the following operations:

View the input/output address in  **4. Operator Input/Output Memory**  in the  **info.txt**  file and check whether the operator is the first operator in inference.

If the operator is the first operator for inference, view the user inference script to check whether sufficient address space is allocated to the network. If it is not the first operator, contact technical support to analyze the source of the incorrect address.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.

```text
****************4. Operator Input/Output Memory*******************
input[0] addr: 0x1240c0047000 end_addr:0x1240c0047100 size: 0x100
input[1] addr: 0x1240c0027000 end_addr:0x1240c0027008 size: 0x8
input[2] addr: 0x1240c0037000 end_addr:0x1240c0037004 size: 0x4
output[0] addr: 0x1240c0057000 end_addr:0x1240c0057008 size: 0x8
```
