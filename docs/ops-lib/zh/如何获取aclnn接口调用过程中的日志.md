# 如何获取aclnn接口调用过程中的日志

调用aclnn API过程中，如果出现算子执行失败、精度异常等问题，可以提取Host侧日志辅助分析和判断。一般需要分析如下日志信息：

- plog日志获取：

    程序执行结束后，默认可在`$HOME/ascendc/log`下查看，host日志文件存储路径如下：

    ```text
    $HOME/ascend/log/debug/plog/plog-pid_*.log
    ```

    开启环境变量ASCEND\_SLOG\_PRINT\_TO\_STDOUT可以将log日志直接打屏显示（1表示开启打屏，0表示关闭打屏），配置示例如下：

    ```bash
    export ASCEND_SLOG_PRINT_TO_STDOUT=1
    ```

    日志相关介绍参见[《CANN 日志参考》](https://hiascend.com/document/redirect/CannCommunitylogref)，环境变量介绍参见[《CANN 环境变量》](https://hiascend.com/document/redirect/CannCommunityEnvRef)。

- aclnn异常错误信息获取：

    通过aclGetRecentErrMsg接口获取aclnn接口调用过程中的异常信息，使用方法如下：

    ```cpp
    printf(aclGetRecentErrMsg());
    ```

    打印错误信息样例如下：

    ```text
    [PID:646612] 2026-01-24-11:53:44.671.727 AclNN_Parameter_Error(EZ1001): Expected a proper Tensor but got null for argument addmmTennsor.self.
    ```
