# 权重更新（由用户管理内存）

## 接口调用流程

对于权重更新的场景，为便于用户一次编译模型后，在模型执行阶段能动态更新权重，可通过以下接口配合使用实现该功能：

1. 基于构图接口编译并保存模型，模型中包含多个图，例如推理图、变量初始化图、变量更新图等。

    此处是调用aclgrphBundleBuildModel接口编译模型、调用aclgrphBundleSaveModel接口保存模型，接口详细描述参见《图开发》中的“接口参考 \> C++语言接口 \> aclgrph接口 \> aclgrphBundleBuildModel”、“接口参考 \> C++语言接口 \> aclgrph接口 \> aclgrphBundleSaveModel”。

    权重初始化是可选步骤，根据业务场景由用户判断是否需要包含权重初始化图，不包含的情况下，可节省模型加载所需的Device内存。

2. 调用aclmdlBundleQueryInfoFromFile或aclmdlBundleQueryInfoFromMem接口获取模型描述信息。
3. 调用aclmdlBundleGetQueryModelNum接口获取捆绑模型中的图总数。
4. 调用aclmdlBundleGetVarWeightSize和aclmdlBundleGetSize接口获取模型需要的内存信息，包含可刷新权重大小，每个图需要的工作内存大小和权重内存大小。
5. 调用aclmdlBundleInitFromFile或aclmdlBundleInitFromMem接口初始化模型。
6. 根据索引多次调用aclmdlBundleLoadModelWithMem接口加载图，支持传入申请好的工作内存和权重内存，得到对应图的modelId。
7. 根据权重初始化图modelId，调用模型执行接口（例如aclmdlExecute）执行权重初始化图。
8. 若需更新权重，在执行权重更新图前，调用aclmdlSetDatasetTensorDesc接口设置图的tensor描述信息。
9. 根据权重更新图modelId，调用模型执行接口（例如aclmdlExecute）执行权重更新图。
10. 根据推理图modelId，调用模型执行接口（例如aclmdlExecute）执行推理图。
11. 推理结束后，需先调用aclmdlBundleUnloadModel接口卸载图，再调用aclmdlBundleUnload接口卸载模型。

## 示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 1. 初始化资源
aclInit(nullptr);
aclrtSetDevice(0);

// 2. 查询基于构图接口构建出来的模型内存信息，模型中包含推理图、权重初始化图、权重更新图，模型文件名以bundle.om为例
aclmdlBundleQueryInfo *query_info = aclmdlBundleCreateQueryInfo();
aclmdlBundleQueryInfoFromFile("./bundle.om", query_info);

// 3. 根据查询信息获取模型中的图总数以及内存信息
size_t modelNum = 0;
aclmdlBundleGetQueryModelNum(query_info, &modelNum);
// 获取模型所需的可刷新权重大小并申请内存（可选，不申请则系统内部完成申请）
size_t variableWeightSize = 0;
aclmdlBundleGetVarWeightSize(query_info, &variableWeightSize);
void *var_p = nullptr;
aclrtMalloc(&var_p, variableWeightSize, ACL_MEM_MALLOC_NORMAL_ONLY);
// 此处以modelNum=3为例，即aclgrphBundleBuildModel接口入参是3张图，各个图的索引是固定的，分别为0、1、2
// 获取索引为0的推理图所需的工作内存和权重内存大小并申请（可选，不申请则系统内部完成申请）
size_t inferWorkSize, inferConstWeightSize;
aclmdlBundleGetSize(query_info, 0, &inferWorkSize, &inferConstWeightSize);
void *inferWorkPtr = nullptr;
aclrtMalloc(&inferWorkPtr, inferWorkSize, ACL_MEM_MALLOC_NORMAL_ONLY);
void *inferConstWeightPtr = nullptr;
aclrtMalloc(&inferConstWeightPtr, inferConstWeightSize, ACL_MEM_MALLOC_NORMAL_ONLY);

// 4. 初始化bundle.om
uint32_t bundle_id = 0;
// 如果系统内部申请，则在var_p处传nullptr，在variableWeightSize处传0
aclmdlBundleInitFromFile("./bundle.om", var_p, variableWeightSize, &bundle_id);

// 5. 根据索引按需加载图
uint32_t infer_id= 0;
// 如果系统内部申请，则aclmdlBundleLoadModelWithMem(bundle_id, 0, nullptr, 0, nullptr, 0, &init_id);
aclmdlBundleLoadModelWithMem(bundle_id, 0, inferWorkPtr, inferWorkSize,inferConstWeightPtr, inferConstWeightSize, &infer_id);
uint32_t init_id= 0;
aclmdlBundleLoadModelWithMem(bundle_id, 1, nullptr, 0, nullptr, 0, &init_id);
uint32_t update_id= 0;
aclmdlBundleLoadModelWithMem(bundle_id, 2, nullptr, 0, nullptr, 0, &update_id);

// 若不需要更新权重，就执行权重初始化图和推理图
// 6. 执行权重初始化图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(init_id, init_mdl_input, init_mdl_output);

// 7. 执行推理图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(infer_id, infer_mdl_input, infer_mdl_output);

// 若需要更新权重，则需要执行权重更新图之后，再执行推理图
// 8. 执行权重更新图
// 如果不需要更新某一个权重，比如第0个，shape可以传入空tensor，但device内存必须有效。
size_t no_need_refresh_index = 0;
std::vector<int64_t> dims{0};
// dims数组中的元素为0，表示空tensor
auto tensorDesc = aclCreateTensorDesc(ACL_FLOAT, dims.size(), dims.data(), ACL_FORMAT_ND);
aclmdlSetDatasetTensorDesc(update_mdl_input, tensorDesc, no_need_refresh_index);

// 9. 若需要更新某一个权重，此处以更新第1个权重为例
size_t need_refresh_index = 1;
std::vector<int64_t> dims{1, 3, 224, 224};
auto tensorDesc = aclCreateTensorDesc(ACL_FLOAT, dims.size(), dims.data(), ACL_FORMAT_ND);
aclmdlSetDatasetTensorDesc(update_mdl_input, tensorDesc, need_refresh_index);

// 10. 执行权重更新图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(update_id, update_mdl_input, update_mdl_output);

// 11. 执行推理图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(infer_id, infer_mdl_input, infer_mdl_output);

// 12. 卸载模型
aclmdlBundleUnloadModel(bundle_id, infer_id);
aclmdlBundleUnloadModel(bundle_id, init_id);
aclmdlBundleUnloadModel(bundle_id, update_id);
aclmdlBundleUnload(bundle_id);

// 13. 释放资源
aclrtResetDevice(0);
aclFinalize();
```
