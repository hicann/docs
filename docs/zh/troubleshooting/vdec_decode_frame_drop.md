# VDEC视频解码丢帧/丢包

## 问题现象描述

视频解码丢帧，出现重影或不连续现象。查看Device日志，发现日志中存在以下几个报错的内容信息中的一个或多个，不同版本日志信息可能有所不同。

- H264码流缺少IDR帧日志报错信息（1）

    ```bash
    [HiDvpp][A618] [Vfmw]:ppssps_check [Line]:6803 pps with this pic_parameter_set_id = %d haven't decode
    [HiDvpp][A618] [Vfmw]:process_slice_header_first_part [Line]:7401 PPS or SPS of this slice not valid
    [HiDvpp][A618] [Vfmw]:h264_dec_slice [Line]:7915 sliceheader dec err
    ```

    或

    ```bash
    [ERROR] DVPP:2020-12-31-23:51:51.339.518 [VDEC][PPSSPSCheckTmpId:7065][T3]  PPSSPSCheckTmpId: pps with this pic_parameter_set_id = 0 haven't decode
    [ERROR] DVPP:2020-12-31-23:51:51.339.616 [VDEC][ProcessSliceHeaderFirstPart:7627][T3]  PPS or SPS of this slice not valid
    [ERROR] DVPP:2020-12-31-23:51:51.339.678 [VDEC][InquiresSlceProperty:10582][T3]  sliceheader dec err
    ```

- H264码流缺少I帧日志报错信息（2）

    ```bash
    [HiDvpp][A618] [Vfmw]:h264_dec_slice [Line]:7983 init pic err, find next recover point or next valid sps, pps, or exit
    [HiDvpp][A618] [Vfmw]:h264_dec_slice [Line]:3716 dec list error, ret=-1
    [HiDvpp][A618] [Vfmw]:receive_packet [Line]:10676 nal_release_err
    ```

    或

    ```bash
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InitPic:6039][T3]  line 6039: frame gap(=48) > dpb size(=2)
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecSlice:8238][T3]  init pic err, find next recover point or next valid sps, pps, or exit
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecOneNal:10077][T3]  DecList error, ret=-1
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][ReceivePacket:10400][T3]  nal_release-err
    ```

- H264码流缺少P帧日志报错信息（3）

    ```bash
    [HiDvpp][A618] [Vfmw]:init_list_x [Line]:4829 for P slice size of list equal 0.ctx->dpb.ref_frames_in_buffer:0.
    [HiDvpp][A618] [Vfmw]:dec_list [Line]:5068 init list error.
    [HiDvpp][A618] [Vfmw]:h264_dec_list [Line]:4829 dec_list error, ret=-1
    [HiDvpp][A618] [Vfmw]:h264_dec_one_nal [Line]:10298 slice_check failed, clear current slice.
    ```

    或

    ```bash
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InitListX:4513][T3]  for P slice size of list equal 0.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][DecList:4832][T3] line: 4832 InitListX failed
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecSlice:8260][T3] DecList error, ret=-1
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecOneNal:10077][T3] Decoder Slice failed
    ```

- H264码流缺少B帧日志报错信息（4）

    ```bash
    [HiDvpp][A618] [Vfmw]:init_list_x [Line]:4865 for B slice size of two list all equal 0.
    [HiDvpp][A618] [Vfmw]:dec_list [Line]:5068 init list error.
    [HiDvpp][A618] [Vfmw]:h264_dec_list [Line]:4829 dec_list error, ret=-1
    ```

    或

    ```bash
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InitListX:4653][T3] for B slice size of two list all equal 0.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][DecList:4830][T3] line: 4832 InitListX failed
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecSlice:8257][T3] DecList error, ret=-1
    ```

- H265码流缺少IDR帧日志报错信息（5）

    ```bash
    [HiDvpp][A618] [Vfmw]:hevc_vps_sps_pps_check [Line]:7300 pps with this pic_parameter_set_id = 0 haven't be decoded
    [HiDvpp][A618] [Vfmw]:hevc_dec_slice_segment_header [Line]:3857 hevc_vps_sps_pps_check != HEVC_DEC_NORMAL
    [HiDvpp][A618] [Vfmw]:hevc_inquire_slice_property [Line]:9004 hevc_dec_slice_segment_header dec err
    [HiDvpp][A618] [Vfmw]:hevc_dec_decode_packet[Line]:9004 hevc_inquire_slice_property error.
    ```

    或

    ```bash
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_VpsSpsPpsCheck:8084][T10] pps with this pic_parameter_set_id = 0 haven't be decoded
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_DecSliceSegmentHeader:2793][T10] HEVC_VpsSpsPpsCheck != HEVC_DEC_NORMAL
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_InquireSliceProperty:10169][T10] HEVC_DecSliceSegmentHeader dec err
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVCDEC_DecodePacket:753][T10] HEVC_InquireSliceProperty error.
    ```

- H265码流缺少I帧或者P帧日志报错现象（6）

    ```bash
    [HiDvpp][A618] [Vfmw]:hevc_ref_pic_process [Line]:3474 ref frame(poc 15) lost.
    [HiDvpp][A618] [Vfmw]:hevc_create_lost_picture [Line]:5839 DPB no suited fs for lost pic.
    [HiDvpp][A618] [Vfmw]:hevc_create_lost_picture [Line]:5847 take poc(17) to create lost poc(15).
    ```

    或

    ```bash
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480][T10] Ref frame(poc 15) lost.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_CreateLostPicture:6392][T10] DPB no suited fs for lost pic.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480][T10] Ref frame(poc 18) lost.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_CreateLostPicture:6392] [T10] DPB no suited fs for lost pic.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480] [T10] Ref frame(poc 18) lost.
    ```

- H265码流缺少I帧或者B帧日志报错信息（7）

    ```bash
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480] [T56] Ref frame(poc 15) lost.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_CreateLostPicture:6392] [T56] Take poc(17) to create lost poc(15).
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][FSP_SetRef:934] [T56] check condition: pstLogicFs->IsDummyFs == 0 fail
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][FSP_SetRef:934] [T56] check condition: pstLogicFs->IsDummyFs == 0 fail
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][FSP_SetRef:934] [T56] check condition: pstLogicFs->IsDummyFs == 0 fail
    ```

## 可能原因

分析上述日志报错信息现象，分别可能存在以下可能原因：

- 日志报错信息（1）可能原因：H264码流缺少IDR帧
- 日志报错信息（2）可能原因：H264码流缺少I帧
- 日志报错信息（3）可能原因：H264码流缺少P帧
- 日志报错信息（4）可能原因：H264码流缺少B帧
- 日志报错信息（5）可能原因：H265码流缺少IDR帧
- 日志报错信息（6）可能原因：H265码流缺少I帧或者P帧
- 日志报错信息（7）可能原因：H265码流缺少I帧或者B帧

## 处理步骤

针对可能原因分析，参考以下步骤处理：

1. 检查输入的源码流是否有问题。

    使用第三方工具（如：eseye u）对输入码流进行检查，查看码流是否异常。

2. 若查看的源码流结果为正常，则可能码流在传输给设备侧VDEC的过程中遭到破坏，需要在调用发送码流接口之前，通过fwrite函数将输送给VDEC的码流保存下来。
    - 使用第三方工具对保存的码流进行检查，如果码流异常，用户需自行排查将码流送进去之前是否有送流问题。

    - 通过对应版本的sample，解码这段保留下来的码流，验证码流是否正常或VDEC是否支持该格式。

        如果sample解码正常，那就是开发代码有问题，可以参考VDEC示例代码，找到对应的视频解码的代码参考优化。
