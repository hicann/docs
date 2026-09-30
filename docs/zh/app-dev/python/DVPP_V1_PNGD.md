# PNGD图片解码

本节介绍PNGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

PNGD（PNG decoder）负责PNG格式图片的解码。关于PNGD功能的详细介绍及约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

开发应用时，如果涉及对PNG图片的解码，则应用程序中必须包含图片解码的代码逻辑，**关于图片解码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明**。

**图 1**  PNG图片解码
![](figures/PNGD_API_call_process_V1.png "PNG图片解码")

当前系统支持PNG图片的解码，支持输出RGB、RGBA编码格式的图片，关键接口的说明如下：

1. 调用`acl.media.dvpp_create_channel_desc`接口**创建通道描述信息**。
2. 调用`acl.media.dvpp_create_channel`接口**创建图片数据处理的通道**。
3. 实现PNG图片解码功能前，**若需要申请Device上的内存**存放输入或输出数据，需调用`acl.media.dvpp_malloc`申请内存。

    在申请输出内存前，可调用`acl.media.dvpp_png_predict_dec_size`接口根据存放PNG图片数据的内存**预估**出PNG图片解码后所需的输出内存的大小。

4. 调用`acl.media.dvpp_png_decode_async`异步接口进行**解码**。

    对于异步接口，还需调用`acl.rt.synchronize_stream`接口阻塞程序运行，直到指定Stream中的所有任务都完成。

5. 在解码结束后，需及时调用`acl.media.dvpp_free`接口**释放输入、输出内存**。
6. 调用`acl.media.dvpp_destroy_channel`接口**销毁图片数据处理的通道**。

    销毁图片数据处理的通道后，再调用`acl.media.dvpp_destroy_channel_desc`接口**销毁通道描述信息**。

## 示例代码

调用接口后，需增加异常处理的分支，同时通过“ERROR_LOG”记录报错日志、通过“INFO_LOG”记录各动作的提示日志，示例代码中不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
import acl
# ......

# 1.初始化。
ACL_CONFIG_PATH = "../src/acl.json"
ret = acl.init(ACL_CONFIG_PATH)

# 2.运行管理资源申请。
# 3.创建图片数据处理通道时的通道描述信息，dvpp_channel_desc是acldvppChannelDesc类型对象。
dvpp_channel_desc = acl.media.dvpp_create_channel_desc()

# 4.创建图片数据处理的通道。
ret = acl.media.dvpp_create_channel(dvpp_channel_desc)

# 5.申请输入内存。
pic_name = "../data/test_png_dec.png"
np_png = np.fromfile(pic_name, dtype=np.byte)
in_buffer_size = np_png.itemsize * np_png.size
bytes_data = np_png.tobytes()
np_png_ptr = acl.util.bytes_to_ptr(bytes_data)
in_dev_buffer, ret = acl.media.dvpp_malloc(in_buffer_size)
ACL_MEMCPY_HOST_TO_DEVICE = 1
ret = acl.rt.memcpy(in_dev_buffer, in_buffer_size, np_png_ptr, in_buffer_size,
    ACL_MEMCPY_HOST_TO_DEVICE)

# 6.申请解码输出内存。
PIXEL_FORMAT_RGB_888 = 12
out_buffer_size, ret = acl.media.dvpp_png_predict_dec_size(np_png_ptr, in_buffer_size,
    PIXEL_FORMAT_RGB_888)
out_dev_buffer, ret = acl.media.dvpp_malloc(out_buffer_size)

# 7.创建解码输出图片的描述信息，设置各属性值。
output_desc = acl.media.dvpp_create_pic_desc()
width, height, components, ret = acl.media.dvpp_png_get_image_info(np_png_ptr, in_buffer_size)
ret = acl.media.dvpp_set_pic_desc_data(output_desc, out_dev_buffer)
ret = acl.media.dvpp_set_pic_desc_size(output_desc, out_buffer_size)
ret = acl.media.dvpp_set_pic_desc_format(output_desc, PIXEL_FORMAT_RGB_888)

# 8.执行异步解码，再调用acl.rt.synchronize_stream接口阻塞程序运行，直到指定Stream中的所有任务都完成。
ret = acl.media.dvpp_png_decode_async(dvpp_channel_desc, in_dev_buffer, in_buffer_size,
    output_desc, stream)
ret = acl.rt.synchronize_stream(stream)

# 9.解码结束后，释放资源，包括解码输出图片的描述信息、解码输出内存、通道描述信息、通道等。
ret = acl.media.dvpp_destroy_pic_desc(output_desc)
ret = acl.media.dvpp_free(in_dev_buffer)
ret = acl.media.dvpp_free(out_dev_buffer)
ret = acl.media.dvpp_destroy_channel(dvpp_channel_desc)
ret = acl.media.dvpp_destroy_channel_desc(dvpp_channel_desc)

# 10.释放运行管理资源。
# 去初始化。
ret = acl.finalize()
# ....
```
