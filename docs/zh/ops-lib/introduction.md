# 简介

## 文档定位

本手册主要面向**算子调用**场景，旨在帮助您快速、正确地调用[CANN](https://www.hiascend.com/cann)（Compute Architecture for Neural Networks）内置算子。这些算子经过深度优化，具备良好的硬件亲和性，能够加速网络在AI处理器上的计算。

<!-- npu="950,A3,910b,910,310p,310b" id1 -->
- 如果您需要进行**自定义算子开发或调试**，请参考[《Ascend C算子开发指南》](https://hiascend.com/document/redirect/CannCommunityOpdevAscendC)。
<!-- end id1 -->
- 如果您调用算子过程中出现问题，请参考[《故障处理》](https://hiascend.com/document/redirect/CannCommunitytrouble)进行问题定位和分析。

<!-- npu="950,A3,910b,910,310p,310b" id2 -->
CANN内置算子的源码已在Gitcode [CANN>算子库](https://gitcode.com/cann)项目开放，您可以进一步了解社区生态和算子开发/贡献流程。
<!-- end id2 -->

## 算子库架构

算子库按功能领域进行分类，在CANN架构中的位置以及库之间的依赖关系如[图1](#fig1)所示。算子库分类如下：

- **Math库**：数值计算类算子库，提供不同维度的数值处理与计算算子，例如Add、Abs等，覆盖张量形态变换、基础数学运算、随机数生成等场景。
- **NN库**：神经网络类算子（Neural Network），提供深度学习模型中常见的计算算子，例如卷积、矩阵乘、激活函数、归一化等。
- **CV库**：计算机视觉类算子（Computer Vision），提供图像处理和目标检测算子，例如GridSample等。
- **Transformer库**：大模型计算类算子，提供Transformer核心算子，例如Attention类、LayerNorm类、通算融合类（简称MC2）等。
- **RAS库**：安全维测类算子（Reliability, Availability and Serviceability），提供可靠性、可用性和可维护性等能力，包含安全、加密以及维测相关算子。
- **Opbase库**：所有算子库依赖的基础框架库，提供基础调度能力（如aclTensor创建/释放、workspace复用等）和公共依赖能力。

**图 1**  算子库架构图 <a id="fig1"></a>

![fig1](figures/ops_lib_architecture.png "算子库架构图")

## 什么是算子和算子接口

算子（Operator）是AI计算中的基础函数单元，类似于一个“数学函数”。例如，Add算子用于向量加法，Matmul算子用于矩阵乘法。通过组合这些算子，可以构建出复杂的神经网络模型。

在实际使用中，我们通过算子接口（Operator API）来调用算子。

- **算子**：底层的计算逻辑，例如加法运算、矩阵乘法。
- **算子接口**：算子对外暴露的编程入口。您在Host侧（CPU侧）编写代码时，实际调用的是这些接口，例如aclnn API、PyTorch API等。

**每个算子可能对应一个或多个算子接口**，以aclnn API为例：

- Add算子对应aclnnAdd、aclnnAdds接口。
- MatMulV3算子对应aclnnMatmul、aclnnMatmulWeightNz接口。

## 算子调用方式

CANN算子支持如下调用方式，请根据实际情况选择。

<!-- npu="950,A3,910b,910,310p,310b" id3 -->
- **aclnn API**：针对全量算子提供标准的C API，便于Host侧调用，即单算子API（又称算子Host API）调用方式，调用流程如[图2](#fig2)所示。
<!-- end id3 -->
<!-- npu="950,A3,910b" id4 -->
- **PyTorch API**：针对非PyTorch原生但常见的算子（例如神经网络、大模型类算子），提供了一套兼容PyTorch原生风格的torch\_extension API。该API借助JIT机制（torch.utils.cpp\_extension.load）在首次调用时即时编译C++ Kernel Wrapper，将PyTorch函数桥接到aclnn API。同时，它还通过GE Converter支持TorchAir图模式。
<!-- end id4 -->
- **Ascend IR**（Intermediate Representation）：以构图方式实现算子调用。通过GE（Graph Engine）图引擎将主流AI框架算子统一转换为Ascend IR定义，实现计算图在AI处理器上加速执行。图模式调用原理参见[《图开发指南》](https://hiascend.com/document/redirect/CannCommunityGraphguide)中“编程指南”。

<!-- npu="950,A3,910b,910,310p,310b" id5 -->
**图 2**  aclnn API调用流程 <a id="fig2"></a>

![fig2](figures/aclnn_call_flowchart.png "aclnn调用流程")
<!-- end id5 -->

## 使用向导

本章将为您的算子调用之旅提供全方位指引。作为新手，建议您按照以下路径阅读：

- <span style="display:inline-block;width:20px;height:20px;line-height:20px;text-align:center;border-radius:50%;background:#0057D9;color:#FFF;font-size:13px">1</span> **环境准备**：先查阅[头文件和库文件说明](header_and_library.md)，了解CANN包安装方法，以及调用算子依赖的头文件或库文件。
- <span style="display:inline-block;width:20px;height:20px;line-height:20px;text-align:center;border-radius:50%;background:#0057D9;color:#FFF;font-size:13px">2</span> **概念理解**：通过学习[基本概念](https://gitcode.com/cann/ops-math/blob/master/docs/zh/context/basic_concept.md)熟悉算子的基础术语和关键特性（例如确定性、量化模式等）。
- <span style="display:inline-block;width:20px;height:20px;line-height:20px;text-align:center;border-radius:50%;background:#0057D9;color:#FFF;font-size:13px">3</span> **接口调用**：根据您的业务场景，选择合适的算子调用方式，算子或算子API可参见下表查找。

    <!-- npu="950,A3,910b,910,310p,310b" id6 -->
    **表 1**  算子列表（昇腾AI处理器）

    <table><thead>
      <tr>
        <th>接口分类</th>
        <th>操作指引</th>
        <th>说明</th>
      </tr></thead>
    <tbody>
      <tr>
        <td><b>公共接口</b></td>
        <td><a href="https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/0_aclnn_meta_api.md">公共接口</a></td>
        <td>调用aclnn接口时依赖的公共Meta接口，如创建aclTensor、aclScalar、aclIntArray等。</td>
      </tr>
      <tr>
        <td rowspan="5"><b>算子接口（aclnn）</b></td>
        <td><a href="https://gitcode.com/cann/ops-math/blob/master/docs/zh/menu_aclnn_api.md">Math类接口</a></td>
        <td>数学计算类算子对应的C API，例如Add、Abs等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-nn/blob/master/docs/zh/menu_aclnn_api.md">NN类接口</a></td>
        <td>Neural Network，即神经网络类算子对应的C API，例如Matmul等算子。目前该类算子在整个算子库中占最大比重。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-cv/blob/master/docs/zh/menu_aclnn_api.md">CV类接口</a></td>
        <td>Computer Vision，即计算机视觉类算子对应的C API，例如GridSample等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-transformer/blob/master/docs/zh/menu_aclnn_api.md">Transformer类接口</a></td>
        <td>大模型计算类算子对应的C API，例如FlashAttention、MC2（通算融合）、MoE（Mixture of Experts）等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-ras/blob/master/docs/zh/menu_aclnn_api.md">RAS类接口</a></td>
        <td>安全维测类算子对应的C API。</td>
      </tr>
      <tr>
        <td rowspan="2"><b>算子接口（torch_extension）</b></td>
        <td><a href="https://gitcode.com/cann/ops-nn/blob/master/docs/zh/menu_torch_api.md">NN类接口</a></td>
        <td>针对非PyTorch原生但常见的神经网络类算子，提供PyTorch API，例如Matmul等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-transformer/blob/master/docs/zh/menu_torch_api.md">Transformer类接口</a></td>
        <td>针对非PyTorch原生但常见的大模型类算子，提供PyTorch API，例如FlashAttention、MC2（通算融合）、MoE等算子。</td>
      </tr>
      <tr>
        <td><b>Ascend IR算子原型</b></td>
        <td><a href="ascendIR_op_specification.md">Ascend IR算子规格说明</a></td>
        <td>罗列了基于Ascend IR定义的算子信息。</td>
      </tr>
    </tbody></table>
    <!-- end id6 -->

    <!-- npu="IPV350" id7 -->
    **表 1**  算子列表（IPV350）

    <table><thead>
      <tr>
        <th>接口分类</th>
        <th>操作指引</th>
        <th>说明</th>
      </tr></thead>
    <tbody>
      <tr>
        <td><b>公共接口（暂不支持）</b></td>
        <td><a href="https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/0_aclnn_meta_api.md">公共接口</a></td>
        <td>调用aclnn接口时依赖的公共Meta接口，如创建aclTensor、aclScalar、aclIntArray等。</td>
      </tr>
      <tr>
        <td rowspan="5"><b>算子接口（aclnn）（暂不支持）</b></td>
        <td><a href="https://gitcode.com/cann/ops-math/blob/master/docs/zh/menu_aclnn_api.md">Math类接口</a></td>
        <td>数学计算类算子对应的C API，例如Add、Abs等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-nn/blob/master/docs/zh/menu_aclnn_api.md">NN类接口</a></td>
        <td>Neural Network，即神经网络类算子对应的C API，例如Matmul等算子。目前该类算子在整个算子库中占最大比重。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-cv/blob/master/docs/zh/menu_aclnn_api.md">CV类接口</a></td>
        <td>Computer Vision，即计算机视觉类算子对应的C API，例如GridSample等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-transformer/blob/master/docs/zh/menu_aclnn_api.md">Transformer类接口</a></td>
        <td>大模型计算类算子对应的C API，例如FlashAttention、MC2（通算融合）、MoE（Mixture of Experts）等算子。</td>
      </tr>
      <tr>
        <td><a href="https://gitcode.com/cann/ops-ras/blob/master/docs/zh/menu_aclnn_api.md">RAS类接口</a></td>
        <td>安全维测类算子对应的C API。</td>
      </tr>
      <tr>
        <td><b>Ascend IR算子原型</b></td>
        <td><a href="ascendIR_op_specification.md">Ascend IR算子规格说明</a></td>
        <td>罗列了基于Ascend IR定义的算子信息。</td>
      </tr>
    </tbody></table>
    <!-- end id7 -->

- <span style="display:inline-block;width:20px;height:20px;line-height:20px;text-align:center;border-radius:50%;background:#0057D9;color:#FFF;font-size:13px">4</span> **相关资源**：
  - [附录](appendix/appendix.md)：获取常见算子调用问题（FAQ）、性能优化指南及进阶接口说明。
    - 提供开发aclnn API依赖的nnopbase接口
    - 提供算子开发/调用过程中依赖的op_common公共接口
    - 通过静态Kernel提升算子执行性能
    - 算子调用过程中常见FAQ和案例
  - [《AI框架算子支持清单》](https://hiascend.com/document/redirect/CannCommunityFwOplist)：获取主流AI框架原生IR算子信息（如TensorFlow、Caffe等）。

## 注意事项

- **V版本演进**：算子或算子API可能存在多个V版本，**请优先选择最高V版本**（高版本兼容低版本）。
- **未支持场景**：对于文档中**未声明支持**的场景（如特定产品型号、数据类型、维度等），不推荐开发者使用，暂不能保证调用效果。
<!-- npu="910b,910,310p" id8 -->
- **虚拟化实例**：融合类算子暂不支持该功能。融合类算子是指由多个独立基础“小算子”（如向量Vector、矩阵Cube等）融合而成的复杂算子，其功能与多个小算子等效，而性能通常更优，例如FlashAttention算子。
<!-- end id8 -->
