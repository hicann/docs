<!-- npu="910b,910,310p,310b" id1 -->
# PNGD图片解码

本节介绍PNGD图片解码的接口调用流程，同时配合示例代码辅助理解该接口调用流程。

PNGD（PNG Decoder）负责PNG格式图片的解码。关于PNGD功能的详细介绍请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

## 接口调用流程

开发应用时，如果涉及对PNG图片的解码，则应用程序中必须包含解码的代码逻辑，关于图片解码的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。

**图 1**  接口调用流程
![](figures/PNGD_API_call_process_V2.png "接口调用流程-6")

当前系统支持解码PNG图片，关键接口的说明如下：

1. 调用`acl.himpi.sys_init`接口进行媒体数据处理系统初始化。
2. 调用`acl.himpi.pngd_create_chn`接口创建通道。
3. 调用`acl.himpi.dvpp_malloc`接口申请Device上的内存，存放输入或输出数据。
    <!-- npu="910b,310b" id2 -->
    对于Atlas 200I/500 A2推理产品与Atlas A2系列产品，调用`acl.himpi.dvpp_malloc`接口申请的内存为媒体数据处理的专用内存，但专用内存的地址空间有限，若关注内存规划或内存资源有限时，建议调用`acl.rt.malloc`接口申请内存。
    <!-- end id2 -->
4. 调用`acl.himpi.pngd_send_stream`接口发送解码码流，`acl.himpi.pngd_send_stream`接口是异步接口，调用该接口仅表示任务下发成功，还需要调用`acl.himpi.pngd_get_image_data`接口获取解码结果数据。
5. 调用`acl.himpi.dvpp_free`接口释放输入、输出内存。
    <!-- npu="310b" id3 -->
    Atlas 200I/500 A2推理产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id3 -->
    <!-- npu="910b" id4 -->
    Atlas A2系列产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id4 -->
6. 调用`acl.himpi.pngd_destroy_chn`接口销毁通道。
7. 调用`acl.himpi.sys_exit`接口进行媒体数据处理系统去初始化。

## 示例代码

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不可以直接拷贝运行，仅供参考。

```python
# 1.获取软件栈的运行模式，不同运行模式影响后续的接口调用流程（例如是否进行数据传输等）。
run_mode, ret = acl.rt.get_run_mode()

# 2.初始化。
ret = acl.init()

# 3.运行时资源申请。
# 4.初始化媒体数据处理系统。
ret = acl.himpi.sys_init()

# 5.创建通道。
attr = {"stream_que_cnt": STREAM_QUE_CNT}
channel_id = 0
ret = acl.himpi.pngd_create_chn(channel_id, attr)

# 6.发送码流。
# 6.1 申请输入内存。
input_addr, ret = acl.himpi.dvpp_malloc(0, input_size)

# 如果运行模式为ACL_HOST，则需要申请Host内存，将输入图片数据读入Host内存，再通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时释放Host内存；否则直接将输入图片数据读入Device内存。
# 直接将输入图片数据读入Device内存。
if run_mode == ACL_HOST:
    # 将输入图片读入内存中。
    jpege_file = np.fromfile(jpege_file_path, dtype=np.byte)
    jpege_file_size = jpege_file.itemsize * jpege_file.size

    bytes_data = jpege_file.tobytes()
    jpege_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, jpege_file_ptr, jpege_file_size, ACL_MEMCPY_HOST_TO_DEVICE)
else:
    # 将输入图片读入内存中。
    jpege_file = np.fromfile(jpege_file_path, dtype=np.byte)
    jpege_file_size = jpege_file.itemsize * jpege_file.size

    bytes_data = jpege_file.tobytes()
    jpege_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, jpege_file_ptr, jpege_file_size, ACL_MEMCPY_DEVICE_TO_DEVICE)

# 6.2 构造存放输入图片信息的字典。
stream = {"type": HI_PT_PNG, "addr": input_addr, "len": input_size, "pts": 0}
img_info, ret = acl.himpi.png_get_image_info(stream)

# 6.3 构造存放输出图片信息的字典，并申请输出内存。
output_addr, ret = acl.himpi.dvpp_malloc(0, img_info['img_buf_size'])
out_pic_info =  {"picture_address": output_addr,
                 "picture_buffer_size": img_info['img_buf_size'],
                 "picture_width": img_info['width'],
                 "picture_height": img_info['height'],
                 "picture_width_stride": img_info['width_stride'],
                 "picture_height_stride": img_info['height_stride'],
                 "picture_format": HI_PIXEL_FORMAT_UNKNOWN}
ret = acl.himpi.pngd_send_stream(channel_id, stream, out_pic_info, 0)

# 7.接收解码结果。
# 7.1 获取解码结果。
pic_info, get_stream, ret = acl.himpi.pngd_get_image_data(channel_id, -1)
if ret == 0: #  Decode success
    print("Chn %u GetFrame Success, Decode Success \n"%channel_id)
elif ret == HI_ERR_PNGD_BUF_EMPTY: # Decoding
    print("Chn %u Decoding, try again \n"%channel_id)
else: # Decode Fail
    print("Chn %u GetFrame Success, Decode Fail \n"%channel_id)

# 7.2 如果运行模式为ACL_HOST，且Host上需要展示PNGD输出的图片数据，则需要申请Host内存，通过acl.rt.memcpy接口将Device的输出图片数据传输到Host。
# 获取PNGD的输出图片数据。
if run_mode == ACL_HOST:
    # 申请Host内存。
    output_buffer, ret= acl.rt.malloc_host(output_size)
    # 数据传输。
    ret = acl.rt.memcpy(output_buffer, output_size, stream['pack'][0]['addr'], output_size, ACL_MEMCPY_DEVICE_TO_HOST)
    # ......
    # 数据使用完成后，及时释放不使用的内存。
    ret = acl.rt.free_host(output_buffer)
else:
    # 可以直接使用PNGD的输出图片数据，在outputPic.picture_address指向的内存中。
    # ......

# 7.3 释放输入内存和输出码流。
ret = acl.himpi.dvpp_free(input_addr)
ret = acl.himpi.dvpp_free(output_addr)

# 8.销毁通道。
ret = acl.himpi.pngd_destroy_chn(channel_id)

# 9.媒体数据处理系统去初始化。
ret = acl.himpi.sys_exit()

# 10.释放运行时资源。
# 11.去初始化。
ret = acl.finalize()
```
<!-- end id1 -->
