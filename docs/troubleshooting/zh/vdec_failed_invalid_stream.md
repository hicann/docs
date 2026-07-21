# 输入码流不符合要求导致VDEC视频解码失败

## 问题现象描述

视频解码失败，日志中打印如下所示的异常信息，不同版本日志信息可能有所不同：

- 日志信息：Invalid width or height

    ```bash
    [HiDvpp][A618] [Vfmw] vdec_drv_check_video_wh [Line]:127 device 0 chn 0 type(255) pic size(32x32) is out of range[128,128]x[4096,4096].
    ```

    或

    ```bash
    [ERROR] DVPP:2020-12-31-20:50:51.318.218 [VDEC][IsValidResolution:639][T56] Invalid width or height, valid range (w:128~4096) (h:128~4096), current width = 32, height = 32, realWidth = 18, realHeight = 18
    [ERROR] DVPP:2020-12-31-20:50:51.318.365 [VDEC][upgrade_picture_info_in_detail:679][T56] check condition: ret == OMX_ErrorNone fail
    [ERROR] DVPP:2020-12-31-20:50:51.318.429 [VDEC][EventHandLer:386][T56] Dynamic Resources Unavailable now
    [ERROR] DVPP:2020-12-31-20:50:51.368.106 [VDEC][handle_release_instance:1352][T56] wait Component Exit Message Thread
    ```

- 日志信息：bit\_depth\_luma\(\*\) not equal \*

    ```bash
    [HiDvpp][A618] [Vfmw] process_sps [Line]:8994 bit_depth_luma(%d) not equal 8.
    [HiDvpp][A618] [Vfmw] hevc_process_sps [Line]:1462 chn 0, bit_depth_luma(9) is not supported, hevc only support 8 or 10 bit depth.
    ```

    或

    ```bash
    [ERROR] DVPP(13757,dvpp_performance):2020-12-31-21:18:26.998.657 [VDEC][ProcessSPS:9055][T26] bit_depth_luma(10) not equal 8.
    [ERROR] DVPP(13757,dvpp_performance):2020-12-31-21:18:26.998.763 [VDEC][ProcessSPS:9070][T26] bit_depth_chroma(10) not equal 8.
    ```

## 可能原因

针对上述日志分析，可能存在输入码流规格不符合软硬件约束。

## 处理步骤

根据[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)中的内容检查VDEC功能约束，使用第三方工具（如：eseye u等）对输入码流进行检查，查看码流类型、码流宽高等信息是否符合要求。如果码流不满足要求，请替换符合要求的码流。
