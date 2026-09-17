# Single-Operator Matching Failure

## Symptom

During the execution of a single-operator, the matching fails. Information similar to the following is displayed in the log:

Offline loading:

```text
EH9999 [Match][OpModel]failed to match model, opName = xxx Has not been compiled or loaded, please make sure the op executed and the op compiled is matched, you can check the op type, op inputs number, outputs number, input format, origin format, datatype, memtype, attr, dim range, and so on.
```

Online loading:

```text
EH9999 [Match][OpModel]MatchOpModel fail from static map or dynamic map. Please make sure the op executed and the op compiled is matched, you can check the op type, op inputs number, outputs number, input format, origin format, datatype, memtype, attr, dim range, and so on.
```

## Possible Cause

- Offline scenario: The .om file of an operator does not exist in the directory specified by  **aclSetModelDir**.
- Online scenario: Some special matching rules are not adapted. As a result, operators fail to be matched.

## Solution

- Offline scenario: Recompile the missing operators and copy them to the directory specified by  **aclSetModelDir**. The remaining steps are the same as those for offline single-operator inference.
- Online scenario: Check that the  **opType**,  **dataType**, and  **format**  information of the compiled operators is consistent based on the reported error.
