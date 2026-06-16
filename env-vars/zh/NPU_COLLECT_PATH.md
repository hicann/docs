# NPU_COLLECT_PATH

## 功能描述

在复现问题场景下，使用该环境变量指定故障信息（包括dump图、AI Core算子异常数据、算子编译信息等）的保存路径，可配置为绝对路径或相对路径（此处是相对执行程序或命令的路径），执行用户需对该路径具有读、写、可执行权限，若路径不存在，系统会自动创建该路径中的目录。

**注意**，使用该环境变量需关注以下事项：

- 设置该环境变量，默认自动开启异常算子dump数据采集功能。如果算子输入或输出包含用户的敏感信息，则存在信息泄露风险。
- 设置该环境变量之后转换模型，在编译om模型时会增加调试信息，导致om模型文件增大，若关注内存规划或内存资源有限时，则在调试完成后及时删除该环境变量。
- 设置该环境变量，仅收集L1 exception dump信息，不收集模型Dump信息、单算子Dump信息、溢出算子Dump信息、L0 exception dump信息。

    L1 exception dump信息存放目录的优先级从高到低依次为：NPU_COLLECT_PATH -\> ASCEND_WORK_PATH -\> 默认路径（指执行程序的当前路径的extra-info目录）

    L1 exception dump是普通exception dump，L0 exception dump是Lite exception dump（即轻量化的exception dump），两者都会导出算子输入&输出、workspace数据等信息，但相比L0 exception dump，L1 exception dump的信息更多，开启L1 exception dump时，会在Host应用类日志文件（即plog日志）中打印出各tensor的dtype等信息，还会把算子相关的算子名、kernel都打印出来。

- 设置该环境变量，模型编译时会在线编译算子，不再使用已编译好的算子二进制文件。

    在线编译的算子信息（.o和.json文件）存放目录的优先级从高到低依次为：NPU_COLLECT_PATH -\> ASCEND_CACHE_PATH -\> 默认路径（指$\{HOME\}/atc_data目录）

## 配置示例

```bash
export NPU_COLLECT_PATH=$HOME/demo/
```

## 使用约束

- 当调用单算子API（例如aclnn类API）时，会使用已编译好的算子二进制文件，不涉及在线编译算子。
- 若配置NPU_COLLECT_PATH环境变量，图模式下，涉及以下算子，在该环境变量指定的路径下无法生成算子编译文件，包括.o和.json文件。

    MatMulAllReduce

    MatMulAllReduceAddRmsNorm

    AllGatherMatMul

    MatMulReduceScatter

    AlltoAllAllGatherBatchMatMul

    BatchMatMulReduceScatterAlltoAll

- 若配置NPU_COLLECT_PATH环境变量，不支持打开“检测Global Memory是否内存越界”的开关，否则编译出来的模型文件或算子kernel包在使用时会报错。打开“检测Global Memory是否内存越界”的开关有以下方式：
    - 使用ATC模型转换工具时，在--op_debug_config参数指定的配置文件中配置oom，详细配置请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。
    <!-- npu="950,A3,910b,910,310p,310b" id1 -->
    - 使用op_compiler算子编译工具时，在--op_debug_config参数指定的配置文件中配置oom，详细配置请参见[《算子编译工具》](https://hiascend.com/document/redirect/CannCommunityopcompiler)。
    <!-- end id1 -->
    - 使用Ascend Graph方式构图时，在op_debug_config或OP_DEBUG_CONFIG参数指定的配置文件中配置oom，详细配置请参见《图开发》。
    - 基于TensorFlow的Python API开发的训练脚本迁移到AI处理器上执行训练时，将op_debug_config参数指定的配置文件中配置oom，详细配置请参见[《TensorFlow 1.15模型迁移》](https://hiascend.com/document/redirect/canncommercial-tfmigr115)、[《TensorFlow 2.6.5模型迁移》](https://hiascend.com/document/redirect/canncommercial-tfmigr26)。
