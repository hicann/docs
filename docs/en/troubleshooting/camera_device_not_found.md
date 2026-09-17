# Failed to Find Devices

## Application Scenario

- Service Scenario: camera image output

- Applicable processor:  Atlas 200I/500 A2 inference products
- Processor forms: EP and RC

## Symptom

The message  **open ISP device error!**  is displayed. The error code  **0xa01c8040**  is returned.

## Possible Cause

The ISP  **.ko**  driver is not inserted.

## Solution

1. Run the  **lsmod**  command to check whether the  **.ko**  driver is inserted.
2. Run the following command to re-insert the AO-related  **.ko**  driver:

    ```bash
    insmod /var/davinci/driver/drv_isp.ko
    ```

3. Perform the camera service again.
