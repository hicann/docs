# Callback Function Not Triggered When VDEC Fails to Decode Video Frames

## Symptom

When a stream is input to VDEC for decoding, the callback function is not triggered for some or all frames. As a result, you cannot receive the decoding result.

## Possible Cause

Some frames in the stream are bad frames, which the syntax fails to parse or decode, resulting in the callback function not called.

## Solution

To rectify the fault, perform the following steps:

1. Check whether the log contains the error information in  [Frame Loss or Packet Loss During VDEC Video Decoding](vdec_decode_frame_drop.md). If yes, the callback function is not called because the exception frames fail to be decoded.
2. If the error in  [Frame Loss or Packet Loss During VDEC Video Decoding](vdec_decode_frame_drop.md)  is not displayed, modify the DVPP module or change the global log level to  **info**  and check whether the total number of times that the following logs are printed is the same as the number of input frames.

    - <u>\(1\) "The queue is empty, so call the non-intelligent pointer callback interface."</u>
    - <u>\(2\) "The queue is not empty, so call the smart pointer callback interface."</u>
    - <u>\(3\) "The queue is not empty, but hiai\_data\_sp is nullptr."</u>

    The preceding types of logs are generated in the following scenarios:

    - **hiai\_data\_sp**  is not used. Data is successfully decoded and returned, log \(1\) is printed, and the callback function registered by the user is called.
    - Each frame corresponds to a setting of  **hiai\_data\_sp**. Data is successfully decoded and returned, log \(2\) is printed, and the callback function registered by the user is called.
    - Set  **hiai\_data\_sp**  for  _N_  frames. If the first frame is successfully decoded and returned, log \(2\) is printed, and the callback function registered by the user is called. For other  _N_–1 frames, log \(3\) is printed after successful decoding, and the callback function registered by the user is called.

    The callback function registered by the user is called in either of the preceding scenarios. That is, if the user callback function is called once, a decoded frame is returned. Therefore, if the total number of occurrences of the preceding three logs is equal to the total number of frames input by the user, no frames are lost during decoding. In this case, check whether the statistics of the decoding results received by the user are correct.
