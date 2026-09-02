# FusionVirtualOpSetSwitch

## 融合模式

控制执行split\_n轴优化和split\_c\_to\_n轴优化的开关。将符合约束条件的Split类算子\(SplitD/SplitVD\)添加no\_task属性，通过N轴拼接操作跳过算子编译流程，从而提升性能。如果Split类算子输入的内存过大，可以选择关闭该融合规则。

该融合比较特殊，生效情况不会写进fusion\_result.json。

对比当前图ge\_onnx\_\*\*\*\*PreRunAfterOptimizeGraphBeforeBuild.pbtxt和前一张图ge\*.pbtxt中的SplitD/SplitVD的"\_no\_task"属性变化，由0-\>1表示pass生效。

>[!NOTE]说明 
> 如上.pbtxt文件的生成，需要在执行训练或者推理之前设置如下环境变量。更多环境变量信息请参见《[环境变量参考](https://gitcode.com/cann/docs/blob/master/docs/zh/env-vars/README.md)》。
> 
> - DUMP\_GE\_GRAPH=2 //把整个流程中各个阶段的图描述信息打印到文件中，此环境变量控制dump图的内容多少。
> 
> - DUMP\_GRAPH\_LEVEL=2 //把整个图编译流程中各个阶段的图描述信息打印到文件中。此环境变量控制图落盘的个数。

## 使用约束

**通用约束**

- 不支持动态场景。
- 当SplitD/SplitVD上"\_input\_memory\_type"和"\_output\_memory\_type"属性列表中含有RT\_MEMORY\_L1\(65536\)或RT\_MEMORY\_L2\(131072\)数值时，该融合规则不生效。
- 不支持如下输入。
    - Data-\>TransData/Reshape-\>Split结构。
    - SplitD/SplitVD对端输入节点已有no\_task属性。
    - SplitD/SplitVD对端输入节点已有"atomic\_output\_index"属性且值非空。
    - SplitD/SplitVD对端输入节点是Const。

- 不支持如下输出。
    - SplitD/SplitVD对端输出节点包括NetOutput/HcomBroadcast/HcomAllGather/HcomAllReduce/HcomReduceScatter/HcomReduce/SplitD/SplitVD。
    - SplitD/SplitVD对端输出节点已有no\_task属性。
    - SplitD/SplitVD对端输出节点不是TVM算子\("imply\_type"属性不为1\)。
    - SplitD/SplitVD对端输出节点"\_fusion\_virtual\_op"属性不为空。
    - SplitD/SplitVD对端输出节点"continuous\_input"属性为true。
    - SplitD/SplitVD对端输出节点已有"atomic\_output\_index"属性且值非空。

**除了满足如上通用约束，split\_n轴优化还需要满足如下特殊约束：**

- 当split\_dim属性为0时，该融合规则生效。如下特殊场景会对原始的split\_dim进行转换，split\_dim属性以转换后的为准。
- SplitD/SplitVD为ND-\>NZ格式且shape dim为2场景下，AI处理器会对split\_dim进行转换（0转换成1或者1转换成0）。
- 对于所有格式的SplitD/SplitVD，如果原始的split\_dim为负值，AI处理器会将其转换，转换后的split\_dim值=原始的split\_dim值+shape的维度值。例如split\_dim为-2，shape为\[1,32,32,1\]，shape的dim为4，split\_dim转换后为2。

**除了满足如上通用约束，split\_c\_to\_n轴优化还需要满足特殊约束：**

SplitD/SplitVD上split\_dim属性为1，SplitD/SplitVD的origin shape维度大于或等于2，并且N轴为1（shape\[0\]=1）时，还需要满足如下条件之一，该融合规则生效。

>[!NOTE]说明 
>如果原始的split\_dim为负值，AI处理器会将其转换，转换后的split\_dim值=原始的split\_dim值+shape的维度值。例如split\_dim为-2，shape为\[1,32,32,1\]，shape的dim为4，split\_dim转换后为2。

- 原始format为ND，当前format为NZ且origin shape维度大于或等于4。
- 原始format为NCHW，当前format为NC1HWC0，C轴（shape\[1\]）按照对应dtype对齐，fp16格式按照16位对齐，int8按照32位对齐，int4按照64位对齐。
- 原始format和当前format一致。
