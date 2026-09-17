# EL0017 Invalid\_Argument\_Null\_Pointer

## Symptom

The following is error format. The meanings of the placeholders %s in sequence are: API name, parameter name.

```text
%s failed because %s cannot be a null pointer.
```

Error example:

```text
halEschedQueryInfo failed because inPut cannot be a null pointer.
```

## Solution

Try again with a correct pointer argument.
