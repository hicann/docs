# 基本介绍

## 使用前须知

**使用场景**

对于纯静态shape网络或者shape变化较少的动态shape网络，如果您想快速提升网络执行性能，可以在网络部署时通过算子编译工具（op\_compiler）编译生成静态Kernel包来提升算子调用性能。

**调优原理**

静态Kernel编译是指在编译时指定算子shape大小，运行时不需要指定shape大小。算子编译工具根据输入的算子信息统计文件，得到确定的shape信息，针对每一个shape都编译出一个算子二进制，从而实现提升算子执行效率和性能的目的。

静态Kernel编译的优势如下：

- 编译时已知所有tensor的大小，存储空间利用率高。
- 编译时可以针对实际的shape大小做针对性优化。
- AI处理器擅长并行指令运行，不擅长逻辑计算，如果有太多的Scalar操作可能会打断并行指令的运行，从而导致性能下降。静态编译可以在编译时完成标量的计算，一定程度上可以提升性能。
- 编译工具在编译时知道确切的操作数据大小，不会额外插入同步，不会导致并行执行多个指令变成串行执行，一定程度上可以提升性能。

**使用约束**

静态编译模式支持的产品型号：
<!-- npu="310p" id1 -->
- <term>Atlas 推理系列产品</term>
<!-- end id1 -->
<!-- npu="910" id2 -->
- <term>Atlas 训练系列产品</term>
<!-- end id2 -->
<!-- npu="910b" id3 -->
- <term>Atlas A2 训练系列产品/Atlas A2 推理系列产品</term>
<!-- end id3 -->
<!-- npu="950" id4 -->
- <term>Ascend 950PR/Ascend 950DT</term>
<!-- end id4 -->

## 整体流程

**图 1**  使用静态Kernel提升性能的原理图

![fig1](../figures/staticKernel_flowchart.png "使用静态Kernel提升性能的原理图")

通过编译静态Kernel提升网络模型中算子执行性能的基本流程如上图所示，整个调优步骤如下：

1. Dump算子信息。

    对算子调优前，需要先获取网络模型中的算子信息。

    - **方式1**：若采用PyTorch的Python接口编程，通过Ascend PyTorch Profiler接口Dump算子json文件。
    - **方式2**：若采用acl接口，直接调用aclopStartDumpArgs和aclopStopDumpArgs接口Dump算子json文件。

2. 编译静态Kernel包。

    通过**算子编译工具**对Dump的算子信息统计文件（\*.json）进行编译并生成Kernel包。

    > **说明：** 算子编译工具（op\_compiler）是CANN提供的用于进行算子编译生成算子二进制文件的命令行工具。当算子shape固定或者变化较少时，可使用该工具编译静态kernel包并安装，提升算子调用的性能。关于该工具的详细介绍，请参考[《算子编译工具》](https://hiascend.com/document/redirect/CannCommunityopcompiler)。

3. 安装静态Kernel包。

    将静态Kernel包上传到目标网络模型运行的服务器上，直接运行run包完成安装。

4. 模型执行效果验证。

    安装静态Kernel包后，重新运行目标网络模型，比较安装静态Kernel包和未安装静态Kernel包的整网运行性能和单算子运行耗时。
