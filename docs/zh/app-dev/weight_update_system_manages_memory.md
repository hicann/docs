# 权重更新（由系统管理内存）

## 接口调用流程

对于权重更新的场景，为便于用户一次编译模型后，在模型执行阶段能动态更新权重，可通过以下接口配合使用实现该功能：

1. 基于构图接口编译并保存模型，模型中包含多个图，例如推理图、变量初始化图、变量更新图等。

    此处是调用aclgrphBundleBuildModel接口编译模型、调用aclgrphBundleSaveModel接口保存模型，接口详细描述参见[《图开发》](https://hiascend.com/document/redirect/CannCommunityGraphguide)中的“接口参考 \> C++语言接口 \> aclgrph接口 \> aclgrphBundleBuildModel”、“接口参考 \> C++语言接口 \> aclgrph接口 \> aclgrphBundleSaveModel”。

    权重初始化是可选步骤，根据业务场景由用户判断是否需要包含权重初始化图，不包含的情况下，可节省模型加载所需的Device内存。

2. 调用aclmdlBundleLoadFromFile或aclmdlBundleLoadFromMem接口加载模型。
3. 调用aclmdlBundleGetModelId接口获取图的ID。
4. 根据权重初始化图ID，调用模型执行接口（例如aclmdlExecute）执行权重初始化图。
5. 若需更新权重，在执行权重更新图前，调用aclmdlSetDatasetTensorDesc接口设置图的tensor描述信息。
6. 根据权重更新图ID，调用模型执行接口（例如aclmdlExecute）执行权重更新图。
7. 根据推理图ID，调用模型执行接口（例如aclmdlExecute）执行推理图。
8. 推理结束后，调用aclmdlBundleUnload接口卸载模型。

## 示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 1. 初始化资源
aclInit(nullptr);
aclrtSetDevice(0);

// 2. 加载基于构图接口构建出来的模型，模型中包含推理图、权重初始化图、权重更新图，模型文件名以bundle.om为例
uint32_t bundle_id = 0;
aclmdlBundleLoadFromFile("./bundle.om", &bundle_id);

// 3. 根据bundleId获取实际可执行的图的数量
size_t modelNum = 0;
aclmdlBundleGetModelNum(bundle_id, &modelNum);

// 此处以modelNum=3为例，即aclgrphBundleBuildModel接口入参是3张图，各个图的索引是固定的，分别为0、1、2
uint32_t infer_id= 0;
aclmdlBundleGetModelId(bundle_id, 0, &infer_id);
uint32_t init_id= 0;
aclmdlBundleGetModelId(bundle_id, 1, &init_id);
uint32_t update_id= 0;
aclmdlBundleGetModelId(bundle_id, 2, &update_id);

// 若不需要更新权重，就执行权重初始化图和推理图
// 4.执行权重初始化图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(init_id, init_mdl_input, init_mdl_output);

// 5. 执行推理图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(infer_id, infer_mdl_input, infer_mdl_output);

// 若需要更新权重，则需要执行权重更新图之后，再执行推理图
// 6. 执行权重更新图
// 如果不需要更新某一个权重，比如第0个，shape可以传入空tensor，但device内存必须有效。
size_t no_need_refresh_index = 0;
std::vector<int64_t> dims{0};
// dims数组中的元素为0，表示空tensor
auto tensorDesc = aclCreateTensorDesc(ACL_FLOAT, dims.size(), dims.data(), ACL_FORMAT_ND);
aclmdlSetDatasetTensorDesc(update_mdl_input, tensorDesc, no_need_refresh_index);

// 7. 若需要更新某一个权重，此处以更新第1个权重为例
size_t need_refresh_index = 1;
std::vector<int64_t> dims{1, 3, 224, 224};
auto tensorDesc = aclCreateTensorDesc(ACL_FLOAT, dims.size(), dims.data(), ACL_FORMAT_ND);
aclmdlSetDatasetTensorDesc(update_mdl_input, tensorDesc, need_refresh_index);

// 8. 执行权重更新图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(update_id, update_mdl_input, update_mdl_output);

// 9. 执行推理图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
aclmdlExecute(infer_id, infer_mdl_input, infer_mdl_output);

// 10. 卸载捆绑模型
aclmdlBundleUnload(bundle_id);

// 11. 释放资源
aclrtResetDevice(0);
aclFinalize();
```
