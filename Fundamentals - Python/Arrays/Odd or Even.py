"""Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"""

def odd_or_even(arr):
    result = 0
    if not arr:
        arr = 0
    for x in range (len(arr)):
        result += arr[x]
    if( result % 2 == 0):
        return "even"
    else:
        return "odd"

arr = [0,-1,-5]
print( odd_or_even(arr) )

# 01/06/2021

# Refined Solution : return 'even' if sum(arr) % 2 == 0 else 'odd'