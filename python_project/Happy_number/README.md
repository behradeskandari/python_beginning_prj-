# Happy Number Checker

## Overview
This Python script defines a function `is_happy_number` that checks whether a given number is a happy number or not. A happy number is a number that eventually reaches 1 when replaced by the sum of the square of each digit.

## Function: `is_happy_number(n)`
The function takes an integer `n` as input and returns `True` if `n` is a happy number and `False` otherwise.

### Algorithm
The function uses a set to keep track of seen numbers to detect cycles. It iteratively calculates the sum of the squares of the digits of the current number until either the number becomes 1 (a happy number) or enters a cycle.

## Usage
```python
# Example Usage
number_to_check = 19
result = is_happy_number(number_to_check)