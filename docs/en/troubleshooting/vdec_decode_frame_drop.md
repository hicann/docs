# Frame Loss or Packet Loss During VDEC Video Decoding

## Symptom

Frame loss occurs during video decoding, causing ghosting or discontinuity. One or more of the following errors are found in the device logs, which may vary in different versions:

- Log message \(1\): The IDR frame is missing in the H.264 stream.

    ```text
    [HiDvpp][A618] [Vfmw]:ppssps_check [Line]:6803 pps with this pic_parameter_set_id = %d haven't decode
    [HiDvpp][A618] [Vfmw]:process_slice_header_first_part [Line]:7401 PPS or SPS of this slice not valid
    [HiDvpp][A618] [Vfmw]:h264_dec_slice [Line]:7915 sliceheader dec err
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][PPSSPSCheckTmpId:7065][T3]  PPSSPSCheckTmpId: pps with this pic_parameter_set_id = 0 haven't decode
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][ProcessSliceHeaderFirstPart:7627][T3]  PPS or SPS of this slice not valid
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InquiresSlceProperty:10582][T3]  sliceheader dec err
    ```

- Log message \(2\): The I-frame is missing in the H.264 stream.

    ```text
    [HiDvpp][A618] [Vfmw]:h264_dec_slice [Line]:7983 init pic err, find next recover point or next valid sps, pps, or exit
    [HiDvpp][A618] [Vfmw]:h264_dec_slice [Line]:3716 dec list error, ret=-1
    [HiDvpp][A618] [Vfmw]:receive_packet [Line]:10676 nal_release_err
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InitPic:6039][T3]  line 6039: frame gap(=48) > dpb size(=2)
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecSlice:8238][T3]  init pic err, find next recover point or next valid sps, pps, or exit
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecOneNal:10077][T3]  DecList error, ret=-1
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][ReceivePacket:10400][T3]  nal_release-err
    ```

- Log message \(3\): The P-frame is missing in the H.264 stream.

    ```text
    [HiDvpp][A618] [Vfmw]:init_list_x [Line]:4829 for P slice size of list equal 0.ctx->dpb.ref_frames_in_buffer:0.
    [HiDvpp][A618] [Vfmw]:dec_list [Line]:5068 init list error.
    [HiDvpp][A618] [Vfmw]:h264_dec_list [Line]:4829 dec_list error, ret=-1
    [HiDvpp][A618] [Vfmw]:h264_dec_one_nal [Line]:10298 slice_check failed, clear current slice.
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InitListX:4513][T3]  for P slice size of list equal 0.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][DecList:4832][T3] line: 4832 InitListX failed
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecSlice:8260][T3] DecList error, ret=-1
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecOneNal:10077][T3] Decoder Slice failed
    ```

- Log message \(4\): The B-frame is missing in the H.264 stream.

    ```text
    [HiDvpp][A618] [Vfmw]:init_list_x [Line]:4865 for B slice size of two list all equal 0.
    [HiDvpp][A618] [Vfmw]:dec_list [Line]:5068 init list error.
    [HiDvpp][A618] [Vfmw]:h264_dec_list [Line]:4829 dec_list error, ret=-1
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][InitListX:4653][T3] for B slice size of two list all equal 0.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][DecList:4830][T3] line: 4832 InitListX failed
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][H264_DecSlice:8257][T3] DecList error, ret=-1
    ```

- Log message \(5\): The IDR frame is missing in the H265 stream.

    ```text
    [HiDvpp][A618] [Vfmw]:hevc_vps_sps_pps_check [Line]:7300 pps with this pic_parameter_set_id = 0 haven't be decoded
    [HiDvpp][A618] [Vfmw]:hevc_dec_slice_segment_header [Line]:3857 hevc_vps_sps_pps_check != HEVC_DEC_NORMAL
    [HiDvpp][A618] [Vfmw]:hevc_inquire_slice_property [Line]:9004 hevc_dec_slice_segment_header dec err
    [HiDvpp][A618] [Vfmw]:hevc_dec_decode_packet[Line]:9004 hevc_inquire_slice_property error.
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_VpsSpsPpsCheck:8084][T10] pps with this pic_parameter_set_id = 0 haven't be decoded
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_DecSliceSegmentHeader:2793][T10] HEVC_VpsSpsPpsCheck != HEVC_DEC_NORMAL
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_InquireSliceProperty:10169][T10] HEVC_DecSliceSegmentHeader dec err
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVCDEC_DecodePacket:753][T10] HEVC_InquireSliceProperty error.
    ```

- Log message \(6\): The I-frame or P-frame is missing in the H.265 stream.

    ```text
    [HiDvpp][A618] [Vfmw]:hevc_ref_pic_process [Line]:3474 ref frame(poc 15) lost.
    [HiDvpp][A618] [Vfmw]:hevc_create_lost_picture [Line]:5839 DPB no suited fs for lost pic.
    [HiDvpp][A618] [Vfmw]:hevc_create_lost_picture [Line]:5847 take poc(17) to create lost poc(15).
    ```

    Or

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480][T10] Ref frame(poc 15) lost.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_CreateLostPicture:6392][T10] DPB no suited fs for lost pic.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480][T10] Ref frame(poc 18) lost.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_CreateLostPicture:6392] [T10] DPB no suited fs for lost pic.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480] [T10] Ref frame(poc 18) lost.
    ```

- Log message \(7\): The I-frame or B-frame is missing in the H.265 stream.

    ```text
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_RefPicProcess:2480] [T56] Ref frame(poc 15) lost.
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][HEVC_CreateLostPicture:6392] [T56] Take poc(17) to create lost poc(15).
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][FSP_SetRef:934] [T56] check condition: pstLogicFs->IsDummyFs == 0 fail
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][FSP_SetRef:934] [T56] check condition: pstLogicFs->IsDummyFs == 0 fail
    [ERROR] DVPP:YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [VDEC][FSP_SetRef:934] [T56] check condition: pstLogicFs->IsDummyFs == 0 fail
    ```

## Possible Cause

The possible causes are as follows:

- Possible cause for log error \(1\): The IDR frame is missing in the H.264 stream.
- Possible cause for log error \(2\): The I-frame is missing in the H.264 stream.
- Possible cause for log error \(3\): The P-frame is missing in the H.264 stream.
- Possible cause for log error \(4\): The B-frame is missing in the H.264 stream.
- Possible cause for log error \(5\): The IDR frame is missing in the H.265 stream.
- For log error \(6\): The I-frame or P-frame is missing in the H.265 stream.
- Possible cause for log error \(7\): The I-frame or B-frame is missing in the H.265 stream.

## Solution

To rectify the fault, perform the following steps:

1. Check the input source stream.

    Use a third-party tool \(for example, eseye u\) to check the input stream.

2. If the source stream is normal, the stream may be damaged when being transmitted to VDEC on the device. In this case, store the stream transmitted to VDEC by using  **fwrite\(\)**  before sending the stream.
    - Use a third-party tool to check the stored stream. If the stream is abnormal, check whether a stream has been sent.

    - Decode the stored stream by using the sample of the corresponding version to check whether the verification stream is normal or whether VDEC supports the format.

        If the sample decoding is normal, it is the development code that causes this problem. You can optimize your VDEC code by referring to the VDEC sample code.
