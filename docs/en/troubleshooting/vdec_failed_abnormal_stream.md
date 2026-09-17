# VDEC Failure Due to Abnormal Streams

## Symptom

**hi\_mpi\_vdec\_get\_frame**  is called successfully, but a decoding failure \(**frame\_info-\>v\_frame.frame\_flag = 1**\) is returned, because the input stream is abnormal or the configured stream format is inconsistent with the actual stream format.

Examples of common syntax parsing errors:

- Log example 1

    ```text
    pid 0 usr chn 0 device 0 chn 0, input stream error, can't decode, report to user
    ```

- Log example 2

    ```text
    ppssps_check_tmp_id: pps is null with this pic_parameter_set_id = 1 haven't decode
    ```

- Log example 3

    ```text
    PPS or SPS of this slice not valid
    ```

- Log example 4

    ```text
    sliceheader dec err
    ```

- Log example 5

    ```text
    H264DEC inquire_slice_property error
    ```

- Log example 6

    ```text
    hevc_inquire_slice_property error
    ```

- Log example 7

    ```text
    ref frame(poc 15) lost
    ```

- Log example 8

    ```text
    SH hevc_dec_short_term_ref_pic_set error
    ```

- Log example 9

    ```text
    p_temp_r_pset->num_negative_pics(66) out of range(0,15)
    ```

## Possible Cause

**frame\_flag = 1**  indicates that the decoding fails. The possible cause is that the input streams sent to the VDEC template are abnormal, or the streams are abnormal due to frame loss of broadcast packets caused by unstable network. As a result, an error is reported during decoding. In this case, you can save the input stream to check for any exception.

## Solution \(Ascend RC  Form\)

1. After successfully calling  **hi\_mpi\_vdec\_send\_stream**, write the input streams to a file as to save the streams. The reference code is as follows:

    ```c
        ret = hi_mpi_vdec_send_stream(chn, stream, vdec_pic_info, milli_sec);
        if (ret == HI_SUCCESS) {
            FILE *fd = NULL;
            fd = fopen("input_stream", "a+");
            fwrite(stream->addr, stream->len, 1, fd);
            fclose(fd);
        }
    ```

2. Use a third-party tool to view the saved input stream and check for any exception such as artifacts or error messages.

## Solution \(Ascend EP  Form\)

1. After successfully calling  **hi\_mpi\_vdec\_send\_stream**, write the input streams to a file as to save the streams. The reference code is as follows:

    Transmit the stream data from the host to the device, and then send the decoded stream.

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

2. Use a third-party tool to view the saved input stream and check for any exception such as artifacts or error messages.
