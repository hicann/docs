# 媒体数据处理基础知识

本章主要介绍图像/视频数据处理的具体功能、接口调用流程以及示例代码。

## 典型功能介绍

CANN提供了**AIPP**和**DVPP**两种处理图像/视频数据的方式，本章主要介绍基于DVPP的图像/视频数据处理。

| 处理方式 | 描述 |
|---------|------|
| **AIPP**(Artificial Intelligence Pre-Processing) | AIPP人工智能预处理，在AI Core上完成数据预处理，主要功能包括改变图像尺寸（抠图、填充等）、色域转换（转换图像格式）、减均值/乘系数（改变图像像素）等。<br>AIPP分为静态AIPP和动态AIPP。您只能选择静态AIPP或动态AIPP中的一种来处理图片，不能同时配置静态AIPP和动态AIPP两种方式。<br>**静态AIPP**：模型转换时设置AIPP模式为静态，同时设置AIPP参数，模型生成后，AIPP参数值被保存在离线模型（*.om）中，每次模型推理过程采用固定的AIPP预处理参数（无法修改）。如果使用静态AIPP方式，多Batch情况下共用同一份AIPP参数，AIPP参数值在使用ATC工具进行模型转换时设置，ATC工具的详细说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)。<br>**动态AIPP**：模型转换时仅设置AIPP模式为动态，每次模型推理前，根据需求，在执行模型前设置动态AIPP参数值，然后在模型执行时可使用不同的AIPP参数。如果使用动态AIPP方式，多Batch可使用不同的AIPP参数，各Batch所使用的AIPP参数值通过pyacl提供的接口来设置，请参见[模型动态AIPP推理](dynamic_AIPP_inference.md)中的介绍。 |
| **DVPP**（Digital Vision Pre-Processing） | DVPP是AI处理器内置的图像处理单元，通过媒体数据处理接口提供强大的媒体处理硬加速能力，主要功能包括以下功能：<br>**VPC**（Vision Preprocessing Core）：处理YUV、RGB等格式的图片，包括缩放、抠图、色域转换等。<br>**JPEGD**（JPEG Decoder）：JPEG压缩格式-->YUV格式的图片解码。<br>**JPEGE**（JPEG Encoder）：YUV格式-->JPEG压缩格式的图片编码。<br>**VDEC**（Video Decoder）：H.264/H.265格式-->YUV/RGB格式的视频码流解码。<br>**VENC**（Video Encoder）：YUV420SP格式-->H.264/H.265格式的视频码流编码。<br>**PNGD**（PNG Decoder）：PNG格式-->RGB格式的图片解码。<br>AIPP、DVPP可以分开独立使用，也可以组合使用。组合使用场景下，一般先使用DVPP对图片/视频进行解码、抠图、缩放等基本处理，但由于DVPP硬件上的约束，DVPP处理后的图片格式、分辨率有可能不满足模型的要求，因此还需要再经过AIPP进一步做色域转换、抠图、填充等处理。 |

## DVPP图像/视频数据处理的典型使用场景

如果源图或视频的分辨率、格式等与模型的要求不一致时，我们可以将源图或视频处理成符合模型的要求。如下为**典型场景的举例**。

- **视频解码、缩放**。

    使用YOLOv3模型实现目标检测的场景下，用户提供的输入视频为H.264/H.265编码格式、分辨率为1920\*1080，但YOLOv3模型要求的输入图片格式为RGB/YUV、分辨率为416\*416，两者不一致，此时可对视频执行以下一系列处理。

    **图 1**  视频解码、缩放使用场景图
    ![](figures/video_decoding_resizing.png "视频解码-缩放使用场景图")

- **图片解码、缩放、格式转换**。

    使用ResNet-50模型实现图片分类的场景下，用户提供的输入图片为JPEG编码格式、分辨率为1280\*720，但ResNet-50模型要求的输入图片格式为RGB、分辨率为224\*224，两者不一致，此时可对图片执行以下一系列处理。

    **图 2**  图片解码、缩放、格式转换使用场景图
    ![](figures/image_decoding_resizing_format_conversion.png "图片解码-缩放-格式转换使用场景图")

- **抠图、缩放、格式转换**。

    使用ResNet-50模型实现图片分类的场景下，用户提供的输入图片格式为YUV420SP、分辨率为1280\*720，但ResNet-50模型要求的输入图片格式为RGB、分辨率为224\*224，两者不一致，此时对图片执行以下一系列处理。

    **图 3**  抠图、缩放、格式转换使用场景图
    ![](figures/image_crop_resize_format_conversion.png "抠图-缩放-格式转换使用场景图")

## 媒体数据处理功能开发流程

**图 4**  开发流程
![](figures/DVPP_development_process.png "开发流程-4")

1. **准备环境**。

    请参见[环境准备](environment_preparation.md)。

2. **创建代码目录**。

    在开发应用前，您需要先创建目录，存放代码文件、脚本、测试图片数据、模型文件等。

    模型推理场景下，必须要有适配AI处理器的离线模型（*.om文件），请参见[模型构建](model_construction.md)。

    >[!NOTE] 说明
    >如果应用中涉及模型推理，则需要构建模型。

3. **开发应用**。

    如果应用中涉及模型推理，请参见[模型管理](model_management.md)编写相应的代码。

4. **运行应用**，请参见[应用调试](app_debug.md)。
