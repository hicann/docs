# VDEC Failure Due to Incorrect Input Streams

## Symptom

If video decoding fails, the following exception information is recorded in the log. The log information varies according to the version.

- Log message: Invalid width or height

    ```text
    [HiDvpp][A618] [Vfmw] vdec_drv_check_video_wh [Line]:127 device 0 chn 0 type(255) pic size(32x32) is out of range[128,128]x[4096,4096].
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][IsValidResolution:639][T56] Invalid width or height, valid range (w:128~4096) (h:128~4096), current width = 32, height = 32, realWidth = 18, realHeight = 18
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][upgrade_picture_info_in_detail:679][T56] check condition: ret == OMX_ErrorNone fail
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][EventHandLer:386][T56] Dynamic Resources Unavailable now
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][handle_release_instance:1352][T56] wait Component Exit Message Thread
    ```

- Log message: bit\_depth\_luma\(\*\) not equal \*

    ```text
    [HiDvpp][A618] [Vfmw] process_sps [Line]:8994 bit_depth_luma(%d) not equal 8.
    [HiDvpp][A618] [Vfmw] hevc_process_sps [Line]:1462 chn 0, bit_depth_luma(9) is not supported, hevc only support 8 or 10 bit depth.
    ```

    Or

    ```text
    [ERROR] DVPP(13757,dvpp_performance):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][ProcessSPS:9055][T26] bit_depth_luma(10) not equal 8.
    [ERROR] DVPP(13757,dvpp_performance):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][ProcessSPS:9070][T26] bit_depth_chroma(10) not equal 8.
    ```

## Possible Cause

According to the preceding log analysis, the input stream specifications may not meet the software and hardware restrictions.

## Solution

Check the VDEC functions and restrictions based on the content in  [DVPP Media Acceleration Library](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/acce/dvpp/dvp.html), use a third-party tool \(for example, eseye u\) to check whether the input stream type, width, and height meet the requirements. If no, replace the stream as required.
