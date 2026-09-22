<!-- npu="950,A3,910b,910,310p,310b" id1 -->
# 概念及使用约束
<!-- end id1 -->
## 相关概念

**表 1**  概念介绍

| 概念 | 描述 |
| --- | --- |
| 动态batch/动态分辨率 | 在某些场景下，模型每次输入的batch size或分辨率是不固定的，如检测出目标后再执行目标识别网络，由于目标个数不固定导致目标识别网络输入batch size不固定。<br>动态batch：用户执行推理时，其batch size是动态可变的。<br>动态分辨率：用户执行推理时，每张图片的分辨率H * W是动态可变的。 |
| 动态维度（ND格式） | 为了支持Transformer等网络在输入格式的维度不确定的场景，需要支持ND格式下任意维度的动态设置。<br>ND表示支持任意格式，当前N ≤ 4。 |

## 使用约束

- 对同一个模型，AIPP（包括静态AIPP和动态AIPP）与动态维度（ND格式）不能同时使用。
- 对同一个模型，以下方式，**只能选择其中一种**：
  - 调用`acl.mdl.set_dataset_tensor_desc`接口设置Shape范围。
  - 调用`acl.mdl.set_dynamic_batch_size`接口设置动态Batch。
  - 调用`acl.mdl.set_dynamic_hw_size`接口设置动态分辨率。
  - 调用`acl.mdl.set_input_dynamic_dims`接口设置动态维度的维度值。

- **申请模型推理的输出内存时**，可以按照各档位的实际大小申请内存，也可以调用`acl.mdl.get_output_size_by_index`接口获取内存大小后再申请内存（建议使用该方式，确保内存足够）。

- 动态AIPP和动态Batch同时使用时：
  - 调用`acl.mdl.create_aipp`接口设置“batchSize”时，“batchSize”要设置为最大Batch数。
  - 模型中需要进行动态AIPP处理的data节点，其对应的输入内存大小需按照最大Batch来申请。

- 动态AIPP和动态分辨率同时使用时：
  - 若在设置动态AIPP参数时，**开启了**抠图或缩放或补边功能，则不能与动态分辨率同时使用。
  - 若在设置动态AIPP参数时，**未开启**抠图或缩放或补边功能，在与动态分辨率同时使用时，需确保通过`acl.mdl.set_aipp_src_image_size`接口设置的宽和高，与通过`acl.mdl.set_dynamic_hw_size`接口设置的宽和高相等，都必须设置成模型转换时动态分辨率最大档位的宽和高。
  - 模型中需要进行动态AIPP处理的data节点，其对应的输入内存大小需按照最大分辨率（宽、高）来申请。

- **动态AIPP和动态Shape输入（设置Shape范围）同时使用时**，动态AIPP的输出图片宽、高要在所设置的Shape范围内。

- **静态AIPP和动态分辨率同时使用时**，由于动态分辨率场景下输入图片的宽和高不确定，因此在使用ATC工具的“insert_op_conf”参数传入AIPP配置文件时，AIPP配置文件中不能开启Crop、Resize和Padding功能，并且需要将配置文件中的“src_image_size_w”和“src_image_size_h”取值设置为0。
