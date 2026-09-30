# JPEGD图片解码

JPEGD（JPEG Decoder）负责完成图像解码功能，将.jpg、.jpeg、.JPG、.JPEG图片解码成YUV格式图片。关于JPEGD功能的详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节介绍JPEGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

## 接口调用流程

开发应用时，如果涉及对JPEG图片的解码，则应用程序中必须包含图片解码的代码逻辑，**关于图片解码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明**。

**图 1**  JPEG图片解码
![](figures/JPEGD_API_call_process_V1.png "JPEG图片解码")

当前系统支持.jpg、.jpeg、.JPG、.JPEG图片的解码，针对不同的源图编码格式，输出不同编码格式的图片，关键接口的说明如下：

1. 调用`acl.media.dvpp_create_channel_desc`接口**创建通道描述信息**。
2. 调用`acl.media.dvpp_create_channel`接口**创建图片数据处理的通道**。
3. 实现JPEG图片解码功能前，**若需要申请Device上的内存**存放输入或输出数据，需调用`acl.media.dvpp_malloc`申请内存。

    **在申请输出内存前**，可根据存放JPEG图片数据的内存，调用`acl.media.dvpp_jpeg_predict_dec_size`接口**预估JPEG图片解码后所需的输出内存的大小**。

4. 调用`acl.media.dvpp_jpeg_decode_async`异步接口进行解码。

    对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。

5. 在解码结束后，需及时调用`acl.media.dvpp_free`接口**释放输入、输出内存**。
6. 调用`acl.media.dvpp_destroy_channel`接口**销毁图片数据处理的通道**。

    销毁图片数据处理的通道后，再调用`acl.media.dvpp_destroy_channel_desc`接口销毁通道描述信息。

## 示例代码

您可以从[获取样例](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)中获取完整样例代码。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行时资源申请。
# 3.创建图片数据处理通道时的通道描述信息，self.dvpp_channel_desc是acldvppChannelDesc类型。
self.dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 4.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(self.dvpp_channel_desc)

# 5.申请内存。
# 加载 YUV格式的图片数据。
# 申请Device内存inputDevBuff。
# 将通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时释放Host内存。
np_jpg = np.fromfile(self.path, dtype=np.byte)
self.in_buffer_size = np_jpg.itemsize * np_jpg.size
bytes_data = np_jpg.tobytes()
np_jpg_ptr = acl.util.bytes_to_ptr(bytes_data)
self.in_buffer_dev, ret = acl.media.dvpp_malloc(self.in_buffer_size)
ret = acl.rt.memcpy(self.in_buffer_dev, self.in_buffer_size, np_jpg_ptr,
                     self.in_buffer_size, 1)

# 6.输出内存，按16对齐方式计算并申请Device内存self.out_buffer_dev,存放编码后的输出数据。
height_stride = ((h + 1) // 2) * 2
width_stride = ((w + 15) // 16) * 16
# malloc for output
self.out_buffer_size = (width_stride * height_stride * 3) // 2
self.out_buffer_dev, ret = acl.media.dvpp_malloc(self.out_buffer_size)

# 7.创建解码输出图片的描述信息，设置各属性值。
# 解码设置输出内存和size到图片描述，用于数据占位。
self.pic_desc = acl.media.dvpp_create_pic_desc()
ret = acl.media.dvpp_set_pic_desc_data(self.pic_desc, self.out_buffer_dev)
ret = acl.media.dvpp_set_pic_desc_size(self.pic_desc, self.out_buffer_size)
ret = acl.media.dvpp_set_pic_desc_format(
            self.pic_desc, PIXEL_FORMAT_YUV_SEMIPLANAR_420)
ret = acl.media.dvpp_set_pic_desc_width(self.pic_desc, w)
ret = acl.media.dvpp_set_pic_desc_height(self.pic_desc, h)
ret = acl.media.dvpp_set_pic_desc_width_stride(self.pic_desc, width_stride)
ret = acl.media.dvpp_set_pic_desc_height_stride(self.pic_desc, height_stride)

# 8.执行异步解码，再调用acl.rt.synchronize_stream接口阻塞Host运行，直到指定Stream中的所有任务都完成。
ret = acl.media.dvpp_jpeg_decode_async(self.dvpp_channel_desc,
                                           self.in_buffer_dev,
                                           self.in_buffer_size,
                                           self.pic_desc, self.stream)
ret = acl.rt.synchronize_stream(self.stream)

# 9.解码结束后，释放资源，包括解码输出图片的描述信息、解码输出内存、通道描述信息、通道等。
ret = acl.media.dvpp_destroy_pic_desc(self.pic_desc)
ret = acl.media.dvpp_free(self.in_buffer_dev)
ret = acl.media.dvpp_free(self.out_buffer_dev)
ret = acl.media.dvpp_destroy_channel(self.dvpp_channel_desc)
ret = acl.media.dvpp_destroy_channel_desc(self.dvpp_channel_desc)

# 10.释放运行时资源。
# 去初始化。
ret = acl.finalize()

# ......
```
