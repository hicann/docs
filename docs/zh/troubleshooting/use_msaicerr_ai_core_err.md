# 使用msaicerr工具分析AI Core Error问题

msaicerr工具的功能及约束请参见[msaicerr工具功能及约束](https://gitcode.com/cann/oam-tools/blob/master/docs/zh/msaicerr/msaicerr_functions_and_restrictions.md)，环境准备请参见[msaicerr工具环境准备](https://gitcode.com/cann/oam-tools/blob/master/docs/zh/msaicerr/msaicerr_environment_preparation.md)。

## 操作步骤

1. 以运行用户登录Host服务器。
2. 使用**msaicerr工具快速定位AI Core Error问题的关键原因**。

    进入“$\{Toolkit包安装路径\}/tools/msaicerr”目录，根据[收集AI Core Error问题信息](collect_ai_core_error_info.md)中收集的信息，执行以下命令提取AI Core Error问题相关的关键信息。以下命令中_aic\_err\_info\_timestamp_为_存放AI Core Error问题信息的目录__，_请根据实际情况替换。

    ```bash
    python3 msaicerr.py -p ${HOME}/aic_err_info_timestamp -out $HOME/result
    ```

    以上命令示例中，通过-p参数指定存放故障信息的目录，例如此处为_$\{HOME\}/aic\_err\_info\_timestamp；_通过-out参数指定解析结果文件的存放路径，例如此处为_$HOME/__result_，如果不指定，则解析结果默认存放在执行命令的当前路径下。

    **注意**：不能进入-p参数指定的目录或子目录下执行msaicerr工具，例如此处不能进入到_aic\_err\_info\_timestamp_目录或其子目录中执行msaicerr工具；-out参数指定的目录也不能为-p参数指定的目录或子目录。否则，会出现工具解析卡住或失败的情况。

    执行命令后，用户根据终端界面提示的info.txt文件所在的路径，通过info.txt文件中的提示信息进行问题分析和定位，重点关注下表所示的关键信息。若[收集AI Core Error问题信息](collect_ai_core_error_info.md)中收集的信息中存在多个AI Core Error问题，则msaicerr工具按日志时间解析第一次出现的AI Core Error问题。

    **表 1**  关键信息

    | 关键信息 | 问题原因 | 典型案例及处理方法 |
    | --- | --- | --- |
    | Failed to execute the built-in sample operator. Check the environment. | 环境异常。 | [系统环境/硬件问题](system_env_hardware_issue.md) |
    | Failed to execute the single-operator test case. The operator logic may be incorrect. | 单算子实现异常或编译过程异常。<br>根据提示信息分析是用户自定义算子，还是cann内置算子。<br>查看debug_info.txt文件中的如下提示，表示工具自动生成了单算子用例脚本，您可以执行该脚本复现单算子问题，根据提示排查问题，如果复现不了问题或者排查不出问题，请联系技术支持。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。<br>Run 'export PYTHONPATH=/usr/local/Ascend/CANN-7.3/tools/msaicerr/:$PYTHONPATH;cd /usr/local/Ascend/CANN-7.3/tools/msaicerr;python3 /home/xxxxxxx/xxx/info_xxxx/aicerror_xxxx/test_single_op.py' can test op! | [单算子运行报错](single_operator_run_error.md) |
    | Atomic add has a precision overflow. Check the operator precision. Note that if tasks are concurrently executed on the NPU, a false warning may be reported. | 由于精度问题导致溢出。 | [atomic add精度溢出](atomic_add_precision_overflow.md) |
    | The input/output memory address of the operator is abnormal (or the original dumped data fails). Check the framework or application. | 算子输入输出数据地址异常。<br>或者框架分配内存问题，此时需要区分是GE或其它框架，联系技术支持。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。 | [算子输入输出数据地址异常](operator_io_address_abnormal.md)<br>[Dump数据失败](dump_data_failed.md) |
    | If the arguments are inconsistent before and after operator execution, memory access may be out of bounds. You are advised to use the memory error detection model  to locate the fault. | 算子输入输出参数异常。 | [算子输入args下发前后不一致](operator_input_args_inconsistent.md) |
    | The number of AI Cores in the environment is less than that required by the operator. | 环境中的AI Core数量比算子所需的AI Core数量少。 | 请检查使用msaicerr工具的环境与真实出错环境的AI Core数量是否一致，若一致，再联系技术支持处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。 |
    | The memset or atomic_clean operator is not inserted before this operator in the graph, while memory cleanup is required before operator execution. | 构图异常。 | 联系技术支持处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。 |
    | The set_flag and wait_flag instructions are not used together in the operator code. | set_flag和wait_flag指令不匹配。 | CANN内置算子联系技术支持处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。<br>自定义算子用户需自行排查算子代码。 |
    | The single-operator test case is successfully executed. In case of an unknown error mode, you are advised to: (1) check the operator again by using the msSanitizer tool. (2) If out-of-bounds memory access occurs on other operators, you are advised to enable memory error detection with op_debug_config=oom and then check the operators. For details: https://www.hiascend.com/zh/document.<br>(3) For details about the framework, contact technical support. | 单算子复现执行成功。 | 联系技术支持处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。 |
    | Internal error. Contact technical support. | 内部错误。 | 联系技术支持处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。 |
    | The maintenance and test information is insufficient or the format is incorrect, contact technical support. | 维测信息不足或格式错误。根据具体报错信息修改维测数据或格式。 | 联系技术支持处理。您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。 |

    若执行msaicerr工具失败：

    1. 检查使用工具的前提条件是否满足、[收集AI Core Error问题信息](collect_ai_core_error_info.md)中收集的信息是否完整；
    2. 再参见[算子输入args错误](operator_input_args_error.md)排查算子参数问题；
    3. 如果无法定位问题，您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。

    msaicerr工具的其它参数及功能请参见[msaicerr工具功能及约束](https://gitcode.com/cann/oam-tools/blob/master/docs/zh/msaicerr/msaicerr_functions_and_restrictions.md)。
