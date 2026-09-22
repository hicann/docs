# 动态Shape算子（不注册算子选择器）

## 基本原理

对于支持动态Shape的算子：

- 如果算子输出Shape明确，该类算子执行的基本流程与固定Shape算子执行类似，接口调用流程请参见[接口调用流程](single_operator_interface_calling_process.md)，执行固定Shape算子的示例代码请参见[固定Shape算子](fixed_shape_op.md)。
- 如果无法明确算子的输出Shape，在调用`acl.op.execute_v2`接口前，需用户调用`acl.op.infer_shape`接口、`acl.get_tensor_desc_num_dims`接口、`acl.get_tensor_desc_dim_v2`接口、`acl.get_tensor_desc_dim_range`等接口，推导或预估算子的输出Shape，作为算子执行接口`acl.op.execute_v2`的输入。

## 示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 此处算子输入Tensor数据的内存必须根据应用运行模式来确定，应用运行在Host时，此处需申请Host上的内存。
# 应用运行在Device时，此处需申请Device上的内存。
ret = acl.op.infer_shape(op_type, self.in_desc_list, self.in_list, num_outputs, self.out_desc_list, self.attr)

tensor_dims = []
# 循环算子的每一个输出，推导或预估Shape值：
for i in range(len(infer_desc_list)):
    dim_nums = acl.get_tensor_desc_num_dims(infer_desc_list[i])
    dim_size = []
    for j in range(dim_nums):
        dim, ret = acl.get_tensor_desc_dim_v2(infer_desc_list[i], j)
        # 表示动态Shape场景下维度值是动态的。
        if dim == -1:
            # 获取Shape范围，使用该范围的Shape最大值来构造输出tensor_desc，作为acl.op.execute_v2的输入。
            dim_range, ret = acl.get_tensor_desc_dim_range(infer_desc_list[i], j, 2)
            dim = dim_range[1]
        dim_size.append(dim)
    tensor_dims.append(dim_size)

# 以上给出了执行算子时输出的shape，根据tensor_dims中的dims构造输出tensor_desc（即self.out_desc_list参数值），用于调用acl.op.execute_v2。
ret = acl.op.execute_v2(op_type, self.in_desc_list, self.in_list, self.out_desc_list, self.out_list, self.attr, self.stream)

out_tensor_dims = []
# 针对上面用户预估Shape值以及使用Shape范围中的最大Shape的场景，在算子执行结束后，需增加下面的调用，获取准确的shape。
for i in range(len(self.out_desc_list)):
    dim_nums = acl.get_tensor_desc_num_dims(self.out_desc_list[i])
    dim_size = []
    for j in range(dim_nums):
        dim, ret = acl.get_tensor_desc_dim_v2(self.out_desc_list[i], j)
        dim_size.append(dim）
    out_tensor_dims.append(dim_size))

# ......
```
