# Index Operator Out of Range

## Symptom

The host application logs \(**log/\[run|debug\]/plog/plog-_pid_\__\*_.log**\) contain the  **0x800000**  error of the index operator.

Common index operators include GatherV2 \(the API corresponding to PyTorch is  **index\_select**\), Scatter \(the API corresponding to PyTorch is  **scatter\_update**\), and GatherElements \(the API corresponding to PyTorch is  **gather**\). Generally, the input names of this type of operators are  **index**  and  **indices**.

## Fault Root Causes

Due to performance reasons, operators of this type cannot perform index out-of-range check. Therefore, the error cannot be correctly reported. When the index is out of range, the AI Core error of the  **0x800000**  may occur.

## Solution

Take the GatherV2 operator as an example. The API of PyTorch corresponding to this operator is  **index\_select**:

```python
torch.index_select(input, dim, index, *, out=None)
```

This operator involves parameters such as  **input**,  **dim**, and  **index**. If  **0x800000**  is displayed for this operator, use the Python printing function to print the shape information of  **input**, and the values of  **dim**  and  **index**. Further, it is determined that the index is out of range. Search for the source of the index by viewing the code. The rules are as follows:

```python
0 <= index[i] < input.shape[dim]
```
