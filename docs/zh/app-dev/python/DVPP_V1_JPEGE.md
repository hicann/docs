# JPEGE图片编码

JPEGE（JPEG Encoder）负责完成图像编码功能，将YUV格式图片编码成.jpg图片。关于JPEGE功能的详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍JPEGE图片编码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程

开发应用时，如果涉及将YUV格式图片编码成JPEG压缩格式的图片文件，则应用程序中必须包含图片编码的代码逻辑，关于图片编码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。

**图 1**  JPEG图片编码
![](figures/JPEG_API_call_process_V1.png "JPEG图片编码")

当前系统支持将YUV格式图片编码成.jpg图片，关键接口的说明如下：

1. 调用`acl.media.dvpp_create_channel_desc`接口**创建通道描述信息**。
2. 调用`acl.media.dvpp_create_channel`接口**创建图片数据处理的通道**。
3. 调用`acl.media.dvpp_create_jpege_config`接口**创建图片编码配置数据**。
4. 实现JPEG图片编码功能前，**若需要申请Device上的内存存放输入或输出数据**，需调用`acl.media.dvpp_malloc`申请内存。

    **在申请输出内存前**，可调用`acl.media.dvpp_jpeg_predict_enc_size`接口根据输入图片描述信息、图片编码配置数据**预估图片编码后所需的输出内存的大小**。

5. 调用`acl.media.dvpp_jpeg_encode_async`异步接口进行编码。

    对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。

6. 调用`acl.media.dvpp_destroy_jpege_config`接口**销毁图片编码配置数据**。
7. 在编码结束后，需及时调用`acl.media.dvpp_free`接口**释放输入、输出内存**。
8. 调用`acl.media.dvpp_destroy_channel`接口**销毁图片数据处理的通道**。

    **销毁图片数据处理的通道后**，再调用`acl.media.dvpp_destroy_channel_desc`接口**销毁通道描述信息**。

## 示例代码

您可以从[获取样例](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)中获取完整样例代码。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行管理资源申请。
# 3.创建图片数据处理通道时的通道描述信息，self.dvpp_channel_desc是acldvppChannelDesc类型。
self.dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 4.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(self.dvpp_channel_desc)

# 5.申请内存。
# 5.1 输入内存。
#  加载 YUV格式的图片数据,将通过acl.rt.memcpy接口将Host的图片数据传输到Device。
np_jpg = np.fromfile(self.path, dtype=np.byte)
self.in_buffer_size = np_jpg.itemsize * np_jpg.size
bytes_data = np_jpg.tobytes()
np_jpg_ptr = acl.util.bytes_to_ptr(bytes_data)
self.in_buffer_dev, ret = acl.media.dvpp_malloc(self.in_buffer_size)
ret = acl.rt.memcpy(self.in_buffer_dev, self.in_buffer_size, np_jpg_ptr,
                    self.in_buffer_size, 1)

# 5.2 输出内存，按16对齐方式计算并申请Device内存self.out_buffer_dev,存放编码后的输出数据。
height_stride = ((h + 1) // 2) * 2
width_stride = ((w + 15) // 16) * 16
# malloc for output
self.out_buffer_size = (width_stride * height_stride * 3) // 2
self.out_buffer_dev, ret = acl.media.dvpp_malloc(self.out_buffer_size)

# 6. 创建编码输入图片的描述信息，并设置各属性值。
# jpeg 编码设置输入yuv图片数据及size到图片描述。
self.pic_desc = acl.media.dvpp_create_pic_desc()
ret = acl.media.dvpp_set_pic_desc_data(self.pic_desc, self.in_buffer_dev)
ret = acl.media.dvpp_set_pic_desc_size(self.pic_desc, self.in_buffer_size)
ret = acl.media.dvpp_set_pic_desc_format(self.pic_desc, PIXEL_FORMAT_YUV_SEMIPLANAR_420)
ret = acl.media.dvpp_set_pic_desc_width(self.pic_desc, w)
ret = acl.media.dvpp_set_pic_desc_height(self.pic_desc, h)
ret = acl.media.dvpp_set_pic_desc_width_stride(self.pic_desc, width_stride)
ret = acl.media.dvpp_set_pic_desc_height_stride(self.pic_desc, height_stride)

# 7. 创建图片编码配置数据，设置编码质量, 预测输出的图片尺寸并分配内存。
# 编码质量范围[0, 100]，其中level 0编码质量与level 100相近，而在[1, 100]内数值越小输出图片质量越差。
self.jpege_config = acl.media.dvpp_create_jpege_config()
ret = acl.media.dvpp_set_jpege_config_level(self.jpege_config, 100)
self.out_buffer_size, ret = acl.media.dvpp_jpeg_predict_enc_size(
         self.pic_desc, self.jpege_config)
self.out_buffer_dev, ret = acl.media.dvpp_malloc(self.out_buffer_size)

# 8. 执行异步编码，再调用acl.rt.synchronize_stream接口阻塞Host运行，直到指定Stream中的所有任务都完成。
acl.rt.set_context(self.context)
np_out_size = np.array([self.out_buffer_size], dtype=np.int32)
bytes_data = np_out_size.tobytes()
np_out_size_ptr = acl.util.bytes_to_ptr(bytes_data)
ret = acl.media.dvpp_jpeg_encode_async(self.dvpp_channel_desc, self.pic_desc,
                                       self.out_buffer_dev, np_out_size_ptr,
                                       self.jpege_config, self.stream)
ret = acl.rt.synchronize_stream(self.stream)

# 9.申请Host内存hostPtr。
# 9.1 将编码后的输出图片回传到Host，再将Host内存中的数据写入文件,写完文件后，需及时调用acl.rt.free_host接口释放Host内存。
# 9.2 创建numpy对象并转成host侧数据存储输出内容。
np_output = np.zeros(size, dtype=np.byte)
bytes_data = np_output.tobytes()
np_output_ptr = acl.util.bytes_to_ptr(bytes_data)
size = int(np_out_size[0])
ret = acl.rt.memcpy(np_output_ptr, size, self.out_buffer_dev, size, 2)

# 10. 编码结束后，释放资源，包括编码输入/输出图片的描述信息、编码输入/输出内存、通道描述信息、通道等。
ret = acl.media.dvpp_destroy_jpege_config(self.jpege_config)
ret = acl.media.dvpp_destroy_pic_desc(self.pic_desc)
ret = acl.media.dvpp_free(self.in_buffer_dev)
ret = acl.media.dvpp_free(self.out_buffer_dev)
ret = acl.media.dvpp_destroy_channel(self.dvpp_channel_desc)
ret = acl.media.dvpp_destroy_channel_desc(self.dvpp_channel_desc)

# 11. 释放运行管理资源。
# 去初始化。
ret = acl.finalize()
# ....
```
