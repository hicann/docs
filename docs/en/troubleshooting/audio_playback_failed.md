# Abnormal Audio Playing

## Application Scenario

- Service scenario: audio playing
- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

The audio cannot be played normally, and the error code  **0xa0168009**  is returned.

```text
sample_comm_audio_start_ao: hi_mpi_ao_set_pub_attr(2) failed with 0xa0168009!
```

## Possible Cause

The audio-related  **.ko**  driver is not inserted.

## Solution

1. Run the  **lsmod**  command to check whether the  **.ko**  driver is inserted.
2. Run the following command to re-insert the AO-related  **.ko**  driver:

    ```bash
    insmod /var/davinci/driver/drv_ao.ko
    ```

3. Run the audio playing command again.
