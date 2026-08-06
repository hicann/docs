# 概念及使用约束

## AIPP是什么

AIPP（Artificial Intelligence Pre-Processing）用于在AI Core上完成图像预处理，包括色域转换（转换图像格式）、图像归一化（减均值/乘系数）和抠图（指定抠图起始点，抠出神经网络需要的图片大小）等。

AIPP区分为静态AIPP和动态AIPP。您只能选择静态AIPP或动态AIPP方式来处理图片，不能同时配置静态AIPP和动态AIPP两种方式。

- 静态AIPP：模型转换时设置AIPP模式为静态，同时设置AIPP参数，模型生成后，AIPP参数值被保存在离线模型（\*.om文件）中，每次模型推理过程采用固定的AIPP预处理参数（无法修改）。

    如果使用静态AIPP方式，多Batch情况下共用同一份AIPP参数。

- 动态AIPP：模型转换时设置AIPP模式为动态，每次模型推理前，根据需求，在执行模型前设置动态AIPP参数值，然后在模型执行时可使用不同的AIPP参数。

    如果使用动态AIPP方式，多Batch可使用不同的AIPP参数。

## 使用约束

- **动态AIPP和动态Batch同时使用时**：
    - 调用aclmdlCreateAIPP接口设置batchSize时，batchSize要设置为最大batch size。
    - 模型中需要进行动态AIPP处理的data节点，其对应的输入内存大小需按照最大Batch来申请。

- **动态AIPP和动态分辨率同时使用时**：
    - 若在设置动态AIPP参数时，开启了抠图或缩放或补边功能，则不能与动态分辨率同时使用。
    - 若在设置动态AIPP参数时未启用抠图或缩放或补边功能，并且与动态分辨率同时使用时，需确保通过aclmdlSetAIPPSrcImageSize接口设置的宽高和通过aclmdlSetDynamicHWSize接口设置的宽高相等，均应设置为模型转换时动态分辨率最大档位的宽、高。
    - 模型中需要进行动态AIPP处理的data节点，其对应的输入内存大小需按照最大分辨率（宽、高）来申请。

- **动态AIPP和动态Shape输入（设置Shape范围）同时使用时**，动态AIPP的输出图片宽、高要在所设置的Shape范围内。
- 对同一个模型，AIPP（包括静态AIPP和动态AIPP）与动态维度（ND格式）不能同时使用。
- 除了AIPP，还存在基于DVPP（Digital Vision Pre-Processing）硬件进行媒体数据处理的acl接口，包括缩放、抠图、格式转换、图片编解码、视频编解码等，功能比AIPP丰富，但对于输入/输出图片、内存有一定的约束。

    基于DVPP的媒体数据处理接口介绍，请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。
