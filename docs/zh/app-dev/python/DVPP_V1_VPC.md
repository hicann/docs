# VPC图像处理典型功能

**VPC**（Vision Preprocessing Core）负责图像处理功能，支持对图片做抠图、缩放、格式转换等操作。关于VPC功能详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节以抠图、缩放为例说明VPC图像处理时的接口调用流程，同时配合以下典型功能的示例代码辅助理解该接口调用流程：

- [图片缩放示例代码](#图片缩放示例代码)
- [格式转换示例代码](#格式转换示例代码)
- [抠图缩放（一图一框）示例代码](#抠图缩放一图一框示例代码)
- [抠图贴图缩放（一图一框）示例代码](#抠图贴图缩放一图一框示例代码)
- [抠图贴图（一图多框）示例代码](#抠图贴图一图多框示例代码)

## 接口调用流程（以抠图、缩放为例）

开发应用时，如果涉及抠图、缩放等图片处理，则应用程序中必须包含图片处理的代码逻辑，**关于图片处理的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明**。

**图 1**  抠图缩放流程
![](figures/image_crop_resize_process.png "抠图缩放流程")

关键接口的说明如下（以抠图、缩放处理为例）：

1. 调用`acl.media.dvpp_create_channel_desc`接口**创建通道描述信息**。
2. 调用`acl.media.dvpp_create_channel`接口**创建图片数据处理的通道**。
3. 调用`acl.media.dvpp_create_roi_config`接口、`acl.media.dvpp_create_resize_config`接口分别**创建抠图区域位置的配置、缩放配置**。
4. 实现抠图、缩放功能前，**若需要申请Device上的内存**存放输入或输出数据，需调用`acl.media.dvpp_malloc`申请内存。
5. **执行抠图、缩放**。
    - 关于抠图：
        - 调用`acl.media.dvpp_vpc_crop_async`异步接口，按指定区域从输入图片中抠图，再将抠的图片存放到输出内存中，作为输出图片。

            输出图片区域与抠图区域“crop_area”不一致时会对图片再做一次缩放操作。

        - 当前系统还提供了`acl.media.dvpp_vpc_crop_and_paste_async`异步接口，支持按指定区域从输入图片中抠图，再将抠的图片贴到目标图片的指定位置，作为输出图片。
            - 抠图区域“crop_area”的宽高与贴图区域“paste_area”宽高不一致时会对图片再做一次缩放操作。
            - 如果用户需要将目标图片读入内存用于存放输出图片，将贴图区域叠加在目标图片上，则需要编写代码逻辑：**在申请输出内存后，将目标图片读入输出内存**。

    - 关于缩放：
        - 调用`acl.media.dvpp_vpc_resize_async`异步接口，将**输入图片缩放到输出图片大小**。
        - 缩放后输出图片内存根据YUV420SP格式计算，计算公式：**对齐后的宽 \* 对齐后的高 \* 3 / 2**。

    - 对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。

6. 调用`acl.media.dvpp_free`接口**释放输入、输出内存**。
7. 调用`acl.media.dvpp_destroy_roi_config`接口、`acl.media.dvpp_destroy_resize_config`接口分别**销毁抠图区域位置的配置、缩放配置**。
8. 调用`acl.media.dvpp_destroy_channel`接口**销毁图片数据处理的通道**。

    销毁图片数据处理的通道后，再调用`acl.media.dvpp_destroy_channel_desc`接口销毁通道描述信息。

## 图片缩放示例代码

- 调用`acl.media.dvpp_create_channel`接口创建图片数据处理的通道、调用`acl.media.dvpp_destroy_channel`接口销毁图片数据处理的通道。
- 调用`acl.media.dvpp_vpc_resize_async`异步接口，将输入图片缩放到输出图片大小。对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。

- 调用`acl.media.dvpp_create_resize_config`接口创建图片缩放配置数据。

    如果不想使用默认缩放算法，也可以调用`acl.media.dvpp_set_resize_config_interpolation`接口指定缩放算法。
<!-- npu="910b,910,310p,310b" id2 -->
您可以从[基于Caffe ResNet-50网络实现图片分类（图片解码+缩放+同步推理）](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vpc_resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id2 -->
调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行时资源申请。
# 3.创建图片缩放配置数据，不支持指定缩放算法，默认缩放算法为“最近邻插值”。
# self.resize_config是acldvppResizeConfig类型。
self.resize_config = acl.media.dvpp_create_resize_config()

# 4.创建图片数据处理通道时的通道描述信息，self.dvpp_channel_desc是acldvppChannelDesc类型。
self.dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 5.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(self.dvpp_channel_desc)

# 6.申请缩放输入内存，内存大小根据计算公式得出; w和h是输入图片的实际尺寸。
width_stride = ((w + 15) // 16) * 16
height_stride = ((h + 1) // 2) * 2
buffer_size = (width_stride * height_stride * 3) // 2
dev_in, ret = acl.media.dvpp_malloc(buffer_size )
self.dev_buffer['input_0'] = dev
# 7.申请缩放输出内存，内存大小根据计算公式得出; w和h是输入图片的缩放尺寸。
width_stride = ((w + 15) // 16) * 16
height_stride = ((h + 1) // 2) * 2
buffer_size = (width_stride * height_stride * 3) // 2
dev_out, ret = acl.media.dvpp_malloc(buffer_size )
self.dev_buffer['output_0'] = dev_out

# 8.创建缩放输入图片的描述信息，并设置各属性值。
# self.input_desc是acldvppPicDesc类型。
self.input_desc = acl.media.dvpp_create_pic_desc()
ret = acl.media.dvpp_set_pic_desc_data(self.input_desc, buffer)
ret = acl.media.dvpp_set_pic_desc_format(self.input_desc, YUV420)
ret = acl.media.dvpp_set_pic_desc_width(self.input_desc, width)
ret = acl.media.dvpp_set_pic_desc_height(self.input_desc, height)
ret = acl.media.dvpp_set_pic_desc_width_stride(self.input_desc, wstride)
ret = acl.media.dvpp_set_pic_desc_height_stride(self.input_desc, hstride)
ret = acl.media.dvpp_set_pic_desc_size(self.input_desc, size)

# 9.创建缩放输出图片的描述信息，并设置各属性值。
# 如果缩放的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致。
# self.output_desc是acldvppPicDesc类型。
self.output_desc= acl.media.dvpp_create_pic_desc()
ret = acl.media.dvpp_set_pic_desc_data(self.output_desc, buffer)
ret = acl.media.dvpp_set_pic_desc_format(self.output_desc, YUV420)
ret = acl.media.dvpp_set_pic_desc_width(self.output_desc, width)
ret = acl.media.dvpp_set_pic_desc_height(self.output_desc, height)
ret = acl.media.dvpp_set_pic_desc_width_stride(self.output_desc, wstride)
ret = acl.media.dvpp_set_pic_desc_height_stride(self.output_desc, hstride)
ret = acl.media.dvpp_set_pic_desc_size(self.output_desc, size)

# 10.执行异步缩放，再调用acl.rt.synchronize_stream接口阻塞Host运行，直到指定Stream中的所有任务都完成。
ret = acl.media.dvpp_vpc_resize_async(self.dvpp_channel_desc, self.input_desc,
                                          self.output_desc, self.resize_config,
                                          self.stream)
ret = acl.rt.synchronize_stream(self.stream)

# 11.缩放结束后，释放资源，包括缩放输入/输出图片的描述信息、缩放输入/输出内存。
ret = acl.media.dvpp_destroy_pic_desc(self.output_desc)
ret = acl.media.dvpp_destroy_pic_desc(self.input_desc)
ret = acl.media.dvpp_free(self.dev_buffer['input_0'] )
ret = acl.media.dvpp_free(self.dev_buffer['output_0'] )

# 12.释放运行时资源。
# 去初始化。
ret = acl.finalize()
# ......
```

<!-- npu="910b,910,310p,310b" id3 -->
## 格式转换示例代码

格式转换支持以下两种实现方式：

- 在实现抠图、缩放等功能时，调用对应的接口（例如`acl.media.dvpp_vpc_crop_async`接口）时，**通过将输入图片和输出图片的格式设置成不同的，达到转换图片格式的目的**。
- 如果**仅进行图片格式转换**，也可以直接调用`acl.media.dvpp_vpc_convert_color_async`接口。

    以下是格式转换功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

ACL_MEMCPY_HOST_TO_DEVICE = 1
ACL_MEMCPY_DEVICE_TO_HOST = 2
PIXEL_FORMAT_YUV_400 = 0
PIXEL_FORMAT_YUV_SEMIPLANAR_420 = 1

# 1.初始化。
ret = acl.init()

# 2.运行时资源申请。
# 3.创建图片数据处理通道时的通道描述信息，dvpp_channel_desc是acldvppChannelDesc类型。
dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 4.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(dvpp_channel_desc)

# 5.申请输入内存。
input_width_stride = ((input_width + 15) // 16) * 16
input_height_stride = ((input_height + 1) // 2) * 2
# input_width_stride、input_height_stride分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例。
in_buffer_size = (input_width_stride * input_height_stride * 3) // 2
in_dev_buffer, ret = acl.media.dvpp_malloc(in_buffer_size)
np_yuv = np.fromfile(path, dtype=np.byte)
buffer_size = np_yuv.itemsize * np_yuv.size
bytes_data = np_yuv.tobytes()
np_yuv_ptr = acl.util.bytes_to_ptr(bytes_data)
ret = acl.rt.memcpy(in_dev_buffer, buffer_size, np_yuv_ptr,
                      buffer_size, ACL_MEMCPY_HOST_TO_DEVICE)

# 6.申请色域转换输出内存。
output_width_stride = ((output_width + 15) // 16) * 16
output_height_stride = ((output_height + 1) // 2) * 2
# output_width_stride、output_height_stride分别表示图片的对齐后宽、对齐后高，此处以YUV420SP格式的图片为例。
out_buffer_size = (output_width_stride * output_height_stride * 3) // 2
out_dev_buffer, ret = acl.media.dvpp_malloc(out_buffer_size)

# 7.创建色域转换输入图片的描述信息，并设置各属性值。
input_desc = acl.media.dvpp_create_pic_desc()
ret = acl.media.dvpp_set_pic_desc_data(input_desc, in_dev_buffer)
ret = acl.media.dvpp_set_pic_desc_format(input_desc, PIXEL_FORMAT_YUV_SEMIPLANAR_420)
ret = acl.media.dvpp_set_pic_desc_width(input_desc, input_width)
ret = acl.media.dvpp_set_pic_desc_height(input_desc, input_height)
ret = acl.media.dvpp_set_pic_desc_width_stride(input_desc, input_width_stride)
ret = acl.media.dvpp_set_pic_desc_height_stride(input_desc, input_height_stride)
ret = acl.media.dvpp_set_pic_desc_size(input_desc, in_buffer_size)

# 8.创建色域转换的输出图片的描述信息，并设置各属性值, 输出的宽和高要求和输入一致。
# 如果色域转换的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致。
output_desc = acl.media.dvpp_create_pic_desc()
ret = acl.media.dvpp_set_pic_desc_data(output_desc, out_dev_buffer)
ret = acl.media.dvpp_set_pic_desc_format(output_desc, PIXEL_FORMAT_YUV_400)
ret = acl.media.dvpp_set_pic_desc_width(output_desc, output_width)
ret = acl.media.dvpp_set_pic_desc_height(output_desc, output_height)
ret = acl.media.dvpp_set_pic_desc_width_stride(output_desc, output_width_stride)
ret = acl.media.dvpp_set_pic_desc_height_stride(output_desc, output_height_stride)
ret = acl.media.dvpp_set_pic_desc_size(output_desc, out_buffer_size)

# 9.执行异步色域转换，再调用acl.rt.synchronize_stream接口阻塞程序运行，直到指定Stream中的所有任务都完成。
ret = acl.media.dvpp_vpc_convert_color_async(dvpp_channel_desc, input_desc,
                                                  output_desc, stream)
ret = acl.rt.synchronize_stream(stream)

# 10.色域转换结束后，释放资源，包括输入/输出图片的描述信息、输入/输出内存。
ret = acl.media.dvpp_destroy_pic_desc(input_desc)
ret = acl.media.dvpp_destroy_pic_desc(output_desc)

np_output = np.zeros(out_buffer_size, dtype=np.byte)
bytes_data = np_output.tobytes()
np_output_ptr = acl.util.bytes_to_ptr(bytes_data)
# 将Device的处理结果数据传输到Host。
ret = acl.rt.memcpy(np_output_ptr, out_buffer_size, out_dev_buffer,
                     out_buffer_size, ACL_MEMCPY_DEVICE_TO_HOST)
ret = acl.media.dvpp_free(in_dev_buffer)
ret = acl.media.dvpp_free(out_dev_buffer)

# 11.释放运行时资源。
# 去初始化。
ret = acl.finalize()
# ......
```
<!-- end id3 -->
<!-- npu="910b,910,310p,310b" id4 -->
## 抠图缩放（一图一框）示例代码

调用`acl.media.dvpp_vpc_crop_async`异步接口，按指定区域从输入图片中抠图，再将抠的图片存放到输出内存中，作为输出图片。
<!-- npu="910b,910,310p,310b" id5 -->
您可以从[基于Caffe ResNet-50网络实现图片分类（图片解码+抠图缩放+图片编码+同步推理）](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id5 -->
调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行时资源申请。
# 3.指定抠图区域的位置、指定贴图区域的位置。
# 按左上角为原点做偏移。w，h为图片原始宽高。
self.crop_area = acl.media.dvpp_create_roi_config(w // 2, w - 1, h // 2, h - 1)

# 4.创建图片数据处理通道时的通道描述信息，dvpp_channel_desc 是acldvppChannelDesc类型。
self.dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 5.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(self.dvpp_channel_desc)

# 6.创建输入输出图片的描述信息，并设置各属性值。
self.input_desc = acl.media.dvpp_create_pic_desc()
assert self.input_desc is not None
# 6.1 自定义方法 set_picture_desc 设置输入图片描述。
# 根据计算公式计算内存大小存储图片数据，并设置到图片描述，同时设置其他属性。
self.set_picture_desc(self.input_desc, w, h, "input", 0)
self.output_desc = acl.media.dvpp_create_pic_desc()
assert self.output_desc is not None
# 6.2 自定义方法 set_picture_desc 设置输出图片描述。
out_buffer_size = self.set_picture_desc(self.output_desc, w // 2, h // 2, "output", 0)

# 7.执行异步抠图，再调用acl.rt.synchronize_stream接口阻塞Host运行，直到指定Stream中的所有任务都完成。
ret = acl.media.dvpp_vpc_crop_async(self.dvpp_channel_desc, self.input_desc, self.output_desc, self.crop_area, self.stream)
ret = acl.rt.synchronize_stream(self.stream)

# 8.释放资源，包括输入/输出图片的描述信息、输入/输出内存、通道描述信息、通道等。
ret = acl.media.dvpp_destroy_roi_config(self.crop_area)
ret = acl.media.dvpp_destroy_pic_desc(self.input_desc)
ret = acl.media.dvpp_destroy_pic_desc(self.output_desc)
# dev_buffer是字典对象，存储device侧申请内存。
for key in self.dev_buffer.keys():
    if self.dev_buffer[key]:
        ret = acl.media.dvpp_free(self.dev_buffer[key])
if self.dvpp_channel_desc:
    ret = acl.media.dvpp_destroy_channel(self.dvpp_channel_desc)
    assert ret == 0
    ret = acl.media.dvpp_destroy_channel_desc(self.dvpp_channel_desc)
    assert ret == 0

# 9.释放运行时资源。
# 10.去初始化。
ret = acl.finalize()
# ......
```
<!-- end id4 -->
<!-- npu="910b,910,310p,310b" id6 -->
## 抠图贴图缩放（一图一框）示例代码

- 调用`acl.media.dvpp_vpc_crop_resize_paste_async`异步接口，按指定区域从输入图片中抠图，再将抠的图片贴到目标图片的指定位置，作为输出图片。对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。

    调用`acl.media.dvpp_vpc_crop_resize_paste_async`实现抠图缩放贴图时，支持指定缩放算法。

- 抠图区域“crop_area”的宽高与贴图区域“paste_area”宽高不一致时会对图片再做一次缩放操作。
- 如果用户需要将目标图片读入内存用于存放输出图片，将贴图区域叠加在目标图片上，则需要编写代码逻辑：在申请输出内存后，将目标图片读入输出内存。
<!-- npu="910b,910,310p,310b" id7 -->
您可以从[基于Caffe ResNet-50网络实现图片分类（图片解码+抠图缩放+图片编码+同步推理）](https://gitee.com/ascend/samples/tree/master/python/level2_simple_inference/1_classification/vpc_jpeg_resnet50_imagenet_classification)中获取完整样例代码。
<!-- end id7 -->
调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行时资源申请。
# 3.创建图片数据处理通道时的通道描述信息，dvpp_channel_desc 是acldvppChannelDesc类型。
self.dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 4.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(self.dvpp_channel_desc)

# 5.创建输出图片的描述信息，并设置各属性值。
self.output_desc = acl.media.dvpp_create_pic_desc()
assert self.output_desc is not None
out_buffer_size = self.set_picture_desc(self.output_desc, w // 2, h // 2, "output", 0)

# 6.创建输入图片的描述信息，并设置各属性值。
self.input_desc = acl.media.dvpp_create_pic_desc()
assert self.input_desc is not None
self.set_picture_desc(self.input_desc, w, h, "input", 0)

# 7.加载图片数据，并拷贝到Device侧。
np_yuv = np.fromfile(path, dtype=np.byte)
in_buffer_size = np_yuv.itemsize * np_yuv.size
bytes_data = np_yuv.tobytes()
np_yuv_ptr = acl.util.bytes_to_ptr(bytes_data)
ret = acl.rt.memcpy(self.dev_buffer["input_0"], in_buffer_size, np_yuv_ptr,
                      in_buffer_size, ACL_MEMCPY_HOST_TO_DEVICE)
assert ret == 0

# 8.指定抠图、贴图区域的位置。
self.crop_area = acl.media.dvpp_create_roi_config(w // 2, w - 1, h // 2, h - 1)
self.paste_area = acl.media.dvpp_create_roi_config(w // 4, w // 2 - 1, h // 4, h // 2 - 1)

# 9.执行异步抠图贴图缩放。
self.resize_config = acl.media.dvpp_create_resize_config()
ret = acl.media.dvpp_vpc_crop_resize_paste_async(self.dvpp_channel_desc,
                                                       self.input_desc, self.output_desc,
                                                       self.crop_area, self.paste_area,
                                                       self.resize_config, self.stream)
assert ret == 0
ret = acl.rt.synchronize_stream(self.stream)
assert ret == 0

# 10.将输出数据拷贝到Host侧。
np_output = np.zeros(out_buffer_size, dtype=np.byte)
bytes_data = np_output.tobytes()
np_output_ptr = acl.util.bytes_to_ptr(bytes_data)
ret = acl.rt.memcpy(np_output_ptr, out_buffer_size, self.dev_buffer["output_0"],
                      out_buffer_size, ACL_MEMCPY_DEVICE_TO_HOST)
assert ret == 0

# 11.释放资源，包括输入/输出图片的描述信息、输入/输出内存、通道描述信息、通道等。
ret = acl.media.dvpp_destroy_pic_desc(self.input_desc)
ret = acl.media.dvpp_destroy_pic_desc(self.output_desc)
# dev_buffer是字典对象，存储device侧申请内存。
for key in self.dev_buffer.keys():
    if self.dev_buffer[key]:
        ret = acl.media.dvpp_free(self.dev_buffer[key])
if self.dvpp_channel_desc:
    ret = acl.media.dvpp_destroy_channel(self.dvpp_channel_desc)
    assert ret == 0
    ret = acl.media.dvpp_destroy_channel_desc(self.dvpp_channel_desc)
    assert ret == 0

# 12.释放运行时资源。
# 13.去初始化。
ret = acl.finalize()
# ......
```
<!-- end id6 -->
<!-- npu="910b,910,310p,310b" id8 -->
## 抠图贴图（一图多框）示例代码

- 调用`dvpp_vpc_batch_crop_and_paste_async`异步接口，按指定区域从输入图片中抠图，再将抠的图片贴到目标图片的指定位置，作为输出图片。对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。
- 抠图区域“crop_area”的宽高与贴图区域“paste_area”宽高不一致时会对图片再做一次缩放操作。
- 如果用户需要将目标图片读入内存用于存放输出图片，将贴图区域叠加在目标图片上，则需要编写代码逻辑：在申请输出内存后，将目标图片读入输出内存。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ret = acl.init()

# 2.运行时资源申请。
# 3.创建图片批处理输入输出描述。
self.out_batch_pic_desc = acl.media.dvpp_create_batch_pic_desc(self.out_batch_size)
self.in_batch_pic_desc = acl.media.dvpp_create_batch_pic_desc(self.in_batch_size)
# 3.1 指定批量抠图区域的位置、指定批量贴图区域的位置。
# 3.2 设置输入输出图片描述:如果抠图贴图的输出图片作为模型推理的输入，则输出图片的宽高要与模型要求的宽高保持一致。
for i in range(self.in_batch_size):
    input_desc = acl.media.dvpp_get_pic_desc(self.in_batch_pic_desc, i)
    assert input_desc is not None
    # 申请内存并设置输出图片描述。
    self.set_picture_desc(input_desc, w, h, "input", i)
    # copy from host to device.
    key = "input" + '_' + str(i)
    ret = acl.rt.memcpy(self.dev_buffer[key], in_buffer_size, np_yuv_ptr,
                         in_buffer_size, 1)
    assert ret == 0
    # 创建roiNums,每张图对应需要抠图和贴图的数量。
    roiList.append(self.out_batch_size // self.in_batch_size)
for i in range(self.out_batch_size):
    output_desc = acl.media.dvpp_get_pic_desc(self.out_batch_pic_desc, i)
    assert output_desc is not None
    # 自定义方法申请内存并设置输出图片描述。
    self.set_picture_desc(output_desc, w, h, "output", i)
    if i == 0:
        crop_area = acl.media.dvpp_create_roi_config(w // 2, w - 1, h // 2, h - 1)
    else:
        crop_area = acl.media.dvpp_create_roi_config(0, w - 1, h // 2, h - 1)
    paste_area = acl.media.dvpp_create_roi_config(w // 2, w - 1, h // 2, h - 1)
    self.cropList.append(crop_area)
    self.pasteList.append(paste_area)
# 3.3 roiList,每张图对应需要抠图和贴图的数量。输出图片数相对输入多出来的，加到最后一张输入图片的输出。
total_num = 0
for i in range(self.in_batch_size):
    total_num += roiList[i]
if self.out_batch_size % self.in_batch_size != 0:
    roiList[-1] = self.out_batch_size - total_num + roiList[-1]

# 4.创建图片数据处理通道时的通道描述信息，dvppChannelDesc_是acldvppChannelDesc类型。
self.dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 5.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(self.dvpp_channel_desc)

# 6.执行异步缩放，再调用acl.rt.synchronize_stream接口阻塞程序运行，直到指定Stream中的所有任务都完成。
_, ret = acl.media.dvpp_vpc_batch_crop_and_paste_async(self.dvpp_channel_desc, self.in_batch_pic_desc,
                                                             roiList, self.out_batch_pic_desc, self.cropList,
                                                             self.pasteList, self.stream)
ret = acl.rt.synchronize_stream(self.stream)

# 7.释放资源，包括输入/输出图片的描述信息、输入/输出内存、通道描述信息、通道等。
# 7.1 释放图片描述和批量图片描述。
self._free_pic_desc()
for i in range(len(self.cropList)):
    ret = acl.media.dvpp_destroy_roi_config(self.cropList[i])
    assert ret == 0
for i in range(len(self.pasteList)):
    ret = acl.media.dvpp_destroy_roi_config(self.pasteList[i])
    assert ret == 0
for key in self.dev_buffer.keys():
    if self.dev_buffer[key]:
        ret = acl.media.dvpp_free(self.dev_buffer[key])
# 7.2 销毁通道和通道描述。
if self.dvpp_channel_desc:
    ret = acl.media.dvpp_destroy_channel(self.dvpp_channel_desc)
    assert ret == 0
    ret = acl.media.dvpp_destroy_channel_desc(self.dvpp_channel_desc)
    assert ret == 0

# 8.释放运行时资源。
# 9.去初始化。
ret = acl.finalize()
```
<!-- end id8 -->