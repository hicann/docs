<!-- npu="310p" id1 -->
# 特征向量检索

## 基本原理

该部分主要实现了对特征检索的功能验证，生成随机底库，随机生成特征数据进行特征检索（当前支持**1 : N**、**M : N**两种检索模式，下文的示例代码以**1 : N**为例）。大致可分为初始化、添加特征到底库、底库搜索、精准修改或删除底库特征、去初始化几个主要步骤，具体接口调用方式如下：

- 初始化：调用`acl.init`接口进行初始化、运行时资源申请，调用`acl.fv.create_init_para`接口创建aclfvInitPara类型的数据来指定特征向量检索的初始化参数。
- 添加特征到底库：主要调用`acl.fv.create_feature_info`接口创建aclfvFeatureInfo类型数据来表示创建特征的描述信息，然后调用`acl.fv.repo_add`添加底库。
- 底库搜索：调用`acl.fv.search`接口来实现检索。
- 精准修改或删除底库特征：调用`acl.fv.delete`和`acl.fv.modify`接口来实现删除或修改底库中某个特征。下文的代码以删除底库特征为例。
- 去初始化：主要包括释放运行时资源、调用`acl.fv.destroy_init_para`接口销毁aclfvInitPara类型的数据、调用`acl.fv.release`接口特征检索模块去初始化，释放内存空间。

## 示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝编译运行，仅供参考。

```python
# 1.初始化。

# 2.申请运行时资源。

# 3.初始化。
# 3.1 初始化特征检索模块，此处以底库特征数100000为例。
fs_num = 100000
fv_init_para = acl.fv.create_init_para(fs_num)

# 3.2 指定特征向量检索的初始化参数。
ret = acl.fv.init(fv_init_para)

# 4.添加底库和特征向量。
# 4.1 增加第一个特征，创建特征描述信息时，偏移量offset参数值为0。
offset = 0
feature_count = 1000
feature_len = 36
base_data_len = feature_count * feature_len

# 创建内存。
feature_info_device, ret = acl.rt.malloc(base_data_len, ACL_MEM_MALLOC_NORMAL_ONLY)

# 此处的自定义函数base_short_feature_alloc用于生成特征随机数据，由用户自行实现。
feature_type = SEARCH_1_N
feature_info_buffer = base_short_feature_alloc(feature_count, feature_type)

# 将随机特征数据转换为数组。
feature_info_list_arr = numpy.array(feature_info_buffer, dtype=numpy.uint8)
# 将随机特征数据转换为bytes对象，通过acl.util.bytes_to_ptr获取bytes对象的指针地址。
bytes_data = feature_info_list_arr.tobytes()
feature_info_ptr = acl.util.bytes_to_ptr(bytes_data)
# 将随机特征数据从Host侧拷贝到Device侧。
ret = acl.rt.memcpy(feature_info_device, feature_count * feature_len, feature_info_ptr, feature_count * feature_len, ACL_MEMCPY_HOST_TO_DEVICE)


# 创建特征描述信息，inputData表示前一步的特征随机数据。
feature_info = acl.fv.create_feature_info(id0, id1, offset, feature_len, feature_count, feature_info_device, feature_len * feature_count)

# 添加底库并向底库中添加特征，featureInfo表示前一步的特征描述信息。
ret = acl.fv.repo_add(SEARCH_1_N, feature_info)

# 销毁aclfvFeatureInfo特征描述信息。
ret = acl.fv.destroy_feature_info(feature_info)

# 4.2增加第二个特征，创建特征描述信息时，偏移值offset需要与库中已添加特征个数一致，并精确删除或修改底库中的某个特征。
offset += feature_count

# 增加特征到底库的步骤，参考4.1中的代码。
# ....

feature_data_list = []
for i in range(36):
    feature_data_list.append(i)
# 将随机特征数据转换为数组。
feature_info_list_arr = numpy.array(feature_data_list, dtype=numpy.uint8)
# 将随机特征数据转换为bytes对象，通过acl.util.bytes_to_ptr获取bytes对象的指针地址。
bytes_data = feature_info_list_arr.tobytes()
feature_info_ptr = acl.util.bytes_to_ptr(bytes_data)
# 创建内存并传输特征数据。
feature_info_device, ret = acl.rt.malloc(36, ACL_MEM_MALLOC_NORMAL_ONLY)
kind = ACL_MEMCPY_DEVICE_TO_DEVICE

# 如果运行模式是ACL_HOST,将特征数据拷贝到Device侧，其中feature_len为feature_data_list数据集申请的内存长度。
ret = acl.rt.memcpy(feature_info_device, feature_count * feature_len, feature_info_ptr, feature_count * feature_len, ACL_MEMCPY_HOST_TO_DEVICE)

# 创建特征描述信息。
id0 = 0
id1 = 0
feature_info = acl.fv.create_feature_info(id0, id1, offset, 36, 1, feature_info_buffer, 36)

#  删除1个特征。
acl.fv.destroy_feature_info(feature_info)

# 4.3 增加特征到其它底库,其中一级底库为1，二级底库为1。
id0 = 1
id1 = 1
offset = 0

# 增加特征到底库步骤，参考4.1中的代码。
# ....

# 5 底库检索（以1：N检索为例），主要包括特征检索预处理，特征1:N检索，特征检索结果处理三个部分。
# 5.1 特征检索预处理，对于1:N来说, queryCnt必须为1。
query_cnt = 1
table_len = 32 * 1024
topK = 5
type_size = 4
table_data_len = query_cnt * table_len

# 生成数据表，用户通过数据表进行检索比对，此处的自定义函数adc_table_init用于初始化特征检索输入Adc表，由用户自行实现。
table_data_tmp = adc_table_init(1000, query_cnt * 1024)

# 为数据表分配内存，table_data_dev用于创建检索输入表信息。
table_data,ret = acl.rt.malloc(table_data_len, ACL_MEM_MALLOC_NORMAL_ONLY)

# 为检索结果resultNumDev,id0Dev,id1Dev,resultOffsetDev,resultDistanceDev分配内存。
data_len = query_cnt * topK * type_size
result_num_data_len = query_cnt * type_size
result_num, ret = acl.rt.malloc(result_num_data_len, ACL_MEM_MALLOC_NORMAL_ONLY)
id_0, ret = acl.rt.malloc(data_len, ACL_MEM_MALLOC_NORMAL_ONLY)
id_1, ret = acl.rt.malloc(data_len, ACL_MEM_MALLOC_NORMAL_ONLY)
result_offset, ret = acl.rt.malloc(data_len, ACL_MEM_MALLOC_NORMAL_ONLY)
result_distance, ret = acl.rt.malloc(data_len, ACL_MEM_MALLOC_NORMAL_ONLY)

# 创建检索输入表信息，结果用于创建检索任务输入信息。
query_table = acl.fv.create_query_table(query_cnt, table_len, table_data, table_data_len)

# 创建特征库范围参数，结果用于创建检索任务输入信息。
repo_range = acl.fv.create_repo_range(0, 1023, 0, 1023)
# 创建检索任务输入信息，结果用于特征1：N检索。
search_input = acl.fv.create_search_input(query_table, repo_range, topK)

# 创建检索结果信息，结果用于特征1：N检索。
search_result = acl.fv.create_search_result(query_cnt, result_num, result_num_data_len, id_0, id_1, result_offert, result_distance, data_len)

# 5.2 特征1：N检索。
ret = acl.fv.search(SEARCH_1_N, search_input, search_result)

# 6. 删除底库和数据。
# 创建特征库范围并删除指定范围内的底库。
id0Min = 0
id0Max = 1023
id1Min = 0
id1Max = 1023
repo_range = acl.fv.create_repo_range(id0Min, id0Max, id1Min, id1Max)
ret = acl.fv.repo_del(SEARCH_1_N, repo_range)

#  销毁aclfvInitPara类型的数据。
ret = acl.fv.destroy_init_para(fv_init_para)

# 7. 释放运行时资源

# 8. 去初始化
# ......
```
<!-- end id1 -->
