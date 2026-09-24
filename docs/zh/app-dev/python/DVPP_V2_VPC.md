<!-- npu="910b,910,310p,310b" id1 -->
# VPC图片处理典型功能

VPC（Vision Preprocessing Core）负责图像处理功能，支持对图片做抠图、缩放、格式转换等操作。关于VPC功能的详细介绍及其约束请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)。

本节以抠图、缩放为例说明VPC图像处理时的接口调用流程，同时配合以下典型功能的示例代码辅助理解该接口调用流程：

- [图片缩放示例代码](#图片缩放示例代码)
- [抠图示例代码](#抠图示例代码)

## 典型功能接口调用流程（以缩放为例）

开发应用时，如果涉及抠图、缩放等图片处理，则应用程序中必须包含图片处理的代码逻辑，关于图片处理的接口调用流程，请先参见[接口调用流程](interface_calling_process.md)了解整体流程，再查看本节中的流程说明。
<!-- npu="910b,910,310p,310b" id2 -->
如果在Host上调用DVPP接口，图像处理的结果数据都在Device的内存中，如果想访问结果数据，需要将结果数据传输回Host侧。
<!-- end id2 -->
**图 1**  接口调用流程（以缩放为例）
![](figures/VPC_API_call_process_V2.png "接口调用流程（以缩放为例）")

当前系统支持对输入图片做抠图、缩放等处理，关键接口的说明如下：

1. 调用`acl.himpi.sys_init`接口进行媒体数据处理系统初始化。
2. 调用`acl.himpi.vpc_create_chn`接口创建通道。
3. 调用`acl.himpi.dvpp_malloc`接口申请Device上的内存，存放输入或输出数据。
    <!-- npu="310b" id3 -->
    Atlas 200I/500 A2推理产品上，同时支持使用`acl.rt.malloc`接口申请内存。
    <!-- end id3 -->
    <!-- npu="910b" id4 -->
    Atlas A2系列产品上，同时支持使用`acl.rt.malloc`接口申请内存。
    <!-- end id4 -->
    <!-- npu="910b,310b" id5 -->
    对于Atlas 200I/500 A2推理产品与Atlas A2系列产品，调用`acl.himpi.dvpp_malloc`接口申请的内存为媒体数据处理的专用内存，但专用内存的地址空间有限，若关注内存规划或内存资源有限时，建议调用`acl.rt.malloc`接口申请内存。
    <!-- end id5 -->
4. 执行抠图、缩放等，此步骤以缩放为例说明，其它功能（例如格式转换、金字塔等）请参见[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)中VPC功能下的接口说明。

    调用`acl.himpi.vpc_resize`接口，对图片进行缩放。`acl.himpi.vpc_resize`接口是异步接口，调用该接口成功仅表示任务下发成功，还需要调用`acl.himpi.vpc_get_process_result`接口等待任务完成。

    - 可以跟`acl.himpi.vpc_resize`接口在同一个线程中调用`acl.himpi.vpc_get_process_result`接口，也可以新起一个线程调用`acl.himpi.vpc_get_process_result`接口，后者多线程并行，提高效率，但用户需自行实现线程间同步。
    - 在实现抠图、缩放等功能时，通过将输入图片和输出图片的格式设置成不同的，达到转换图片格式的目的。
    <!-- npu="310p" id6 -->
    - 对于Atlas推理系列产品，调用`acl.rt.get_run_mode`接口获取软件栈的运行模式，如果运行模式为ACL_HOST，且Host上需要展示VPC输出的图片数据，则需要申请Host内存，通过`acl.rt.memcpy`接口将Device的输出图片数据传输到Host；如果Host上不需要展示VPC输出的图片数据，则VPC的输出图片数据可以直接作为模型推理的输入，模型推理的相关介绍请参见[模型管理](model_management.md)、[模型动态AIPP推理](dynamic_AIPP_inference.md)。
    <!-- end id6 -->
5. 调用`acl.himpi.dvpp_free`接口释放输入、输出内存。
    <!-- npu="310b" id7 -->
    Atlas 200I/500 A2推理产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id7 -->
    <!-- npu="910b" id8 -->
    Atlas A2系列产品上，若使用`acl.rt.malloc`接口申请内存，则需使用`acl.rt.free`接口释放内存。
    <!-- end id8 -->
6. 调用`acl.himpi.vpc_destroy_chn`接口销毁通道。
7. 调用`acl.himpi.sys_exit`接口进行媒体数据处理系统去初始化。

## 图片缩放示例代码

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
channel_id = 0
chn_attr = {'attr': 0, 'pic_width': 0, 'pic_height': 0}
ret = acl.himpi.vpc_create_chn(channel_id, chn_attr)

# 6.执行缩放。
# 6.1 构造存放输入图片信息的字典。
input_pic = {'picture_width': 1920,
             'picture_height': 1080,
             'picture_width_stride': 1920,
             'picture_height_stride': 1080,
             'picture_format': HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420}
input_pic["picture_buffer_size"] = input_pic["picture_width_stride"] * input_pic["picture_height_stride"] * 3 // 2
picture_address, ret = acl.himpi.dvpp_malloc(0, input_pic["picture_buffer_size"])
input_pic["picture_address"] = picture_address

# 6.2 如果运行模式为ACL_HOST，则需要申请Host内存，将输入图片数据读入Host内存，再通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时释放Host内存；否则直接将输入图片数据读入Device内存。
# 直接将输入图片数据读入Device内存。
if run_mode == ACL_HOST:
    # 将输入图片读入内存中。
    vpc_file = np.fromfile(vpc_file_path, dtype=np.byte)
    vpc_file_size = vpc_file.itemsize * vpc_file.size

    bytes_data = vpc_file.tobytes()
    vpc_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_pic["picture_address"], input_pic["picture_buffer_size"],
                        vpc_file_ptr, vpc_file_size, ACL_MEMCPY_HOST_TO_DEVICE)
else:
    # 将输入图片读入内存中。
    vpc_file = np.fromfile(vpc_file_path, dtype=np.byte)
    vpc_file_size = vpc_file.itemsize * vpc_file.size

    bytes_data = vpc_file.tobytes()
    vpc_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_pic["picture_address"], input_pic["picture_buffer_size"],
                        vpc_file_ptr, vpc_file_size, ACL_MEMCPY_DEVICE_TO_DEVICE)


# 6.3 构造存放输出图片信息的字典。
output_pic = {'picture_width': 960,
                'picture_height': 540,
                'picture_width_stride': 960,
                'picture_height_stride': 540,
                'picture_format': HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420}
output_pic["picture_buffer_size"] = output_pic["picture_width_stride"] * output_pic["picture_height_stride"] * 3 // 2
picture_address, ret = acl.himpi.dvpp_malloc(0, output_pic["picture_buffer_size"])
output_pic["picture_address"] = picture_address
# 初始化内存。
ret = acl.rt.memset(output_pic["picture_address"], output_pic["picture_buffer_size"], 0, output_pic["picture_buffer_size"])

# 6.4 调用缩放接口。
task_id, ret = acl.himpi.vpc_resize(channel_id, input_pic, output_pic, 0, 0, 0, -1)

# 6.5 等待任务处理结束，任务处理结束后，输出图片数据在outputPic.picture_address指向的内存中。
ret = acl.himpi.vpc_get_process_result(channel_id, task_id, -1)

# 6.6 如果运行模式为ACL_HOST，且Host上需要展示VPC输出的图片数据，则需要申请Host内存，通过acl.rt.memcpy接口将Device的输出图片数据传输到Host；如果Host上不需要展示VPC输出的图片数据，则VPC的输出图片数据可以直接作为模型推理的输入。
# VPC的输出图片数据可以直接作为模型推理的输入。
if run_mode == ACL_HOST:
        np_output = np.zeros(output_pic.get('picture_buffer_size'), dtype=np.byte)

        bytes_data = np_output.tobytes()
        np_output_ptr = acl.util.bytes_to_ptr(bytes_data)
        ret = acl.rt.memcpy(np_output_ptr, output_pic.get('picture_buffer_size'), output_pic.get("picture_address"),
                            output_pic.get('picture_buffer_size'), ACL_MEMCPY_DEVICE_TO_HOST)
        # ......
else
    # 可以直接使用VPC的输出图片数据，在outputPic.picture_address指向的内存中。
    # ......

# 6.7 释放输入、输出内存。
ret = acl.himpi.dvpp_free(input_pic['picture_address'])
ret = acl.himpi.dvpp_free(output_pic['picture_address'])

# 7.销毁通道。
ret = acl.himpi.vpc_destroy_chn(channel_id)

# 8. 媒体数据处理系统去初始化。
ret = acl.himpi.sys_exit()

# 9. 释放运行时资源。
# 10.去初始化。
ret = acl.finalize()
```

## 抠图示例代码

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
channel_id = 0
chn_attr = {'attr': 0, 'pic_width': 0, 'pic_height': 0}
ret = acl.himpi.vpc_create_chn(channel_id, chn_attr)

# 6.执行抠图。
# 6.1 构造存放输入图片信息的字典。
input_pic = {'picture_width': 1920,
             'picture_height': 1080,
             'picture_width_stride': 1920,
             'picture_height_stride': 1080,
             'picture_format': HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420}
input_pic["picture_buffer_size"] = input_pic["picture_width_stride"] * input_pic["picture_height_stride"] * 3 // 2
picture_address, ret = acl.himpi.dvpp_malloc(0, input_pic["picture_buffer_size"])
input_pic["picture_address"] = picture_address

# 6.2 如果运行模式为ACL_HOST，则需要申请Host内存，将输入图片数据读入Host内存，再通过acl.rt.memcpy接口将Host的图片数据传输到Device，数据传输完成后，需及时释放Host内存；否则直接将输入图片数据读入Device内存。
# 直接将输入图片数据读入Device内存。
if run_mode == ACL_HOST:
    # 将输入图片读入内存中。
    vpc_file = np.fromfile(vpc_file_path, dtype=np.byte)
    vpc_file_size = vpc_file.itemsize * vpc_file.size

    bytes_data = vpc_file.tobytes()
    vpc_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_pic["picture_address"], input_pic["picture_buffer_size"],
                        vpc_file_ptr, vpc_file_size, ACL_MEMCPY_HOST_TO_DEVICE)
else:
    # 将输入图片读入内存中。
    vpc_file = np.fromfile(vpc_file_path, dtype=np.byte)
    vpc_file_size = vpc_file.itemsize * vpc_file.size

    bytes_data = vpc_file.tobytes()
    vpc_file_ptr = acl.util.bytes_to_ptr(bytes_data)
    # 数据传输。
    ret = acl.rt.memcpy(input_addr, input_size, vpc_file_ptr, vpc_file_size, ACL_MEMCPY_DEVICE_TO_DEVICE)

# 6.3 构造存放输出图片信息的字典。
multithreading_count = 1
crop_region_infos = []
for i in range(multithreading_count):
    output_pic = {'picture_width': 960,
                  'picture_height': 540,
                  'picture_width_stride': 960,
                  'picture_height_stride': 540,
                  'picture_format': HI_PIXEL_FORMAT_YUV_SEMIPLANAR_420}
    output_pic["picture_buffer_size"] = output_pic["picture_width_stride"] * output_pic["picture_height_stride"] * 3 // 2
    picture_address, ret = acl.himpi.dvpp_malloc(0, output_pic["picture_buffer_size"])
    output_pic["picture_address"] = picture_address

    ret = acl.rt.memset(output_pic["picture_address"], output_pic["picture_buffer_size"], 0, output_pic["picture_buffer_size"])
    crop_region = {'top_offset': 0, 'left_offset': 0, 'crop_width': 960, 'crop_height': 540}
    crop_region_info = {'dest_pic_info': output_pic, 'crop_region': crop_region}
    crop_region_infos.append(crop_region_info)

# 6.4 调用抠图接口。
task_id, ret = acl.himpi.vpc_crop(channel_id, input_pic, crop_region_infos, 1, -1)

# 6.5 等待任务处理结束，任务处理结束后，输出图片数据在outputPic.picture_address指向的内存中。
ret = acl.himpi.vpc_get_process_result(channel_id, task_id, -1)

# 6.6 如果运行模式为ACL_HOST，且Host上需要展示VPC输出的图片数据，则需要申请Host内存，通过acl.rt.memcpy接口将Device的输出图片数据传输到Host；如果Host上不需要展示VPC输出的图片数据，则VPC的输出图片数据可以直接作为模型推理的输入。
# VPC的输出图片数据可以直接作为模型推理的输入。
if run_mode == ACL_HOST:
    np_output = np.zeros(output_pic.get('picture_buffer_size'), dtype=np.byte)

    bytes_data = np_output.tobytes()
    np_output_ptr = acl.util.bytes_to_ptr(bytes_data)
    ret = acl.rt.memcpy(np_output_ptr, output_pic.get('picture_buffer_size'), output_pic.get("picture_address"),
                        output_pic.get('picture_buffer_size'), ACL_MEMCPY_DEVICE_TO_HOST)
    # ......
else
    # 可以直接使用VPC的输出图片数据，在outputPic.picture_address指向的内存中。
    # ......

# 6.7 释放输入、输出内存。
ret = acl.himpi.dvpp_free(input_pic['picture_address'])
ret = acl.himpi.dvpp_free(output_pic['picture_address'])

# 7.销毁通道。
ret = acl.himpi.vpc_destroy_chn(channel_id)

# 8. 媒体数据处理系统去初始化。
ret = acl.himpi.sys_exit()

# 9. 释放运行时资源。
# 10.去初始化。
ret = acl.finalize()
```
<!-- end id1 -->
