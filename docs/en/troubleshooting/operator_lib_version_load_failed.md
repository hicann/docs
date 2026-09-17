# Failure in Loading a Single Operator Due to an OPP Version Issue

## Symptom

An error is reported during the loading of a single operator. Information similar to the following is displayed in the log:

```text
E19999: Inner Error
E19999 The opp version of the model does not match the current opp run package, Model is [6.4.T11.0.B300], opp run package is [7.0.T3.0.B107], try to convert the om again!
```

## Possible Cause

In the dynamic shape operator or  Ascend virtual instance  scenario, the OPP version \(**Ascend-cann-toolkit\__\{version\}_  \_linux-_\{arch\}_.run**\) installed in the data loading environment of the single-operator model is inconsistent with that in the OM model file compilation environment. As a result, an error is reported when the operator is loaded.

## Solution

In the dynamic shape operator or  Ascend virtual instance  scenario, the OPP version installed in the data loading environment of the single-operator model must be the same as that in the OM model file compilation environment. If an error is reported, check the installed OPP version, change the OPP version in the operator loading environment or that in the operator OM file compilation environment. If you change the OPP version in the OM model file compilation environment, you need to convert the model again.
