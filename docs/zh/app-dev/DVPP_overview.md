# 媒体数据处理功能简介

本章主要介绍图像/视频/音频数据处理的具体功能、接口调用流程以及示例代码。

## 图像/视频/音频数据处理的典型功能介绍

<!-- npu="310b" id1 -->
**图 1**  图像/视频数据处理  
![](figures/image_video_data_processing.png "图像-视频数据处理")
<!-- end id1 -->

各功能的介绍如下表所示，各产品型号上媒体数据处理各功能的支持度请参见[各产品型号功能支持情况](functions_supported_status.md)，其中，AIPP当前各版本均支持。

| 功能 | 子功能模块 | 描述 |
| --- | --- | --- |
| 图像数据处理 | AIPP（Artificial Intelligence Pre-Processing） | AIPP人工智能预处理，在AI Core上完成数据预处理，主要功能包括改变图像尺寸（抠图、填充等）、色域转换（转换图像格式）、减均值/乘系数（改变图像像素）等。<br>AIPP分为静态AIPP和动态AIPP。您只能选择静态AIPP或动态AIPP中的一种来处理图片，不能同时配置静态AIPP和动态AIPP两种方式。<br>  - 静态AIPP：模型转换时设置AIPP模式为静态，同时设置AIPP参数，模型生成后，AIPP参数值被保存在离线模型（*.om）中，每次模型推理过程采用固定的AIPP预处理参数（无法修改）。如果使用静态AIPP方式，多Batch情况下共用同一份AIPP参数，AIPP参数值在使用ATC工具进行模型转换时设置，ATC工具的详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。<br>  - 动态AIPP：模型转换时仅设置AIPP模式为动态，每次模型推理前，根据需求，在执行模型前设置动态AIPP参数值，然后在模型执行时可使用不同的AIPP参数。 |
| 图像/视频数据处理 | DVPP（Digital Vision Pre-Processing） | DVPP是AI处理器内置的图像处理单元，通过媒体数据处理接口提供强大的媒体处理硬加速能力，主要功能包括以下功能：<br><br>  - VPC（Vision Preprocessing Core）：处理YUV、RGB等格式的图片，包括缩放、抠图、图像金字塔、色域转换等。<br>  - JPEGD（JPEG Decoder）：JPEG压缩格式-->YUV格式的图片解码。<br>  - JPEGE（JPEG Encoder）：YUV格式-->JPEG压缩格式的图片编码。<br>  - VDEC（Video Decoder）：H264/H265格式-->YUV/RGB格式的视频码流解码。<br>  - VENC（Video Encoder）：YUV420SP格式-->H264/H265格式的视频码流编码。<br>  - PNGD（PNG Decoder）：PNG格式-->RGB格式的图片解码。<br><br><br>AIPP、DVPP可以分开独立使用，也可以组合使用。组合使用场景下，一般先使用DVPP对图片/视频进行解码、抠图、缩放等基本处理，但由于DVPP硬件上的约束，DVPP处理后的图片格式、分辨率有可能不满足模型的要求，因此还需要再经过AIPP进一步做色域转换、抠图、填充等处理。 |

<!-- npu="310b" id2 -->
<br>

Atlas 200I/500 A2 推理产品上还支持以下功能：

| 功能 | 子功能模块 | 描述 |
| --- | --- | --- |
| 获取视频数据 | ISP（Image Signal Processing）系统控制 | 系统控制部分用于注册3A算法、注册Sensor驱动、初始化ISP firmware、运行ISP firmware、退出ISP firmware、配置ISP属性等功能。 |
| 获取视频数据 | MIPI Rx ioctl命令字 | MIPI Rx是一个支持多种差分视频输入接口的采集单元，通过combo-PHY接收MIPI/LVDS/sub-LVDS/HiSPi接口的数据，通过不同的功能模式配置，MIPI Rx可以支持多种速度和分辨率的数据传输需求，支持多种外部输入设备。 |
| 获取视频数据 | VI（Video Input） | VI模块捕获视频图像，可对其做裁剪、颜色优化、亮度优化、噪声去除等处理，并输出YUV或RAW格式的图像数据。 |
| 展示视频数据 | VO（Video Output） | VO模块接收VPSS处理后的输出图像，可进行播放控制等处理，最后按用户配置的输出协议（当前仅支持HDMI）输出给外围视频设备。<br>VO可配合TDE（Two Dimensional Engine）模块、HIFB（Hisilicon Framebuffer）模块，利用硬件分别进行图形绘制、叠加图形层管理。 |
| 展示视频数据 | HDMI（High Definition Multimedia Interface） | HDMI是全数字化影像和声音发送接口，可以发送未压缩的音频及视频信号。 |
| 展示视频数据 | TDE（Two Dimensional Engine） | TDE是图形二维加速引擎，它利用硬件为OSD（On Screen Display）和GUI（Graphical User Interface）提供快速的图形绘制功能，主要有快速拷贝、快速色彩填充、模式填充（当前仅支持Alpha Blending操作）。 |
| 展示视频数据 | HIFB（Hisilicon Framebuffer） | HIFB用于管理叠加图形层，它不仅提供Linux Framebuffer的基本功能，还在Linux Framebuffer的基础上增加图层显示起始位置修改、层间Alpha等扩展功能。 |
| 区域管理 | Region | 叠加在视频上的OSD (On Screen Display)和遮挡在视频上的色块统称为区域。区域管理模块，用于统一管理这些区域资源，用于在视频上显示一些特定信息（如通道号、时间戳等）、或在视频中填充色块用于遮挡，当前该功能需配合VPSS一起使用。 |
| 图像/视频数据处理 | VPSS（Video Process Sub-System） | VPSS模块支持对输入图像进行统一预处理，如去噪、去隔行、裁剪等，然后再对各通道分别进行处理，如缩放、加边框等。 |
| 音频数据获取和输出 | AI（Audio Input） | AI模块捕获音频数据。 |
| AO（Audio Output） | 通过ADEC模块解码后的音频数据，AO模块支持播放音频。 |  |
| 音频数据编解码 | AENC（Audio Encoder） | 通过AI模块获取的音频数据，AENC模块支持对其进行编码，输出音频码流。 |
| 音频数据编解码 | ADEC（Audio Decoder） | ADEC支持解码G.711a、G.711u等协议的音频码流，再通过AO模块播放音频。 |
<!-- end id2 -->

## DVPP图像/视频数据处理的典型使用场景

如果源图或视频的分辨率、格式等与模型的要求不一致时，我们可以将源图或视频处理成符合模型的要求。如下为**典型场景**的举例。

- **视频解码、缩放**

    使用Yolov3模型实现目标检测的场景下，用户提供的输入视频为H264编码格式、分辨率为1920\*1080，但Yolov3模型要求的输入图片格式为RGB/YUV、分辨率为416\*416，两者不一致，此时可对视频执行以下一系列处理。

    **图 2**  视频解码、缩放使用场景图  
    ![](figures/video_decoding_resizing.png "视频解码-缩放使用场景图")

- **图片解码、缩放、格式转换**

    使用Resnet50模型实现图片分类的场景下，用户提供的输入图片为JPEG编码格式、分辨率为1280\*720，但Resnet50模型要求的输入图片格式为RGB、分辨率为224\*224，两者不一致，此时可对图片执行以下一系列处理。

    **图 3**  图片解码、缩放、格式转换使用场景图  
    ![](figures/image_decoding_resizing_format_conversion.png "图片解码-缩放-格式转换使用场景图")

- **抠图、缩放、格式转换**

    使用Resnet50模型实现图片分类的场景下，用户提供的输入图片格式为YUV420SP、分辨率为1280\*720，但Resnet50模型要求的输入图片格式为RGB、分辨率为224\*224，两者不一致，此时对图片执行以下一系列处理。

    **图 4**  抠图、缩放、格式转换使用场景图  
    ![](figures/image_crop_resize_format_conversion.png "抠图-缩放-格式转换使用场景图")
