# 动态shape模型用户输入和模型推导结果不匹配

## 问题现象描述

**场景1：**模型执行报错，日志信息中包含以下关键信息：

```bash
[INFO] GE(2284607, ir_build):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task_context.cc:257]2284607 AllocateOutput: To allocate output for node: add2. index = 0, tensor desc = [TensorDescl DataType = 6 , Format = 2 · Shape = [50, ] 
[ERROR] GE(2284607, ir_build):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task_context.cc:257]2284607 AllocateOutput: ErrorNo: 50331649() [LOAD][LOAD][Check][Size] add2(Add) index[0] mem size out of range! Expected size: 128, but given input size: 2. 
```

**场景2：**单算子场景执行报错，日志信息中包含以下关键信息：

```bash
[INFO] GE(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [single op.cc:161]131511 ValidateArgs:lnput [1], aligned_size:96, inputs.length:40, input_sizes_:96 
[INFO] GE(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [single op.cc:186]131511 ValidateArgs:Output [0], aligned_size:3145760, outputs.length:3145728, input_sizes_:18446744073709551615 
[ERROR] GE(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [single op.cc:161]131511 ValidateArgs: ErrorNo: 145000(Parameter invalid.) [FINALI][FlNALl][CheCkl][Param.Outputs]Output Size mismatch. index = 0, model expect  18446744073709551615, but given ....
[ERROR] ASCENDCL(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [op_executor.cpp:68]131511 DoExecteAsync:  [FINALI][FlNALl][Exec][Op]Execute op failed. ge result = 145000
```

## 可能原因

**场景1：**

此处为模型执行时，校验用户分配的output\_buffer大小和模型经过一层层infershape后得到的模型输出的output\_buffer大小不匹配。

**场景2：**

此处为单算子场景执行时，校验用户分配的output\_buffer大小和单算子编译时infershape推出的output\_size大小不匹配。

## 解决措施

针对分析的故障可能原因，可以参考下面步骤处理：

**针对场景1：**

若发生该错误，用户需要检查分配的output\_buffer大小是否正确，应该与模型推导的大小保持一致。建议用户分配的output\_buffer按照上报的ERROR中提示的大小进行分配。

**针对场景2：**

若发生该错误，用户需检查分配的output\_buffer大小和算子infershape提示的size大小是否一致，建议按照报错提示的大小进行分配。
