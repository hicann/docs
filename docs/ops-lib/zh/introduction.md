# 简介

## 概述

> **须知：**
>
> <!-- npu="950,A3,910b,910,310p,310b" id1 -->
> - 本算子库提供的算子均为CANN内置算子，您可以直接调用；如需自定义算子，请参考[《Ascend C算子开发指南》](https://hiascend.com/document/redirect/CannCommunityOpdevAscendC)完成算子开发。
> <!-- end id1 -->
> - CANN算子源码已在[Gitcode CANN开源项目](https://gitcode.com/cann)开放，您可以进一步了解社区生态或算子开发和贡献流程。

[CANN](https://www.hiascend.com/cann)（Compute Architecture for Neural Networks）提供了一系列丰富且经过深度优化、硬件亲和的高性能算子，可直接应用于AI业务，为网络在AI处理器上的加速计算奠定了基础。

算子库在CANN架构中的位置如[图1](#fig1)所示，主要包含如下算子库：

- **Math库**：数值计算类算子库，提供不同维度的数值处理与计算算子，例如Add、Abs等，覆盖张量形态变换、基础数学运算、随机数生成等场景。
- **NN库**：神经网络类算子（Neural Network），提供深度学习模型中常见的计算算子，例如卷积、矩阵乘、激活函数、归一化等。
- **CV库**：计算机视觉类算子（Computer Vision），提供图像处理和目标检测算子，例如GridSample等。
- **Transformer库**：大模型计算类算子，提供Transformer核心算子，例如Attention类、LayerNorm类、通算融合类（简称MC2）等。
- **Opbase库**：所有算子库依赖的基础框架库，提供基础调度能力（如aclTensor创建/释放、workspace复用等）和公共依赖能力。

**图 1**  算子库架构图 <a id="fig1"></a>

![fig1](figures/算子库架构图.png "算子库架构图")

如需调用算子库中的算子，CANN提供了多种调用方式，请根据实际情况选择。

<!-- npu="950,A3,910b,910,310p,310b" id2 -->
- aclnn API：针对全量算子，提供了一套相应的C API，方便Host侧调用，简称单算子API（或者算子Host API）调用方式，调用流程如[图2](#fig2)所示。
<!-- end id2 -->
<!-- npu="950,A3,910b" id3 -->
- PyTorch API：针对非PyTorch原生但常见的大模型算子，提供了一套兼容PyTorch原生风格的torch\_extension API。该API借助JIT机制（torch.utils.cpp\_extension.load）在首次调用时即时编译C++ Kernel Wrapper，将PyTorch函数桥接到aclnn API。同时，它还通过GE Converter支持TorchAir图模式。
<!-- end id3 -->
- GE图模式调用：通过算子Ascend IR（Intermediate Representation）定义，以构图方式实现算子调用，调用原理参见[《图开发指南》](https://hiascend.com/document/redirect/CannCommunityGraphguide)中“编程指南”，这里不详细阐述。

<!-- npu="950,A3,910b,910,310p,310b" id4 -->
**图 2**  aclnn API调用流程 <a id="fig2"></a>

![fig2](figures/aclnn-API调用流程.png "aclnn-API调用流程")
<!-- end id4 -->

## 使用说明

- **V版本演进**：功能演进过程中，算子或算子API可能会存在多个V版本，使用时请选择最高V版本（高版本默认兼容低版本能力）。
- 对于算子文档中**未声明支持的场景**（如产品型号、数据类型、数据格式、数据维度等），不推荐开发者使用，当前版本不保证算子调用效果。
<!-- npu="910b,910,310p" id9 -->
- 昇腾虚拟化实例：当前版本融合类算子暂不支持该功能。融合类算子是指由多个独立基础“小算子”（如向量Vector、矩阵Cube等）融合而成，其功能与多个小算子等效，而性能通常更优，例如Flash Attention、通算融合算子（简称MC2算子）等。
<!-- end id9 -->

## 使用向导

阅读手册正文前，请先熟悉向导表，了解手册大纲和章节作用，以帮助您快速了解算子分类、适用场景等信息。

<!-- npu="950,A3,910b,910,310p,310b" id12 -->
> **须知**：
>
> - aclnn API调用从CANN 9.0.0版本开始，整库文件libopapi.so废弃，请使用libopapi_*.so子库文件以提升算子编译效率。
> - aclnn API调用从CANN 8.5.0版本开始，libaclnn_ops_infer、libaclnn_ops_train、libaclnn_math、libaclnn_rand静态库（\*.a）和动态库（\*.so）废弃，请使用libopapi_*.so库文件替代。
> - aclnn API调用从CANN 7.0.0版本开始，头文件引用路径aclnnop/level2/aclnn\_\*.h废弃，请使用新头文件路径aclnnop/aclnn\_\*.h替代。
<!-- end id12 -->

<!-- npu="950,A3,910b,910,310p,310b" id10 -->
**表 1**  使用向导

<table><thead>
  <tr>
    <th>使用场景</th>
    <th>操作指引</th>
    <th>说明</th>
  </tr></thead>
<tbody>
  <tr>
      <td>1.算子库<b>依赖哪些头文件/库文件</b></td>
    <td><a href="header_and_library.md">头文件和库文件说明</a></td>
    <td>介绍不同方式调用算子依赖的头文件或库文件。</td>
  </tr>
  <tr>
      <td>2.算子库<b>基础领域知识</b></td>
    <td><a href="https://gitcode.com/cann/ops-math/blob/9.1.0/docs/zh/context/%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5.md">基本概念</a></td>
    <td>介绍算子的基本概念、术语及关键技术，帮助用户更好地理解算子文档。</td>
  </tr>
  <tr>
    <td>3.算子API调用时<b>依赖哪些公共接口</b></td>
    <td><a href="https://gitcode.com/cann/opbase/blob/9.1.0/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md">公共接口</a></td>
    <td>调用算子接口时依赖的公共Meta接口，如创建aclTensor、aclScalar、aclIntArray等。</td>
  </tr>
  <tr>
    <td rowspan="4">4.算子库中有哪些<b>aclnn API</b></td>
    <td><a href="bookmap_aclnn_math.md">Math类接口</a></td>
    <td>数学计算类算子库，提供Add、Abs等算子API。</td>
  </tr>
  <tr>
    <td><a href="bookmap_aclnn_nn.md">NN类接口</a></td>
    <td>Neural Network，即神经网络类算子库，提供Matmul等算子API。目前该类算子在整个算子库中占最大比重。</td>
  </tr>
  <tr>
    <td><a href="bookmap_aclnn_cv.md">CV类接口</a></td>
    <td>Computer Vision，即计算机视觉类算子库，提供GridSample等算子API。</td>
  </tr>
  <tr>
    <td><a href="bookmap_aclnn_trans.md">Transformer类接口</a></td>
    <td>大模型计算类算子库，提供FlashAttention、MC2（通算融合）、MoE（Mixture of Experts）等算子API。</td>
  </tr>
  <tr>
    <td>5.算子库有哪些<b>Torch扩展接口</b></td>
    <td><a href="op_interface_torch_extension.md">torch_extension接口</a></td>
    <td>针对非PyTorch原生但常见的大模型算子，提供PyTorch API。通过JIT即时编译C++ Kernel Wrapper，将PyTorch函数桥接到aclnn API，同时通过GE Converter支持TorchAir图模式。</td>
  </tr>
  <tr>
    <td>6.算子库中<b>Ascend IR算子规格信息</b></td>
    <td><a href="ascendIR_op_specification.md">Ascend IR算子规格说明</a></td>
    <td>罗列了基于Ascend IR定义的算子信息。</td>
  </tr>
  <tr>
    <td>7.算子库相关知识</td>
    <td><a href="appendix/appendix.md">附录</a></td>
      <td>
          <ul>
              <li>提供开发aclnn API依赖的nnopbase接口</li>
              <li>提供算子开发/调用过程依赖的op_common公共接口</li>
              <li>介绍算子性能提升方法</li>
              <li>算子调用过程中常见FAQ和案例</li>
          </ul>
      </td>
  </tr>
</tbody></table>
<!-- end id10 -->
