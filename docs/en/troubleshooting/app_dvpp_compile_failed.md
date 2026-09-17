# Application Building Failure Due to DVPP APIs

## Symptom

DVPP APIs are not defined, leading to a building error. The log keywords include  **undefined reference to \*\*\***.

## Possible Cause

The possible cause is as follows:

The DVPP APIs are packed into  **libacl\_dvpp.so**. Test cases use the DVPP APIs but are not linked to  **libacl\_dvpp.so**.

## Solution

To rectify the fault, perform the following steps:

Check whether test cases use the DVPP APIs that are not linked to the  **libacl\_dvpp.so**. If no, link  **libacl\_dvpp.so**  in the build file.

Check whether the  **target\_link\_libraries\(\)**  option in  **CmakeLists**  is connected to the  **acl\_dvpp**  target.

Example:

```cmake
add_executable(main
utils.cpp
main.cpp)
target_link_libraries(main
ascendcl acl_dvpp stdc++)
```
