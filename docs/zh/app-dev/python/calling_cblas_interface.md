# 调用CBLAS接口

## 基本原理

目前，pyacl已将GEMM算子（用于矩阵-向量乘、矩阵-矩阵乘）、Cast算子（用于转换数据类型）封装成pyacl接口，可参见《Runtime运行时API》中的CBLAS接口，目前支持以下两种执行方式：

- 不以handle方式执行算子，接口名称中不包含“handle”关键字，例如，调用`acl.blas.gemm_ex`接口（封装GEMM算子）、`acl.op.cast`接口（封装Cast算子）等执行算子。
- 以handle方式执行算子，接口名称中包含“handle”关键字，例如，调用`acl.blas.create_handle_for_gemm_ex`接口、`acl.op.create_handle_for_cast`接口等创建handle后，还需要调用`acl.op.execute_with_handle`接口执行算子。

>[!NOTE]
>
>- 不以handle方式执行算子时，每次执行算子时，系统内部都会根据算子描述信息匹配内存中的模型。
>- 以handle方式执行算子时，系统内部将算子描述信息匹配到内存中的模型，并缓存在Handle中，每次执行算子时，无需重复匹配算子与模型，因此在涉及多次执行同一个算子时，效率更高。但Handle使用结束后，需调用`acl.op.destroy_handle`接口释放。

## 示例代码

本章以`acl.blas.gemm_ex`接口为例，该示例中矩阵乘的计算公式为：C = αAB + βC，表示矩阵A和矩阵B相乘后得到矩阵C，α和β表示乘积的系数。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

ACL_MEM_MALLOC_HUGE_FIRST = 2
ACL_TRANS_N = 0
ACL_COMPUTE_HIGH_PRECISION = 0
ACL_MEMCPY_HOST_TO_DEVICE = 1
ACL_MEMCPY_DEVICE_TO_HOST = 2

# 1.初始化。
ret = acl.init("test_data/config/acl.json")

# 2.设置单算子模型文件所在的目录。
ret = acl.op.set_model_dir("op_models")

# 3.指定用于运算的设备。
device_id = 0
ret = acl.rt.set_device(device_id)

# 4.申请内存。
# 4.1 申请Device上的内存存放执行算子的输入数据。
# 对于该矩阵乘示例，size_a表示矩阵A数据的大小，size_b表示矩阵B数据的大小，size_c表示矩阵C数据的大小。
in_dtype, out_dtype = 1, 1
size_a = m * k * acl.data_type_size(acl_dtype)
size_b = k * n * acl.data_type_size(acl_dtype)
size_c = m * n * acl.data_type_size(acl_dtype)
dev_matrix_a, ret = acl.rt.malloc(size_a, ACL_MEM_MALLOC_HUGE_FIRST)
dev_matrix_b, ret = acl.rt.malloc(size_b, ACL_MEM_MALLOC_HUGE_FIRST)
dev_matrix_c, ret = acl.rt.malloc(size_c, ACL_MEM_MALLOC_HUGE_FIRST)
# 4.2 申请Host上的内存。
# 对于该矩阵乘示例，m表示矩阵A的行数与矩阵C的行数，n表示矩阵B的列数与矩阵C的列数。
# k表示矩阵A的列数与矩阵B的行数。
host_matrix_a, ret = acl.rt.malloc_host(size_a)
host_matrix_b, ret = acl.rt.malloc_host(size_b)
host_matrix_c, ret = acl.rt.malloc_host(size_c)

# 5.准备输入数据。
# 从文件读入到host_matrix_a和host_matrix_b中。
# 对于该矩阵乘示例，将矩阵A和矩阵B的数据从Host复制到Device。
ret = acl.rt.memcpy(dev_matrix_a, size_a, host_matrix_a, size_a, ACL_MEMCPY_HOST_TO_DEVICE)
ret = acl.rt.memcpy(dev_matrix_b, size_b, host_matrix_b, size_b, ACL_MEMCPY_HOST_TO_DEVICE)

# 6.执行单算子。
stream, ret = acl.rt.create_stream()
# 对于该示例，调用acl.blas.gemm_ex接口（异步接口）实现矩阵-矩阵的乘法。
ret = acl.blas.gemm_ex(ACL_TRANS_N, ACL_TRANS_N, ACL_TRANS_N, m, n, k, dev_alpha, dev_matrix_a, k, input_type, dev_matrix_b, n, input_type, dev_beta, dev_matrix_c, n, output_type, ACL_COMPUTE_HIGH_PRECISION, stream)
# 调用acl.rt.synchronize_stream接口阻塞Host运行，直到指定Stream中的所有任务都完成。
ret = acl.rt.synchronize_stream(stream)

# 7.将算子的输出数据从Device复制到Host。
ret = acl.rt.memcpy(host_matrix_c, size_c, dev_matrix_c, size_c, ACL_MEMCPY_DEVICE_TO_HOST)

# 8.释放运行时资源。
ret = acl.rt.destroy_stream(stream)
ret = acl.rt.reset_device(device_id)
ret = acl.finalize()
# ......
```
