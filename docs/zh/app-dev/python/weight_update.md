<!-- npu="950,A3,910b,910,310p,310b" id1 -->
# 权重更新

## 接口调用流程

对于权重更新的场景，为便于用户一次编译模型后，在模型执行阶段能动态更新权重，可通过以下接口配合使用实现该功能：

1. 基于构图方式编译并保存模型，模型中包含推理图、权重初始化图、权重更新图三部分。

    此处是调用“接口参考 > C++语言接口 > aclgrph接口 > aclgrphBundleBuildModel”接口编译模型、调用“接口参考 > C++语言接口 > aclgrph接口 > aclgrphBundleSaveModel”接口保存模型，接口详细描述参见《图开发》。

    权重初始化是可选步骤，根据业务场景由用户判断是否需要包含权重初始化图，不包含的情况下，可节省模型加载所需的Device内存。

2. 调用`acl.mdl.bundle_load_from_file`或`acl.mdl.load_from_mem`接口加载模型。
3. 调用`acl.mdl.bundle_get_model_id`接口获取三个图的ID。
4. 根据权重初始化图ID，调用模型执行接口（例如`acl.mdl.execute`）执行权重初始化图。
5. 若需更新权重，在执行权重更新图前，调用`acl.mdl.set_dataset_tensor_desc`接口设置图的tensor描述信息。
6. 根据权重更新图ID，调用模型执行接口（例如`acl.mdl.execute`）执行权重更新图。
7. 根据推理图ID，调用模型执行接口（例如`acl.mdl.execute`）执行推理图。
8. 推理结束后，调用`acl.mdl.bundle_unload`接口卸载模型。

## 示例代码

本节中的示例重点介绍模型推理的代码逻辑，初始化和去初始化请参见[初始化与去初始化](initialization_and_deinitialization.md)，运行时资源申请与释放请参见[运行时资源申请与释放](runtime_resource_allocation_and_release.md)。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝编译运行，仅供参考。

```python
# 1. 初始化资源
ret = acl.init(config_path)
ret = acl.rt.set_device(device_id)

# 2. 加载基于构图方式构建出来的模型，模型中包含推理图、权重初始化图、权重更新图，模型文件名以bundle.om为例
bundle_id, ret = acl.mdl.bundle_load_from_file("./bundle.om")

# 3. 获取模型中各个图的ID
model_num, ret = acl.mdl.bundle_get_model_num(bundle_id)

# 此处aclgrphBundleBuildModel接口入参是3张图，各个图的索引是固定的
infer_id, ret = acl.mdl.bundle_get_model_id(bundle_id, 0)
init_id, ret = acl.mdl.bundle_get_model_id(bundle_id, 1)
update_id, ret = acl.mdl.bundle_get_model_id(bundle_id, 2)

# 若不需要更新权重，就执行权重初始化图和推理图
# 4.执行权重初始化图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
ret = acl.mdl.execute(init_id, init_mdl_input, init_mdl_output)

# 5. 执行推理图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
ret = acl.mdl.execute(infer_id, infer_mdl_input, infer_mdl_output)

# 若需要更新权重，则需要执行权重更新图之后，再执行推理图
# 6. 执行权重更新图
# 如果不需要更新某一个权重，比如第0个，shape可以传入空tensor，但device内存必须有效。
no_need_refresh_index = 0
dims = [0]
# dims数组中的元素为0，表示空tensor
tensor_desc = acl.create_tensor_desc(data_type, dims, format)
update_mdl_input, ret = acl.mdl.set_dataset_tensor_desc(update_mdl_input, tensor_desc, no_need_refresh_index)

# 若需要更新某一个权重，此处以更新第1个权重为例
need_refresh_index = 1
dims = [1, 3, 224, 224]
tensor_desc = acl.create_tensor_desc(data_type, dims, format)
update_mdl_input, ret = acl.mdl.set_dataset_tensor_desc(update_mdl_input, tensor_desc, need_refresh_index)

# 7. 执行权重更新图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
ret = acl.mdl.execute(update_id, update_mdl_input, update_mdl_output)

# 8. 执行推理图，准备模型输入、输出请参见模型推理下其它推理特性章节的示例代码
ret = acl.mdl.execute(infer_id, infer_mdl_input, infer_mdl_output)

# 9. 卸载捆绑模型
ret = acl.mdl.unload(bundle_id)

# 10. 释放资源
ret = acl.rt.reset_device(0)
ret = acl.finalize()
```
<!-- end id1 -->