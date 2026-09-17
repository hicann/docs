# The Brightness and Darkness of the VENC-Encoded Streams Are Different from Those of the Original YUV

## Symptom

When a user uses a third-party player to play a stream encoded by VENC, the brightness and darkness of the encoded stream differs from those of the original YUV.

## Possible Cause

Due to the uncontrollable rendering effect of the player, when decoding and displaying the stream content, the player's target pixel value range is inconsistent with the  **video\_full\_range\_flag**  set in VENC encoding. This results in pixel value range mapping and causes inconsistency in brightness and darkness between the encoded stream and the original YUV.

For details about the  **full\_range**, see  [See Also](#section98371392323).

## Solution

You are not advised using a player to check the brightness and darkness effect, because the rendering effect of the player is uncontrollable. It is recommended that the VENC stream be decoded into a YUV file and compare it with the original YUV. At the same time, ensure that the  **video\_full\_range\_flag**  is used consistently during encoding and decoding.

1. Specify the value of the  **video\_full\_range\_flag**  during VENC encoding.

    For H.264 and H.265 streams on the  Atlas inference products, the default value of the  **video\_full\_range\_flag**  is  **0**  \(indicating  **limited\_range**\) during VENC encoding.

    On the  Atlas 200I/500 A2 inference products, the default value of the  **video\_full\_range\_flag**  is  **0**  \(indicating  **limited\_range**\) for H.265 streams and  **1**  \(indicating  **full\_range**\) for H.264 streams.

    **If the default value does not meet the requirements, you can call hi\_mpi\_venc\_set\_h264\_vui or hi\_mpi\_venc\_set\_h265\_vui to change the value of video\_full\_range\_flag.**

2. Check the  **video\_full\_range\_flag**  of the stream encoded by VENC.

    Use a stream analysis tool to check the  **value of video\_full\_range\_flag**  in the SPS field. If the value of  **flag**  is  **1**, the original YUV is  **full\_range**. If the value of  **flag**  is  **0**, the original YUV is  **limited\_range**.

    ![](figures/image_0000001927915793.png)

3. Specify  **video\_full\_range\_flag**  during decoding, and then compare the decoded YUV file with the original YUV file in terms of brightness and darkness.

    The  **video\_full\_range\_flag**  usage varies depending on the decoder. The following uses FFmpeg as an example. You can use the  **-vf**  option to specify the target output  **video\_full\_range\_flag**. The default output is  **limited\_range**.

    FFmpeg is used as an example. The example command is as follows:

    ```bash
    ffmpeg -i ${instream} -pix_fmt nv12 -vf scale=out_range=full/limited -y ${outyuv}
    ```

    **The following uses examples to describe the brightness/darkness contrast**. Currently, the YUV format is  **full-range**. Therefore, the scenario where the source YUV format is  **limited-range**  is excluded. Considering the four combinations of VENC and FFmpeg parameters,  **vui**  indicates  **video\_full\_range\_flag**  set during VENC encoding, and  **ffmpeg**  indicates  **video\_full\_range\_flag**  set during FFmpeg decoding.

    - The results of  **vui0\_ffmpeg0**  and  **vui1\_ffmpeg1**  are the same, and those of the source YUV are also the same. This is because the  **vui**  and  **ffmpeg**  parameters are consistent and the YUV data is directly decompressed and output.
    - The  **vui0\_ffmpeg1**  image appears darker because  **ffmpeg**  requires a conversion from  **limited\_range**  to  **full\_range**, which results in the stretching of the pixel value distribution towards both ends. This is exacerbated by the fact that the scene itself is already dark, causing a larger number of pixel values to shift towards 0. Consequently, the image appears darker than it actually is.
    - The  **vui1\_ffmpeg0**  image appears brighter because the  **ffmpeg**  value range is compressed from 0–255 to 16–235. This compression causes a significant number of low pixel values to move to the middle range, resulting in a brighter image.

    ![](figures/image_0000001927835405.png)

<a id="section98371392323"></a>

## See Also

Generally, a TV supports 240 color levels ranging from 16 to 255, that is,  **limited\_range**. The corresponding YUV value ranges are Y \[16, 235\] and UV \[16, 240\].

A modern computer supports 255 color levels, ranging from 0 to 255, that is,  **full\_range**. The corresponding YUV value range is YUV \[0, 255\].

The following flags are equivalent in different software or modules:

- **"full range" = "jpeg" = "pc" = "cg" = "high rgb"**
- **"limited range" = "mpeg" = "tv" = "broadcast" = "low rgb"**

In the VUI field of H.265 streams,  **video\_full\_range\_flag = 0**  indicates that the original YUV is  **limited\_range**, and  **video\_full\_range\_flag = 1**  indicates that the original YUV is  **full\_range**. Note that  **this flag bit does not affect the VENC encoding process**. The stream data produced during encoding is solely determined by the actual pixel values of the input YUV. Pixel value mapping does not take place during the encoding process.

For example, during FFmpeg decoding, the system checks whether the original YUV format matches the output YUV format.  **Pixel value remapping is only initiated when there is a mismatch between the two YUV formats.**  If the original YUV format is  **full\_range**,  **video\_full\_range\_flag**  is set to 1 for VENC encoding. If the output YUV format after FFmpeg decoding is  **limited\_range**, the YUV format is degraded from  **full\_range**  to  **limited\_range**. Therefore, pixel values are mapped from \[0, 255\] to \[16, 235\] after decoding. This results in a difference in brightness and darkness between the decoded YUV and the original YUV.
