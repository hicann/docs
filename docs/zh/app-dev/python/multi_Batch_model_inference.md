# 多Batch模型推理

多Batch推理的基本流程与单Batch类似，请参见[模型管理](model_management.md)。

多Batch推理与单Batch推理的不同点在于：

- 多Batch场景下，在构建模型时，使用ATC工具的input\_shape参数需设置具体的Batch数，详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。
- 在推理前，需要编写一段代码逻辑：当输入数据满足多Batch（例如：8Batch）的要求，申请Device上的内存存放多Batch的数据，作为模型推理的输入。如果最后循环遍历所有的输入数据后，仍不满足多Batch的要求，则直接将剩余数据作为模型推理的输入。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考，此处以**8Batch**为例：

```python
batch_size = 8
device_num = 1
device_id = 0

# 获取模型第一个输入的大小。
model_input_size = acl.mdl.get_input_size_by_index(model_desc, 0)
# 获取每个Batch输入数据的大小。
single_buff_size = model_input_size / batch_size

# 定义该变量，用于累加Batch数是否达到8Batch。
cnt = 0
# 定义该变量，用于描述每个文件读入内存时的位置偏移。
pos = 0
infer_file_vec = []

for i in range(len(files_list)):
    # 每8个文件，申请一次Device上的内存，存放8Batch的输入数据。
    if cnt % batch_size == 0:
        pos = 0
        infer_file_vec.clear()
        # 申请Device上的内存。
        p_batch_dst, ret = acl.rt.malloc(model_input_size, ACL_MEM_MALLOC_NORMAL_ONLY)

    # TODO: 从某个目录下读入文件，计算文件大小file_size。

    # 根据文件大小，申请Host上的内存，存放文件数据。
    p_img_buf, ret = acl.rt.malloc_host(file_size)

    # 将Host上的文件数据复制到Device的内存中。
    ret = acl.rt.memcpy(p_batch_dst + pos, file_size, p_img_buf, file_size, ACL_MEMCPY_HOST_TO_DEVICE)
    pos += file_size
    # 释放Host上的内存。
    acl.rt.free_host(p_img_buf)
    # 将第i个文件存入vector中，同时cnt++。
    infer_file_vec.append(files_list[i])
    cnt += 1
    # 每8Batch的输入数据送给模型进行推理。
    if cnt % batch_size == 0:
        # TODO: 创建aclmdlDataset、aclDataBuffer类型的数据，用于描述模型的输入、输出数据。
        # TODO: 调用acl.mdl.execute接口执行模型推理。
        # TODO: 推理结束后，调用acl.rt.free接口释放Device上的内存。

# 如果最后循环遍历所有的输入数据后，仍不满足多Batch的要求，则直接将剩余数据作为模型推理的输入。
if cnt % batch_size != 0:
    # TODO: 创建aclmdlDataset、aclDataBuffer类型的数据，用于描述模型的输入、输出数据。
    # TODO: 调用acl.mdl.execute接口执行模型推理。
    # TODO: 推理结束后，调用acl.rt.free接口释放Device上的内存。
# ......
```
