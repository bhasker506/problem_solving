# Given; a; 32 - bit; signed; integer, reverse; digits; of; an; integer.
#
# Note:
# Assume; we; are; dealing with an environment that could only store integers within the 32-bit signed integer
# range: [−231, 231 − 1].For; the; purpose; of; this; problem, assume; that; your; function; returns; 0; when; the; reversed; integer; overflows.
#
# Example1:
#
# Input: x = 123
# Output: 321
# Example2:
#
# Input: x = -123
# Output: -321
# Example3:
#
# Input: x = 120
# Output: 21

# Example 4:
#
# Input: x = 0
# Output: 0

def solution(number: int):
    rev = 0
    is_negative = True if number<0 else False
    if is_negative:
        number = -1 * number
    while number > 0:
        rem = number % 10
        rev = rev*10 + rem
        number = number//10
    return -1*rev if is_negative else rev


