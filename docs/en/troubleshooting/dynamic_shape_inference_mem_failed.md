# Failure in Allocating Memory for Dynamic-Shape Inference

## Symptom

When memory with  **size = 0**  is allocated during model inference, the error log contains the following key information:

```text
[INFO] ASCENDCL ****** start to execute aclrtMalloc, size = 0
[ERROR] ASCENDCL ****** malloc size must be greater than zero
```

## Possible Cause

The model is a dynamic-shape model, with the output shape containing  **-1**. Therefore, the value of  **size**  obtained by calling  **aclmdlGetOutputSizeByIndex**  is  **0**.

Then, the memory with  **size = 0**  is allocated. As a result, a failure occurs.

## Solution

If the value of  **size**  obtained by  **aclmdlGetOutputSizeByIndex**  is  **0**, you need to predict a large memory block.
