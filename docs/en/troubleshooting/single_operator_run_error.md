# Single-operator Running Error

## Analysis Result

If the following conclusion is provided in the  **info.txt**  file, an error is reported during the running of a single operator or the pass is abnormal.

```text
**********************Root cause conclusion******************
Failed to execute the single-operator test case. The operator logic may be incorrect.
```

In this case, you can use the single-operator reproduction method to rectify the fault based on the following information in the  **info.txt**  file. You can also run the  **python3 test\_single\_op.py**  command to view the error information reported during the execution of the abnormal operator and analyze the cause of the error.

1. The following is an example of the operator information provided in  **Basic information** . YYYY-MM-DD-HH:MM:SS.fff.uuu (year-month-day-hour:minute:second.millisecond.microsecond) represents the log output time.

    ```text
    ***********************1. Basic information********************
    error time   : YYYY‑MM‑DD‑HH:MM:SS.fff.uuu
    device id    : 0
    core id      : 0
    task id      : 6
    stream id    : 7
    node name    : GatherV2
    kernel name  : te_gatherv2_657cb48fa1743a43209d7bc779fe8c294760a5b09b3079a3323fdf18376fc408_1
    flip num     :
    kernel file  : te_gatherv2_657cb48fa1743a43209d7bc779fe8c294760a5b09b3079a3323fdf18376fc408_1.o
    json file  : te_gatherv2_657cb48fa1743a43209d7bc779fe8c294760a5b09b3079a3323fdf18376fc408_1.json
    cce file          :
    rts_block_dim     : 8
    driver_aicore_num : 24
    ```

2. The following is an example of the detailed error message provided in  **AICERROR code** .

    ```text
    ***********************2. Ai Core DFX Register***********************
    error code  : 0x10
    CCU_ERR_INFO: 0x2c6290000324442
    ccu_err_addr bit[22:8]=011001001000100  meaning:CCU Error Address [17:3]  approximate:0x19220
    ccu_illegal_instr, Illegal instruction. 1: instruction binary error; 2: instruction address misalignment
    ```

3. The following is an example of the CCE line number provided in  **Instructions** .

    ```text
    ***********************3. Operator Error Line Number************************
    start   pc   : 0x1000124080064000
    current pc   : 0x124080067d2c
    Error occurred most likely at line: 3d08

    /home/HwHiAiUser/tf/info_20230609065654/aicerror_0_20230609065534/te_gatherv2_657cb48fa1743a43209d7bc779fe8c294760a5b09b3079a3323fdf18376fc408_1.o.txt:3d08
    te_gatherv2_657cb48fa1743a43209d7bc779fe8c294760a5b09b3079a3323fdf18376fc408_1.cce:1364
    ....../opp/built-in/op_impl/ai_core/tbe/impl/dynamic/gather_v2.py:1214
    ....../opp/built-in/op_impl/ai_core/tbe/impl/dynamic/gather_v2.py:1214

    related instructions (error occurred before the mark *):

    3d08: <not available>
    3d0c: <not available>
    3d10: <not available>
    3d14: <not available>
    3d18: <not available>
    3d1c: <not available>
    3d20: <not available>
    3d24: <not available>
    3d28: <not available>
    *   3d2c: <not available>

    For complete instructions, please view /home/tf/info_20230609065654/aicerror_0_20230609065534/te_gatherv2_657cb48fa1743a43209d7bc779fe8c294760a5b09b3079a3323fdf18376fc408_1.o.txt
    ```

## Fault Root Causes

The possible causes are as follows:

- The logic of the operator is incorrect. For example, some unallocated addresses are read or written.
- The compiler is incorrect. The logic of the operator is correct, but the compiler compiles the operator into an incorrect bottom-layer assembly instruction. As a result, the chip reports an AI Core error.
- The input data is incorrect. Generally, the input data is used as the index input. Incorrect indexes cause unauthorized access to operators.
- The TilingData data computation or selection is incorrect.

## Solution

This type of problem can be located and handled by reproducing a single operator.

After  **msaicerr.py**  is executed for analysis, the  **info\_\{_timestamp_\}/debug\_info.txt**  file and the abnormal operator test script  **info\_\{_timestamp_\}/aicerror\_\{_number_\}\_\{_timestamp_\}/test\_single\_op.py**  are generated in the same directory where  **msaicerr.py**  is executed.

In the  **debug\_info.txt**  file, run the command \(as shown in the following example\) of the abnormal operator test script, and then execute the script to reproduce the AI Core error.

```text
Run 'export PYTHONPATH=/usr/local/Ascend/CANN-7.3/tools/msaicerr/:$PYTHONPATH;cd /usr/local/Ascend/CANN-7.3/tools/msaicerr;python3 /home/xxxxxxx/xxx/info_xxxx/aicerror_xxxx/test_single_op.py' can test op!
```

>**NOTE:**
>You need to collect the analysis result of  **msaicerr.py**  \(all files in the  **info\__timestamp_**  directory\). If the fault cannot be located or rectified based on these files, submit an issue at  [https://gitee.com/ascend](https://gitee.com/ascend)  for help.
