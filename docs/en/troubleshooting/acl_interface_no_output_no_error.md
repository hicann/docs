# No Error Reported When acl API Execution Produces No Output

## Symptom

During acl API calling, no API error is reported, but the expected result is not output.

## Possible Cause

- The .so file in  **stub**  is linked during acl API execution.
- In the asynchronous scenario, stream synchronization is not performed during output data copy.

## Solution

For the first case, run the  **ldd**  command to check whether the .so file linked to the execution file is correct. Ensure that a valid .so file is linked.

For the second case, with asynchronous APIs, the API call only indicates that tasks are delivered. The asynchronous APIs return a success response to the host thread before the tasks are completed. You need to call an explicit synchronization API \(for example,  **aclrtSynchronizeStream**\) to block the host thread and wait until the tasks are completed. Otherwise, service exceptions \(such as training or inference exceptions\) or unknown situations \(such as device link or card disconnections\) may occur.
