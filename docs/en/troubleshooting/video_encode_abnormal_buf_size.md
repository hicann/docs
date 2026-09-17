# Video Encoding Is Abnormal Because the buf\_size Parameter Is Improperly Set

In video encoding scenarios, the encoding buffer size is set by  **buf\_size**  in  **hi\_venc\_attr**. If  **buf\_size**  is improperly set, video encoding may take a long time or fail.

## Symptom and Possible Cause  \(Ascend RC\)

If video encoding takes a long time or fails, run the  **proc**  command to locate the fault. In the  **proc**  query result, pay attention to the following key information:  **EncStart**  indicates the number of frames to be encoded;  **EndSuccessed**  indicates the number of frames that are successfully encoded;  **Lost**  and  **Disc \(discard\)**  indicate the number of frames that fail to be encoded; and  **Recode**  indicates the number of recoding times.

1. Log in to the device when the encoding process is running.
2. Run the  **cat /proc/umap/h265e**  or  **cat /proc/umap/h264e**  command.
    - The symptom highlighted in the red box in the following figure is displayed. That is, the  **Lost**  and  **Disc**  numbers are 0 or very small, but the  **Recode**  number is large, indicating that most frames can be successfully encoded but there are too many times of recoding.

        When the actual size of the encoding result is greater than the available buffer size in the encoding buffer, the encoding module automatically adjusts the parameters and recodes the frames to reduce the encoding result size. Therefore, if the value of  **buf\_size**  is too small, the number of buffer frames is small. As a result, the probability of recoding is high, the encoding delay increases, the frame rate decreases, and the performance deteriorates.

        ![](figures/image_0000001927915741.png)

    - The symptom highlighted in the red box in the following figure is displayed. That is, the  **Lost**,  **Disc**, and  **Recode**  numbers are large, indicating that a large number of frames fail to be encoded.

        When the actual size of the encoding result is greater than the available buffer size in the encoding buffer, the encoding module automatically adjusts the parameters and recodes the frames to reduce the encoding result size. If the number of recoding times is used up but the encoding result size is still greater than the available buffer size, the encoding module discards the frame. Therefore, if the value of  **buf\_size**  is too small, the number of buffer frames is small. As a result, there are high probabilities of recoding and frame loss.

        ![](figures/image_0000001927835357.png)

## Symptom and Possible Cause \(Ascend EP\)

If video encoding takes a long time or fails, use the  **proc**  information of DVPP to locate the fault. In the  **proc**  information,  **EncStart**  indicates the number of frames to be encoded;  **EndSuccessed**  indicates the number of frames that are successfully encoded;  **Lost**  and  **Disc \(discard\)**  indicate the number of frames that fail to be encoded; and  **Recode**  indicates the number of recoding times.

1. After running the encoding process, log in to the host and run the  **msnpureport -a**  command in the directory on which you have the read, write, and execute permissions to export the log information of the device.
2. Go to the directory with the timestamp that corresponds to the export time and open the  **module\_info\\dev-os-0\\dvpp\\dvpp\_proc.log**  file.
    - The symptom highlighted in the red box in the following figure is displayed. That is, the  **Lost**  and  **Disc**  numbers are 0 or very small, but the  **Recode**  number is large, indicating that most frames can be successfully encoded but there are too many times of recoding.

        When the actual size of the encoding result is greater than the available buffer size in the encoding buffer, the encoding module automatically adjusts the parameters and recodes the frames to reduce the encoding result size. Therefore, if the value of  **buf\_size**  is too small, the number of buffer frames is small. As a result, the probability of recoding is high, the encoding delay increases, the frame rate decreases, and the performance deteriorates.

        ![](figures/image_0000001881876550.png)

    - The symptom highlighted in the red box in the following figure is displayed. That is, the  **Lost**,  **Disc**, and  **Recode**  numbers are large, indicating that a large number of frames fail to be encoded.

        When the actual size of the encoding result is greater than the available buffer size in the encoding buffer, the encoding module automatically adjusts the parameters and recodes the frames to reduce the encoding result size. If the number of recoding times is used up but the encoding result size is still greater than the available buffer size, the encoding module discards the frame. Therefore, if the value of  **buf\_size**  is too small, the number of buffer frames is small. As a result, there are high probabilities of recoding and frame loss.

        ![](figures/image_0000001882036518.png)

## Solution

Set the  **buf\_size**  parameter properly when creating an encoding channel. For details, see the description of the  **buf\_size**  member in  **hi\_venc\_attr**.
