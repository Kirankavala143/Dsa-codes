# print 1 to n using recursion

# def print1ton(n):
#     if n==1:
#         print(1)
#         return
#     print1ton(n-1)
#     print(n)
# print1ton(5)

# def printNto1(n):
#     if n==1:
#         print(1)
#         return
#     print(n)
#     printNto1(n-1)
# printNto1(5)

# sum of first n numbers
# def sumN(n):
#     if n==1:
#         return 1
#     return n + sumN(n-1)
# print(sumN(5))

# factorial
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))    

# reverse a array


# def reverse(arr):
#     if not arr:  # Base case: empty list
#         return []
#     return [arr[-1]] + reverse(arr[:-1])

# print(reverse([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

# def reverse(arr):
#     return arr[::-1]

# print(reverse([1, 2, 3, 4, 5]))

# check if a string is palindrome or not

# fibnoccai number recursion sequence
def fibnocci(n):
    if n==1 or n==2:
        return 1
    return fibnocci(n-1) + fibnocci(n-2)
print(fibnocci(5))  