# 头文件和库文件说明

## 环境要求

<!-- npu="950,A3,910b,910,310p,310b" id1 -->
- 通过aclnn API调用算子时，请提前安装CANN Toolkit包、ops算子包，具体操作参见[《CANN软件安装》](https://hiascend.com/document/redirect/CannCommunityInstSoftware)。
<!-- end id1 -->
<!-- npu="950,A3,910b" id2 -->
- 通过PyTorch API调用算子时，请提前安装CANN Toolkit包、ops算子包、TorchNPU包（注意与Toolkit包版本配套），具体操作参见[《CANN软件安装》](https://hiascend.com/document/redirect/CannCommunityInstSoftware)和[《TorchNPU软件安装》](https://www.hiascend.com/document/detail/zh/Pytorch/2600/configandinstg/instg/docs/zh/installation_guide/installation_description.md)。
<!-- end id2 -->
- 通过GE构图方式调用算子Ascend IR时，请提前安装CANN Toolkit包、ops算子包，具体操作参见[《CANN软件安装》](https://hiascend.com/document/redirect/CannCommunityInstSoftware)。

## 依赖文件列表

**算子库中不同类型的接口定义在不同的路径下：**

<!-- npu="950,A3,910b,910,310p,310b" id3 -->
- 调用算子aclnn API时，需include依赖的头文件和库文件，头文件默认在`${INSTALL_DIR}/include/`目录，库文件默认在`${INSTALL_DIR}/lib64/`目录，详细引用路径参见[表1](#table1)。
<!-- end id3 -->
<!-- npu="950,A3,910b" id4 -->
- 调用torch\_extension API时，需导入如下模块，其中cann\_ops\_transformer定义在`${INSTALL_DIR}/python/site-packages/cann_ops_transformer`目录。

    ```python
    import torch 
    import torch_npu
    import cann_ops_transformer
    ```
<!-- end id4 -->

- 调用Ascend IR算子时，其头文件路径为`${INSTALL_DIR}/opp/built-in/op_graph/inc/ops_proto_*.h`，库文件路径为`${INSTALL_DIR}/opp/built-in/op_graph/lib/libopgraph_*.so`，详细引用路径参见[表1](#table1)。

其中`${INSTALL_DIR}`请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为`/usr/local/Ascend/cann`。

**表 1**  依赖文件列表  <a id="table1"></a>

<!-- npu="950,A3,910b,910,310p,310b" id5 -->
|  接口分类  |  用途  |  命名风格  |  依赖的头文件  |  依赖的库文件  |
|----------|--------|-----------|--------------|--------------|
|  [公共接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md)   |调用aclnn API依赖的公共Meta接口，如创建aclTensor、aclScalar、aclIntArray等。|以acl为前缀，要求大驼峰风格。|<li>aclnn/acl_meta.h</li><li>aclnn/aclnn_base.h</li>|libnnopbase.so|
|  [算子接口（aclnn）](op_interface_aclnn.md)  | 提供一套C API实现CANN算子调用，包括Math、NN、CV、Transformer等类算子。 | 以aclnn为前缀，一般分为两段式接口，其中“Xxx”表示算子名（要求大驼峰风格）。<li>一阶段：aclnnXxxGetWorkspaceSize</li><li>二阶段：aclnnXxx</li>|<li>每类API依赖的头文件（推荐）：aclnnop/aclnn_ops_math.h、aclnnop/aclnn_ops_nn.h、aclnnop/aclnn_ops_cv.h、aclnnop/aclnn_ops_transformer.h</li><li>每个API依赖的头文件：aclnnop/aclnn_*.h（*表示具体算子名）</li>  | <li>aclnn API依赖的总库文件：libopapi.so（废弃）</li><li>每类API依赖的库文件：libopapi_math.so、libopapi_nn.so、libopapi_cv.so、libopapi_transformer.so</li> |
|   [算子接口（torch_extension）](op_interface_torch_extension.md)  | 针对非PyTorch原生但常见的大模型算子，提供一套兼容PyTorch风格的API实现CANN算子调用。 | 以\$\{op\_name\}为接口名，要求小写和下划线形式，调用样式cann\_ops\_transformer.\$\{op\_name\}，一般定义在`${INSTALL_DIR}/python/site-packages/cann_ops_transformer`目录. | - | - |
|   [Ascend IR算子规格](ascendIR_op_specification.md)  | 提供GE图场景下会用到的CANN算子规格信息，包括功能、数据类型、format等。 | IR命名是大驼峰风格：XxxYyyZzz，例如AsinGrad。 | <li>ops_proto_math.h</li><li>ops_proto_nn.h</li><li>ops_proto_cv.h</li><li>ops_proto_transformer.h</li><li>ops_proto_legacy.h</li> |  <li>libopgraph_math.so</li><li>libopgraph_nn.so</li><li>libopgraph_cv.so</li><li>libopgraph_transformer.so</li><li>libopgraph_legacy.so</li> |
|   [附录>nnopbase接口>框架能力接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/opbase_frame_interface.md)   | 提供开发aclnn API依赖的公共框架能力接口。 | 大驼峰风格 | aclnn/opdev/*.h，具体文件名参见[nnopbase接口列表](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/01-aclnn_development_interface_list.md)。 | - |
|   [附录>nnopbase接口>基础张量操作接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/L0/basic_l0_Interface.md)  | 提供开发aclnn API依赖的Level0接口。 | 大驼峰风格 | aclnn_kernels/*.h，具体文件名参见[nnopbase接口列表](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/01-aclnn_development_interface_list.md)。 | libopapi_math.so |
|   [附录>op_common接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/op_common/00_op_common_list.md)   | 提供算子开发/调用过程中依赖的公共能力，例如日志获取、Tiling/InferShape开发相关接口。 |大驼峰风格  |  <ul><li>op\_common/log/\*.h</li><li>op\_common/op\_host/\*.h</li><li>op\_common/op\_kernel/\*.h</li><li>op\_common/op\_graph/\*.h</li></ul>具体文件名参见[op_common接口列表](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/op_common/op_common_interface_list.md)。  | - |
<!-- end id5 -->

<!-- npu="IPV350" id6 -->
|  接口分类  |  用途  |  命名风格  |  依赖的头文件  |  依赖的库文件  |
|----------|--------|-----------|--------------|--------------|
|  [公共接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/aclnn/00_aclnn_api_list.md)   |调用aclnn API依赖的公共Meta接口，如创建aclTensor、aclScalar、aclIntArray等。|以acl为前缀，要求大驼峰风格。|<li>aclnn/acl_meta.h</li><li>aclnn/aclnn_base.h</li>|libnnopbase.so|
|  [算子接口（aclnn）](op_interface_aclnn.md)  | 提供一套C API实现CANN算子调用，包括Math、NN、CV、Transformer等类算子。 | 以aclnn为前缀，一般分为两段式接口，其中“Xxx”表示算子名（要求大驼峰风格）。<li>一阶段：aclnnXxxGetWorkspaceSize</li><li>二阶段：aclnnXxx</li>|<li>每类API依赖的头文件（推荐）：aclnnop/aclnn_ops_math.h、aclnnop/aclnn_ops_nn.h、aclnnop/aclnn_ops_cv.h、aclnnop/aclnn_ops_transformer.h</li><li>每个API依赖的头文件：aclnnop/aclnn_*.h（*表示具体算子名）</li>  | <li>aclnn API依赖的总库文件：libopapi.so（废弃）</li><li>每类API依赖的库文件：libopapi_math.so、libopapi_nn.so、libopapi_cv.so、libopapi_transformer.so</li> |
|   [Ascend IR算子规格](ascendIR_op_specification.md)  | 提供GE图场景下会用到的CANN算子规格信息，包括功能、数据类型、format等。 | IR命名是大驼峰风格：XxxYyyZzz，例如AsinGrad。 | <li>ops_proto_math.h</li><li>ops_proto_nn.h</li><li>ops_proto_cv.h</li><li>ops_proto_transformer.h</li><li>ops_proto_legacy.h</li> |  <li>libopgraph_math.so</li><li>libopgraph_nn.so</li><li>libopgraph_cv.so</li><li>libopgraph_transformer.so</li><li>libopgraph_legacy.so</li> |
|   [附录>nnopbase接口>框架能力接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/opbase_frame_interface.md)   | 提供开发aclnn API依赖的公共框架能力接口。 | 大驼峰风格 | aclnn/opdev/*.h，具体文件名参见[nnopbase接口列表](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/01-aclnn_development_interface_list.md)。 | - |
|   [附录>nnopbase接口>基础张量操作接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/L0/basic_l0_Interface.md)  | 提供开发aclnn API依赖的Level0接口。 | 大驼峰风格 | aclnn_kernels/*.h，具体文件名参见[nnopbase接口列表](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/nnopbase/opdev/01-aclnn_development_interface_list.md)。 | libopapi_math.so |
|   [附录>op_common接口](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/op_common/00_op_common_list.md)   | 提供算子开发/调用过程中依赖的公共能力，例如日志获取、Tiling/InferShape开发相关接口。 |大驼峰风格  |  <ul><li>op\_common/log/\*.h</li><li>op\_common/op\_host/\*.h</li><li>op\_common/op\_kernel/\*.h</li><li>op\_common/op\_graph/\*.h</li></ul>具体文件名参见[op_common接口列表](https://gitcode.com/cann/opbase/blob/master/docs/zh/api/op_common/op_common_interface_list.md)。  | - |
<!-- end id6 -->

<!-- npu="950,A3,910b,910,310p,310b" id7 -->
>**说明：**
>
> - 调用算子接口（aclnn）时，请注意依赖的头文件：
>   - 引用每类总头文件后无需引用单API头文件。
>   - 从CANN 7.0.0开始，算子头文件路径aclnnop/level2/aclnn\_\*.h**废弃**，请使用新头文件路径aclnnop/aclnn\_\*.h替代。
> - 调用算子接口（aclnn）时，请注意依赖的库文件：
>   - 从CANN 9.0.0开始，libopapi.so**废弃，**请使用libopapi\_\*.so子库文件以提升算子编译效率。
>   - 从CANN 8.5.0开始，libaclnn\_ops\_infer、libaclnn\_ops\_train、libaclnn\_math、libaclnn\_rand静态库（\*.a）和动态库\(\*.so\)**废弃，**请使用libopapi\_\*.so库文件。
<!-- end id7 -->

<!-- npu="IPV350" id8 -->
> **说明：**
>
> 当前版本**暂不支持使用**此类接口，您无需关注：
>
> - 公共接口
> - 算子接口（aclnn）
> - 附录\>nnopbase接口
> - 附录\>op\_common接口
<!-- end id8 -->