# 概念及使用约束

## 相关概念

**表 1**  概念介绍

| 概念 | 描述 |
| --- | --- |
| 动态Batch/动态分辨率 | 在某些场景下，模型每次输入的batch size或分辨率是不固定的，如检测出目标后再执行目标识别网络，由于目标个数不固定导致目标识别网络输入BatchSize不固定。<br><br>  - 动态Batch：用户执行推理时，其batch size是动态可变的。<br>  - 动态分辨率: 用户执行推理时，每张图片的分辨率H*W是动态可变的。 |
| 动态维度（ND格式） | 为了支持Transformer等网络在输入格式的维度不确定的场景，需要支持ND格式下任意维度的动态设置。 |

## 使用约束

| 使用场景 | 须知 |
| --- | --- |
| 对同一个模型执行推理时 | AIPP（包括静态AIPP和动态AIPP）与动态维度（ND格式）不能同时使用。 |
| 对同一个模型执行推理时 | 以下方式，只能选择其中一种：<br>  - 调用aclmdlSetDatasetTensorDesc接口设置Shape范围<br>  - 调用aclmdlSetDynamicBatchSize接口设置动态Batch<br>  - 调用aclmdlSetDynamicHWSize接口设置动态分辨率<br>  - 调用aclmdlSetInputDynamicDims接口设置动态维度的维度值 |
| 申请模型推理的输出内存时 | 可以按照各档位的实际大小申请内存，也可以调用aclmdlGetOutputSizeByIndex接口获取内存大小后再申请内存（建议使用该方式，确保内存足够）。 |
| 静态AIPP和动态分辨率同时使用时 | 由于动态分辨率场景下输入图片的宽和高不确定，因此在使用ATC工具的insert_op_conf参数传入AIPP配置文件时，AIPP配置文件中不能开启Crop和Padding功能，并且需要将配置文件中的src_image_size_w和src_image_size_h取值设置为0。 |
| 动态AIPP和动态Batch同时使用时 | - 调用aclmdlCreateAIPP接口设置batchSize时，batchSize要设置为最大batch size。<br>  - 模型中需要进行动态AIPP处理的data节点，其对应的输入内存大小需按照最大Batch来申请。 |
| 动态AIPP和动态分辨率同时使用时 | - 若在设置动态AIPP参数时，开启了抠图或缩放或补边功能，则不能与动态分辨率同时使用。<br>  - 若在设置动态AIPP参数时，未开启抠图或缩放或补边功能，在与动态分辨率同时使用时，需确保通过aclmdlSetAIPPSrcImageSize接口设置的宽、高与通过aclmdlSetDynamicHWSize接口设置的宽、高相等，都必须设置成模型转换时动态分辨率最大档位的宽、高。<br>  - 模型中需要进行动态AIPP处理的data节点，其对应的输入内存大小需按照最大分辨率（宽、高）来申请。 |
| 动态AIPP和动态Shape输入（设置Shape范围）同时使用时 | 动态AIPP的输出图片宽、高要在所设置的Shape范围内。 |
