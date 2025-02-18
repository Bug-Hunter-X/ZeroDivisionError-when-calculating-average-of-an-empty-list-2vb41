# Python ZeroDivisionError Bug
This repository demonstrates a common Python bug: a `ZeroDivisionError` that occurs when attempting to calculate the average of an empty list. The bug and its solution are provided in separate Python files.

## Bug Description
The `calculate_average` function fails to handle empty lists, resulting in a `ZeroDivisionError` when the input list is empty. This occurs because the code divides by `len(numbers)`, which is zero for an empty list.

## Solution
The solution file shows how to handle this error gracefully by checking if the list is empty before performing the calculation. If the list is empty, the function returns 0, avoiding the division by zero.
