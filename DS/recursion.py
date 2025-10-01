# RECURSION
# Recursion is when a function calls itself to solve a smaller version of the same problem until a base condition is reached.

# 2. Components of Recursion
# Base Case → The condition where recursion stops (to prevent infinite calls).
# Recursive Case → Function calls itself with a smaller input.

# Factorial Problem
# def factorial(n):
#     if n == 0 or n == 1:  # base case
#         return 1
#     return n * factorial(n-1)  # recursive case

# print(factorial(5))

# Fibonacci
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

# Sum of Natural Numbers
# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n-1)

# print(sum_n(5))

# Print 1 to N
# def print_numbers(n):
#     if n == 0:
#         return
#     print_numbers(n-1)
#     print(n, end=" ")

# print_numbers(5)

# Reverse a string using recursion
# def reverse_string(s):
#     if len(s) == 0:
#         return ""
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("hello"))

# Palindrome check
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])

# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))

# Count digits of a number
# def count_digits(n):
#     if n == 0:
#         return 0
#     return 1 + count_digits(n//10)

# print(count_digits(12345))