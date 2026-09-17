# Abnormal Operator Input/Output Data Addresses

## Analysis Result

If the  **info.txt**  file contains the following analysis conclusion, an invalid address error generally occurs:

```text
"**********************Root cause conclusion******************"
The input/output memory address of the operator is abnormal (or the original dumped data fails). Check the framework or application.
```

In addition, the following information is displayed in  **4. Operator Input/Output Memory**  in the  **info.txt**  file:

```text
****************4. Operator Input/Output Memory*******************
*[ERROR]input[1] is out of range
*[ERROR]input[2] is out of range

input[0] addr: 0x124080042000 end_addr:0x124080042100 size: 0x100
input[1] addr: 0xaaaaaaaa end_addr:0xaaaaaab2 size: 0x8
input[2] addr: 0x0 end_addr:0x4 size: 0x4
output[0] addr: 0x124080052000 end_addr:0x124080052008 size: 0x8
arg[4][0x1240003E5070] cannot find alloc log, if it is not tiling_gm, please check
arg[2][0x0] cannot find alloc log, if it is not tiling_gm, please check
workspace_bytes:0
```

## Fault Root Causes

The msaicerr tool checks the logs related to the addresses in which memories are allocated and freed on the device, and determines the available memory address range by calculating the difference set of the two values. If the input and output addresses are not within the range, an error is reported.

## Solution

If the address is invalid, check whether the operator address is valid. The options are:

1. If the error occurs in the input/output of an offline inference graph or single-operator call, the address space requested in the user application is incorrect. In this case, check the application source code.
2. In other cases, the error occurs generally because the address space requested by the framework is abnormal. You need to prepare the fault information collected by the asys tool and the analysis result files of the msaicerr tool, and then contact technical support for check and locating.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
