# Operator Prototype Is Not Registered

## Symptom

An error is reported in the log, indicating that an operator does not have a prototype definition:

```text
op[%s] type[%s] have no ir factory.
```

Or

```text
IR for op[%s] optype[%s] is not registered.
```

>**NOTE:**
>**%s**  in  **op\[%s\] type\[%s\]**  indicates the operator name and operator type.

## Possible Cause

- The operator prototype .so file fails to be loaded.
- The operator type is not registered or compiled into the operator prototype .so file.

## Solution

1. Check whether the operator prototype .so file is successfully loaded.
    - Information displayed if the operator prototype .so file is successfully loaded:

        ```text
        OpsProtoManager plugin load ******/opp/built-in/op_proto/libopsproto.so success.
        ```

    - Key warning information in the case of loading failure:

        ```text
        OpsProtoManager dlopen failed, plugin name:%s. Message(%s).
        ```

2. If the operator prototype .so file is successfully loaded, check whether the operator prototype definition is compiled into the loaded .so file.

    Run the  **nm**  command to view the symbol table of the .so file. If the operator prototype is not registered, register it. For details, see  Operator Development Process \> Operator Prototype Definition  in  [TBE & AI CPU Operator Development](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/others/tbeaicpudevg/atlasopdev_10_0001.html).

    >**NOTE:**
    >You can run the  **nm -D**  command to view the symbol table of the .so file.

3. If the operator prototype .so file fails to be loaded, rectify the fault by referring to the message in the failure warning.
