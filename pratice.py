# <!-- Title: Square of Each Element in Tuple
# Problem Statement:
# You are given a single line of space-separated integers. Your task is to store them in a tuple and create a new tuple where each element is the square of the original. -->

# tuple1 = tuple(map(int, input().split()))
# tuple2 = tuple(map(lambda x: x * x, tuple1))
# print(tuple2)

# a=tuple(map(int,input().split()))
# b=tuple(map(lambda x:x**2,a))
# print(b)

# another method
# def sqauree(numbers):
#     a=tuple(i**2 for i in numbers)
#     return a

# numbers=(1,2,3,4,5)
# print(sqauree(numbers))

# Question 2
# Title: Remove Even Numbers from Tuple
# Problem Statement:
# You are given a tuple of integers. Your task is to remove all even numbers and return a tuple with only odd numbers.
# FILTER()-returns elements lambda return bool values

# a=tuple(map(int,input().split()))
# b=tuple(filter(lambda x:x%2!=0,a))
# print(b)

# another method
# def odd(num):
#     return num%2!=0
# a=tuple(map(int,input().split()))
# b=tuple(filter(odd,a))
# print(b)

# def odd(num):
#     a=tuple(i for i in num if i%2!=0)
#     return a

# num=(1,2,3,4,5)
# print(odd(num))

# Question 3
# Title: Tuple Index-wise Addition
# Problem Statement:
# You are given two tuples of equal length. Add the corresponding elements of both tuples and print the resulting tuple.

# tuple1 = tuple(map(int, input().split()))
# tuple2 = tuple(map(int, input().split()))
# tuple3 = tuple(map(lambda x, y: x + y, tuple1, tuple2))
# print(tuple3)

# ZIP
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# zipped = zip(list1, list2)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# def sum(num1,num2):
#     result=tuple(a+b for a,b in zip(num1,num2))
#     return result

# num1=(1,2,3)
# num2=(4,5,6)
# print(sum(num1,num2))

# Question 4
# Title: Find Second Largest Number in Tuple
# Problem Statement:
# Given a tuple of integers, find and print the second largest element.

tuple1 = tuple(map(int, input().split()))
sorted_tuple = sorted(tuple1, reverse=True)
print(sorted_tuple)
second_largest = sorted_tuple[1]
print(second_largest)