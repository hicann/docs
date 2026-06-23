# 查找量化场景下的精度损失层

当前**仅支持Caffe**框架模型，使用精度比对工具查找量化场景下的精度损失层，主要包含以下两步的比对：

1. **定位量化阶段的精度问题**。

    执行非量化原始模型（GPU/CPU） vs 量化原始模型（GPU/CPU）。

2. **定位模型转换阶段产生的精度问题**，即量化离线模型在NPU上运行时的精度问题。

    执行量化原始模型（GPU/CPU） vs 量化离线模型（关闭融合规则）（NPU）。

**详细操作请参见**[《精度调试工具》](https://hiascend.com/document/redirect/CannCommunityToolAccucacy)中的“GPU/CPU vs NPU（Caffe离线推理）”。
