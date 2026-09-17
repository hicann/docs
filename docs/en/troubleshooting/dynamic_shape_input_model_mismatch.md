# User Input of the Dynamic-Shape Model Does Not Match the Model Inference Result

## Symptom

**Scenario 1**: An error is reported in the model execution. The log contains the following key information:

```text
[INFO] GE(2284607, ir_build):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task_context.cc:257]2284607 AllocateOutput: To allocate output for node: add2. index = 0, tensor desc = [TensorDescl DataType = 6 , Format = 2 · Shape = [50, ]
[ERROR] GE(2284607, ir_build):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [task_context.cc:257]2284607 AllocateOutput: ErrorNo: 50331649() [LOAD][LOAD][Check][Size] add2(Add) index[0] mem size out of range! Expected size: 128, but given input size: 2.
```

**Scenario 2**: An error is reported in the single-operator scenario. The log contains the following key information:

```text
[INFO] GE(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [single op.cc:161]131511 ValidateArgs:lnput [1], aligned_size:96, inputs.length:40, input_sizes_:96
[INFO] GE(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [single op.cc:186]131511 ValidateArgs:Output [0], aligned_size:3145760, outputs.length:3145728, input_sizes_:18446744073709551615
[ERROR] GE(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [single op.cc:161]131511 ValidateArgs: ErrorNo: 145000(Parameter invalid.) [FINALI][FlNALl][CheCkl][Param.Outputs]Output Size mismatch. index = 0, model expect  18446744073709551615, but given ....
[ERROR] ASCENDCL(130191,python):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [op_executor.cpp:68]131511 DoExecteAsync:  [FINALI][FlNALl][Exec][Op]Execute op failed. ge result = 145000
```

## Possible Cause

**Scenario 1:**

During model execution, the size of  **output\_buffer**  allocated by the user does not match that output by the model after layers of infershape.

**Scenario 2:**

In the single-operator scenario, the size of  **output\_buffer**  allocated by the user does not match  **output\_size**  computed by infershape during single-operator compilation.

## Solution

To rectify the fault, perform the following steps:

**For scenario 1:**

If this error occurs, check whether the size of the allocated  **output\_buffer**  is correct. The size must be the same as that inferred by the model. You are advised to allocate  **output\_buffer**  based on the size specified in the reported error message.

**For scenario 2:**

If this error occurs, check whether the size of the allocated  **output\_buffer**  is the same as  **size**  specified by infershape. You are advised to allocate the buffer based on the error message.
