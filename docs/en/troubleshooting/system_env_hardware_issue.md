# System Environment/Hardware Problems

## Analysis Result

If the following analysis conclusion is provided in the  **info.txt**  file, the fault is generally caused by the system environment or hardware.

```text
"**********************Root cause conclusion******************"
Failed to execute the built-in sample operator. Check the environment.
```

## Fault Root Causes

When the msaicerr tool is used for analysis, a benchmark operator runs. The benchmark operator does not perform complex calculation and it only calls vector instructions, cube instructions, and instructions for movement from GM to UB, from UB to GM, and from UB to UB. These instructions are necessary for the minimum process of an operator. In normal cases, the operator can run properly. If the information in the analysis result is displayed, the benchmark operator fails to run, and the system environment or hardware functions are abnormal.

>**NOTE:**
>Generally, the first operator on the network reports an AI Core error.

## Solution

Use the  [MindCluster ToolBox](https://www.hiascend.com/en/software/mindx-dl)  to check whether the system environment or hardware is normal. If the fault persists, submit the fault information collected by the asys tool and the analysis result file of the msaicerr tool at  [https://gitee.com/ascend](https://gitee.com/ascend)  for help.
