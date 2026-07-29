# ASCEND_WORK_PATH

## 功能描述

若开发者期望编译运行过程中产生的文件落盘到归一路径，可通过此环境变量设置**单机独享文件**的存储路径，各组件编译运行过程中产生的单机独享文件会存储到此环境变量定义的路径中。

- 路径支持大小写字母（a-z，A-Z）、数字（0-9）、下划线（_）、中划线（-）、句点（.）、中文字符。
- 若指定的路径存在且有效，请确保执行用户具有读、写、执行权限；若指定的路径不存在，软件会自动创建。

**${ASCEND_WORK_PATH}路径下的文件包括：**

- **${ASCEND_WORK_PATH}/aoe_data/**：记录AOE调优过程中的相关信息，包括调优任务名称、调优耗时、调优前后的模型执行时间/算子执行时间、知识库命中信息等。

  优先级说明：

  ASCEND_WORK_PATH > AOE默认调优工作目录
  
  AOE默认调优工作目录为：\${install_path}/latest/tools/aoe/conf/aoe.ini中“WORK_PATH”参数的取值。

  <!-- npu="950,A3,910b,910,310p,310b" id2 -->
- **${ASCEND_WORK_PATH}/log/**：日志文件。

  优先级说明：

  ASCEND_PROCESS_LOG_PATH > ASCEND_WORK_PATH > 日志默认存储路径（$HOME/ascend/log）
  <!-- end id2 -->

- **${ASCEND_WORK_PATH}/atrace/**：trace日志文件。

  优先级说明：

  ASCEND_WORK_PATH > trace日志默认存储路径（\$HOME/ascend/atrace）

- **${ASCEND_WORK_PATH}/profiling_data/**：Profiling工具收集到的性能数据的存放路径。

  优先级说明：

  离线推理场景：
  
  - 若通过`msprof`命令采集性能数据，优先级如下：

    `--output参数` > ASCEND_WORK_PATH > 默认路径（推理执行的模型文件存储路径）
  - 若通过`acl.json`配置文件方式采集性能数据，优先级如下：

    配置参数“output” > ASCEND_WORK_PATH > 默认路径（应用工程可执行文件所在目录）
  
  <!-- npu="950,A3,910b,910,310p" id3 -->
  TensorFlow训练/在线推理场景：
  
  PROFILING_OPTIONS环境变量中的“output”参数、训练脚本“profiling_options”配置中的“output”参数、训练脚本调用Profiler类配置的“output_path”参数，优先级大于ASCEND_WORK_PATH。
  
  需要注意：训练/在线推理场景下，output/output_path参数与环境变量ASCEND_WORK_PATH二者需要配置一个，否则profiling性能数据采集功能报错。
  <!-- end id3 -->
  
  <!-- npu="A3,910b,910" id4 -->
  PyTorch训练/在线推理场景：
  
  on_trace_ready=tensorboard_trace_handler函数指定的性能数据路径 > ASCEND_WORK_PATH > 默认路径
  
  若配置tensorboard_trace_handler函数后未指定具体路径，可以通过环境变量ASCEND_WORK_PATH设置，此时落盘的性能数据会自动解析；若代码中未使用on_trace_ready=torch_npu.profiler.tensorboard_trace_handler函数，那么通过环境变量ASCEND_WORK_PATH设置并落盘的性能数据为原始数据。
  <!-- end id4 -->

- **${ASCEND_WORK_PATH}/kernel_meta/**：算子编译生成的调试相关的过程文件，包括但不限于算子.o（算子二进制文件）、.json（算子描述文件）、.cce等文件。

  以下场景提供了设置算子编译生成的调试过程文件存储路径的参数或接口，其优先级高于ASCEND_WORK_PATH环境变量，详细描述如下：
  
  - 使用ATC工具进行离线模型编译的场景
  
    参数“--debug_dir” > ASCEND_WORK_PATH  > 默认路径（./当前执行路径）
  
  - 使用AscendCL接口构建或编译模型的场景
  
    - 构图接口"aclgrphBuildInitialize"中参数“DEBUG_DIR” > ASCEND_WORK_PATH  > 默认路径（./当前执行路径）

    - 构图接口"aclgrphBuildModel"中参数“DEBUG_DIR” > ASCEND_WORK_PATH  > 默认路径（./当前执行路径）

    - 应用编译接口“aclCompileOpt”中参数ACL_DEBUG_DIR > ASCEND_WORK_PATH  > 默认路径（./当前执行路径）

    <!-- npu="950,A3,910b,910,310p" id5 -->
  - TensorFlow网络训练或在线推理场景
  
    TF Adapter配置参数“debug_dir” > ASCEND_WORK_PATH  > 默认路径（./当前执行路径）。
    <!-- end id5 -->

- **\$\{ASCEND_WORK_PATH}/\$\{pid}_${device_id}**：开启DUMP图描述信息打印的场景下（即配置环境变量DUMP_GE_GRAPH的场景），会落盘相应的DUMP图文件。

  优先级说明：
  
  环境变量“DUMP_GRAPH_PATH” > ASCEND_WORK_PATH > 默认路径（./当前执行路径）

- **${ASCEND_WORK_PATH}/extra-info/data-dump/**：exception dump文件、异常算子编译信息。
  
  优先级说明：

  环境变量“NPU_COLLECT_PATH” > ASCEND_WORK_PATH > 默认存储路径（当前执行路径）。

- **\$\{ASCEND_WORK_PATH}/tmp_weight_${pid}_${session_id}**：开启权重外置的场景下，此目录下存储Const、Constant节点的权重文件。

  不同场景下开启权重外置的方法不同，具体可参考对应场景的用户指南或开发指南。
  
  优先级说明：

   ASCEND_WORK_PATH > 默认路径（./当前执行路径）

- **\$\{ASCEND_WORK_PATH}/FE/${pid}/fusion_result.json**：除去“fusion_switch.cfg”文件中已关闭的融合规则后，仍然在使用的融合规则。

  优先级说明：

  ASCEND_WORK_PATH > 默认路径（./当前执行路径）

- **${ASCEND_WORK_PATH}/check_result.json**：模型预检结果文件。

  使用ATC工具进行离线模型编译时，当atc命令中的--mode=0且模型解析失败时，或者--mode=3仅做模型预检时，通过该环境变量可指定预检结果文件的保存路径。

  优先级说明：

  参数“--check_report”> ASCEND_WORK_PATH > 默认路径（./当前执行路径）

- **${ASCEND_WORK_PATH}/printf/**：算子Kernel数据Dump的数据文件。

  优先级说明：

  ASCEND_DUMP_PATH > ASCEND_WORK_PATH > 默认路径（当前执行路径）。

## 配置示例

```bash
export ASCEND_WORK_PATH=/repo/task001/172.16.1.12_01_03
```

配置的路径需要为已存在目录，且执行用户具有读、写、执行权限，该路径的最后一段字段需要可唯一标识当前机器。

建议此唯一标识通过machineID、vmID与dockerID拼接组成，如：“machineID_vmID_dockerID”。

- machineID：当前机器的IP地址。
- vmID：虚拟机ID。
- dockerID：Docker容器ID。

如果您是物理机环境，仅通过IP地址标识即可。

## 使用约束

多服务器场景下，各机器上的AI处理器型号以及固件驱动与CANN软件版本需要保持一致。

## 支持的型号

全量芯片支持
