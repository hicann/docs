# 异常码流导致VDEC视频解码失败

## 问题现象描述

调用hi\_mpi\_vdec\_get\_frame接口成功，返回的解码结果为失败\(frame\_info-\>v\_frame.frame\_flag = 1\)，表示可能由于输入码流异常、设置的码流格式与实际码流不一致等问题导致解码失败。

常见语法解析日志报错示例如下：

- 日志示例1

    ```bash
    pid 0 usr chn 0 device 0 chn 0, input stream error, can't decode, report to user
    ```

- 日志示例2

    ```bash
    ppssps_check_tmp_id: pps is null with this pic_parameter_set_id = 1 haven't decode
    ```

- 日志示例3

    ```bash
    PPS or SPS of this slice not valid
    ```

- 日志示例4

    ```bash
    sliceheader dec err
    ```

- 日志示例5

    ```bash
    H264DEC inquire_slice_property error
    ```

- 日志示例6

    ```bash
    hevc_inquire_slice_property error
    ```

- 日志示例7

    ```bash
    ref frame(poc 15) lost
    ```

- 日志示例8

    ```bash
    SH hevc_dec_short_term_ref_pic_set error
    ```

- 日志示例9

    ```bash
    p_temp_r_pset->num_negative_pics(66) out of range(0,15)
    ```

## 原因分析

frame\_flag = 1解码失败，一般是由于送给VDEC视频解码模板的输入码流存在异常，或者网络不稳定导致播包丢帧导致码流异常，所以解码会报错失败，针对这种情况，可以通过保存输入码流来进行判断输入码流是否异常。

## 解决方法（Ascend RC形态）

1. 在调用hi\_mpi\_vdec\_send\_stream接口成功之后，将输入码流进行写文件保存，可参考如下代码。

    ```c
        ret = hi_mpi_vdec_send_stream(chn, stream, vdec_pic_info, milli_sec);
        if (ret == HI_SUCCESS) {
            FILE *fd = NULL;
            fd = fopen("input_stream", "a+");
            fwrite(stream->addr, stream->len, 1, fd);
            fclose(fd); 
        }
    ```

2. 使用第三方工具查看保存下来的input\_stream码流，检查是否存在异常，例如花屏、报错提示等。

## 解决方法（Ascend EP形态）

1. 在调用hi\_mpi\_vdec\_send\_stream接口成功之后，将输入码流进行写文件保存，可参考如下代码。

    需要先将码流数据从Host传输至Device，再发送解码码流。

    ```c
         aclrtMemcpy(stream->addr, stream->len, buf, size, ACL_MEMCPY_HOST_TO_DEVICE);
        ret = hi_mpi_vdec_send_stream(chn, stream, vdec_pic_info, milli_sec);
        if (ret == HI_SUCCESS) {
            FILE *fd = NULL;
            fd = fopen("input_stream", "a+");
            fwrite(buf, size, 1, fd);
            fclose(fd); 
        }
    ```

2. 使用第三方工具查看保存下来的input\_stream码流，检查是否存在异常，例如花屏、报错提示等。
