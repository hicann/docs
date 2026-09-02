# TbeAippConvReluMaxpoolingFusion

## 融合模式

该融合将满足如下Pattern关系的子图中Aipp（可选） + Conv2D + Dequant（可选） + ElemWise（可选） + MaxPool（MaxPool/Pooling/MaxPoolv3）+ AscendQuant（可选）算子融合成一个融合算子。

![](../figures/TbeAippConvReluMaxpoolingFusion_1.png)

## 使用约束

满足如下条件才可以融合：

- Conv2D：small channel开启，kernel需为3\*3，5\*5或7\*7，strides需为\[1, 1\]或\[2, 2\]，cout ≤ 64。
- MaxPool：strides = \[2, 2\], ksize = \[2, 2\]/\[3, 3\]。
- 当MaxPool ksize = \[2, 2\]时，Conv2D input width超过1000不启用该融合。
- 当MaxPool ksize = \[3, 3\]时，Conv2D input width超过800不启用该融合。
- Pooling：strides = \[2, 2\], window= \[2, 2\]/\[3, 3\]。
- 当Pooling window = \[2, 2\]时，Conv2D input width超过1000不启用该融合。
- 当Pooling window = \[3, 3\]时，Conv2D input width超过800不启用该融合。

<!-- npu="310p" id1 -->
Maxpoolv3满足如下条件才可以融合:

- soc：Atlas 推理系列加速卡产品
- conv2d：

    （1）输入参数的format为NCHW

    （2）fmap的shape为\[N,3,224,224\]，N为任意合法输入

    （3）filter的shape为\[N,3,7,7\]，N为1\~96

    （3）pads的shape为\[3,3,3,3\]

    （4）strides的shape为\[N,N,2,2\]，N为任意合法输入

    （5）dilations的shape为\[N,N,1,1\]，N为任意合法输入

    （6）groups为1

- maxpoolv3:

    （1）输入参数的format为NCHW

    （2）strides的shape为\[N,N,2,2\]，N为任意合法输入

    （3）ksize的shape为\[N,N,3,3\]，N为任意合法输入

    （4）padding\_mode为CALCULATED

    （5）pads的shape为\[1,1,1,1\]

    （6）global\_pooling为false

    （7）ceil\_mode为false

- aipp:开启C04
- elemwise：仅支持Relu和LeakyRelu
<!-- end id1 -->

## 支持的型号

<!-- npu="310b" id1 -->
Atlas 200I/500 A2 推理产品
<!-- end id1 -->

<!-- npu="310p" id2 -->
Atlas 推理系列产品
<!-- end id2 -->

<!-- npu="910" id3 -->
Atlas 训练系列产品
<!-- end id3 -->
