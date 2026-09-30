# 应用调试

## 运行应用
<!-- npu="910,310p,310b" id1 -->
运行应用的步骤，请参考[基于Caffe ResNet-50网络实现图片分类（同步推理）](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/resnet50_imagenet_classification)。
<!-- end id1 -->
**相关注意点如下：**

1. 模型转换，详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。
2. 运行时，需将初始化配置文件（acl.json）所在的目录、测试图片所在的目录、\*.om文件所在的目录都上传到Host的同一个目录下。

    如果在[初始化](initialization_and_deinitialization.md)阶段，在`acl.init`接口中不传入参数，则无需将初始化配置文件（acl.json）所在的目录上传到Host。

3. 运行代码时，直接运行对应的Python脚本即可。如：

    ```python
    python3 main.py
    ```

## 问题定位

运行应用时如果出错，您可以参见[《日志参考》](https://hiascend.com/document/redirect/CannCommunitylogref)获取日志文件，以便查看日志文件中详细报错。根据报错初步定位后：

- 如果是接口约束导致接口调用逻辑不对，需查看总体的[使用约束](constraints.md)以及各接口本身的约束，再调整接口调用逻辑。
