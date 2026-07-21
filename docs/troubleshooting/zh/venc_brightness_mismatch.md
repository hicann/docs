# 播放VENC编码的码流，亮暗与原始YUV不一致

## 问题现象描述

用户使用第三方播放器播放经过VENC编码的码流，发现编码后的码流亮暗与原始YUV不一致。

## 可能原因

由于播放器的渲染效果不可控，播放器在解码、显示码流内容时，播放器的目标像素值域范围与VENC编码时设置的video\_full\_range\_flag标志位不一致，导致发生像素值域映射，进而出现码流亮暗与原始YUV不一致。

关于full\_range的原理介绍请参见[参考信息](#section98371392323)。

## 处理步骤

不建议用播放器验收亮暗效果，因为播放器的渲染效果不可控，建议将VENC码流解码为YUV文件后再与原始YUV对比，同时需确保编码和解码时使用一致的video\_full\_range\_flag标志位。

1. 在VENC编码时，指定video\_full\_range\_flag参数值。

    在Atlas 推理系列产品上，对于H.264、H.265码流，当前VENC编码时video\_full\_range\_flag默认值为0（表示limited\_range）。

    在Atlas 200I/500 A2 推理产品上，对于H.265码流，当前VENC编码时video\_full\_range\_flag默认值为0（表示limited\_range）；对于H.264码流，当前VENC编码时video\_full\_range\_flag默认值为1（表示full\_range）。

    **若默认值不满足要求，用户可以调用hi\_mpi\_venc\_set\_h264\_vui或hi\_mpi\_venc\_set\_h265\_vui接口修改video\_full\_range\_flag参数值。**

2. 确认VENC编码后码流的video\_full\_range\_flag标志位。

    通过码流分析工具查看SPS字段的video\_full\_range\_flag，flag=1表示原始YUV是full\_range的，flag=0表示是limited\_range的。

    ![](figures/zh-cn_image_0000001927915793.png)

3. 解码时指定video\_full\_range\_flag，然后再将解码后YUV文件与原始YUV对比亮暗。

    不同解码器的video\_full\_range\_flag使用方式不同，此处仅以FFmpeg为例，可以通过-vf参数指定目标输出video\_full\_range\_flag，默认为输出limited\_range。

    此处以ffmpeg为例，示例指令如下，供参考：

    ```bash
    ffmpeg -i ${instream} -pix_fmt nv12 -vf scale=out_range=full/limited -y ${outyuv}
    ```

    **此处举例说明亮暗对比情况。**现在的YUV一般都是full\_range的，暂时排除源YUV本身为limited\_range的情况，考虑Venc和FFmpeg参数组合4种情况，vui表示VENC编码时设置的video\_full\_range\_flag，ffmpeg表示FFmpeg解码时设置的video\_full\_range\_flag：

    - **vui0\_ffmpeg0**和**vui1\_ffmpeg1**结果一致，并且对比过源YUV也是一致的，这是因为vui和ffmpeg参数一致，直接解压输出YUV；
    - **vui0\_ffmpeg1**图像“更暗”，这是因为ffmpeg认为需要从limited\_range转换为full\_range，所以对像素值分布进行了往两侧拉伸，而该场景本身偏暗，像素值更多地往0值靠拢，表现为变暗；
    - **vui1\_ffmpeg0**图像“更亮”，因为ffmpeg做了标准的值域压缩，从0\~255压到16\~235，图中大量低像素值往中间区间抬升，图像表现为变亮。

    ![](figures/zh-cn_image_0000001927835405.png)

<a id="section98371392323"></a>

## 参考信息

电视机一般支持240个色阶，从16\~255，也就是**limited\_range**，对应YUV值域：Y\[16, 235\]，UV \[16, 240\]。

现代电脑显示支持255个色阶，从0\~255，也就是**full\_range**，对应YUV值域：YUV\[0, 255\]。

以下标记等价，是在不同软件或者模块中各自的表达方式：

- **“full range” = “jpeg” = “pc” = “cg” = “high rgb”**
- **“limited range” = “mpeg” = “tv” = “broadcast” = “low rgb”**

H.265码流中VUI字段的video\_full\_range\_flag = 0表示源YUV是limited\_range，video\_full\_range\_flag = 1表示源YUV是full\_range。注意**这个标记位不影响VENC编码过程**，编码生成的码流数据只由输入YUV的实际像素值决定，编码阶段不会发生像素值映射。

例如，ffmpeg解码时会判断源YUV格式和输出YUV格式是否匹配，**仅在两者不匹配时触发像素值重映射**。当原始YUV是full\_range的，此时VENC编码设置了video\_full\_range\_flag = 1，若ffmpeg解码输出YUV格式是limited\_range的，它发现YUV格式从full\_range降为limited\_range，于是在解码后对像素值进行了映射，从 \[0, 255\] 缩小到 \[16, 235\]，此时就会发现解出来的YUV和原始YUV存在亮暗差异。
