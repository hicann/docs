# Using the msaicerr Tool to Analyze AI Core Errors

For details about the functions and restrictions of the msaicerr tool, see  [Functions and Restrictions of the msaicerr Tool](https://gitcode.com/cann/oam-tools/blob/master/docs/en/msaicerr/msaicerr_functions_and_restrictions.md). For details about how to prepare the environment, see  [msaicerr – Tool Environment Preparation](https://gitcode.com/cann/oam-tools/blob/master/docs/en/msaicerr/msaicerr_environment_preparation.md).

## Procedure

1. Sign in to the host server as the running user.
2. Use the msaicerr tool to quickly locate the key causes of AI Core errors.

    Go to the  **_$\{Toolkit installation path\}_/tools/msaicerr**  directory and run the following command to extract key information related to the AI Core error based on the information collected in  [Collecting AI Core Error Information](collect_ai_core_error_info.md). In the following command,  _aic\_err\_info\_timestamp_  indicates the directory for storing AI Core error information. Replace it with the actual directory.

    ```bash
    python3 msaicerr.py -p ${HOME}/aic_err_info_timestamp -out $HOME/result
    ```

    In the preceding command example, the  **-p**  parameter is used to specify the directory for storing fault information, for example,  _$\{HOME\}/aic\_err\_info\_timestamp_. The  **-out**  parameter is used to specify the path for storing the parsing result file, for example,  _$HOME/__result_; if the path is not specified, the parsing result is stored in the current path where the command is executed by default.

    Note: Do not execute the msaicerr tool in the directory specified by the  **-p**  parameter or its subdirectory. For example, you cannot execute the msaicerr tool in the  _aic\_err\_info\_timestamp_  directory or its subdirectory. The directory specified by the  **-out**  parameter must not be the directory specified by the  **-p**  parameter or its subdirectory. Otherwise, the tool parsing may be suspended or fail.

    After the command is executed, you can analyze and locate the fault based on the prompt information in the  **info.txt**  file, the path of which is displayed on the terminal interface. Pay attention to the key information described in the following table. If the information collected in  [Collecting AI Core Error Information](collect_ai_core_error_info.md)  contains multiple AI Core errors, the msaicerr tool parses the AI Core error that occurs for the first time based on the log time.

    **Table  1**  Key information

    | Key Information | Possible Cause | Typical Case and Handling Method |
| --- | --- | --- |
| Failed to execute the built-in sample operator. Check the environment. | The operating environment is abnormal. | [System Environment/Hardware Problems](system_env_hardware_issue.md) |
| Failed to execute the single-operator test case. The operator logic may be incorrect. | Errors occur in single-operator implementation or compilation process.<br>Check whether the operator is a user custom operator or a built-in CANN operator based on the displayed information.<br>If the following information is displayed in the debug_info.txt file, the tool automatically generates a single-operator case script. You can run the script to reproduce the single-operator fault and locate the fault as prompted. If the fault cannot be reproduced or located, contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support.<br>Run 'export PYTHONPATH=/usr/local/Ascend/CANN-7.3/tools/msaicerr/:$PYTHONPATH;cd /usr/local/Ascend/CANN-7.3/tools/msaicerr;python3 /home/xxxxxxx/xxx/info_xxxx/aicerror_xxxx/test_single_op.py' can test op! | [Single-operator Running Error](single_operator_run_error.md) |
| Atomic add has a precision overflow. Check the operator precision. Note that if tasks are concurrently executed on the NPU, a false warning may be reported. | Overflow occurs due to precision problems. | [Accuracy Overflow/Underflow During Atomic Add](atomic_add_precision_overflow.md) |
| The input/output memory address of the operator is abnormal (or the original dumped data fails). Check the framework or application. | The input and output data addresses of the operator are abnormal.<br>Alternatively, a framework memory allocation error occurs. In this case, you need to determine whether it is the GE framework or another framework and contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support. | [Abnormal Operator Input/Output Data Addresses](operator_io_address_abnormal.md)<br>[Data Dump Failure](dump_data_failed.md) |
| If the arguments are inconsistent before and after operator execution, memory access may be out of bounds. You are advised to use the memory error detection model to locate the fault. | The input and output parameters of the operator are abnormal. | [Inconsistent Dispensation Before And After The Operator Input Arg](operator_input_args_inconsistent.md) |
| The number of AI Cores in the environment is less than that required by the operator. | The number of AI Cores in the environment is less than that required by the operator. | Check whether the number of AI Cores in the environment where the msaicerr tool is used is the same as that in the actual environment. If so, contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support. |
| The memset or atomic_clean operator is not inserted before this operator in the graph, while memory cleanup is required before operator execution. | Graph build is abnormal. | Contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support. |
| The set_flag and wait_flag instructions are not used together in the operator code. | The set_flag and wait_flag instructions do not match. | For CANN built-in operators, contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support.<br>For custom operators, check the operator code by yourself. |
| The single-operator test case is successfully executed. In case of an unknown error mode, you are advised to: (1) check the operator again by using the msSanitizer tool. (2) If out-of-bounds memory access occurs on other operators, you are advised to enable memory error detection with op_debug_config=oom and then check the operators. For details: https://www.hiascend.com/zh/document.<br>(3) For details about the framework, contact technical support. | Single-operator reproduction is successful. | Contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support. |
| Internal error. Contact technical support. | An internal error occurs. | Contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support. |
| The maintenance and debugging information is insufficient or the format is incorrect, contact technical support. | The maintenance and debugging information is insufficient or the format is incorrect. Modify the maintenance and debugging data or format based on the specific error information. | Contact technical support. After obtaining the logs, click [here](https://www.hiascend.com/support) to contact technical support. |

    If the msaicerr tool fails to be executed:

    1. Check whether the prerequisites for using the tool are met and whether the information collected in  [Collecting AI Core Error Information](collect_ai_core_error_info.md)  is complete.
    2. Check the operator parameters by referring to  [Operator Input Argument Errors](operator_input_args_error.md).
    3. After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.  Perform this operation if the fault cannot be located.

    For details about other parameters and functions of the msaicerr tool, see  [Functions and Restrictions of the msaicerr Tool](https://gitcode.com/cann/oam-tools/blob/master/docs/en/msaicerr/msaicerr_functions_and_restrictions.md).
