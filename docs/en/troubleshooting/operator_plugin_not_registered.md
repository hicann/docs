# Operator Plugin Is Not Registered

## Symptom

An error is reported in the log, indicating that an operator type is not supported.

```text
Check op[%s]'s type[%s] failed, it is not supported.
```

Or

During model conversion, the type of an operator is converted into the  **frameworkop**  type, which does not meet the expectation.

## Possible Cause

- The operator plugin .so file fails to be loaded.
- Mapping is not registered for the operator or not compiled into the .so plugin of the operator.

## Solution

1. Check whether the operator plugin .so file is successfully loaded.
    - Information displayed if the operator plugin .so file is successfully loaded:

        ```text
        plugin load ******/opp/built-in/framework/onnx/libops_all_onnx_plugin.so success.
        ```

    - Key warning information in the case of loading failure:

        ```text
        dlopen failed, plugin name:%s. Message(%s).
        ```

2. If the operator plugin .so file is successfully loaded, check whether the mapping registered by the operator is compiled into the loaded .so file.

    Run the  **nm**  command to view the symbol table of the .so file. If the operator plugin is not registered, register it. For details, see  Operator Development Process \> Operator Adaptation  in  [TBE & AI CPU Operator Development](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/others/tbeaicpudevg/atlasopdev_10_0001.html).

    >**NOTE:**
    >You can run the  **nm -D**  command to view the symbol table of the .so file.

3. If the operator plugin .so file fails to be loaded, rectify the fault by referring to the message in the failure warning.
