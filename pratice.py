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


# You are given a tuple of integers. Your task is to remove all even numbers and return a tuple with only odd numbers.
# filter()-returns elements lambda return bool values

# a=tuple(map(int,input().split()))
# b=tuple(filter(lambda x:x%2!=0,a))
# print(b)

# another method
# def odd(num):
#     return num%2!=0
# a=tuple(map(int,input().split()))
# b=tuple(filter(odd,a))
# print(b)

def odd(num):
    a=tuple(i for i in num if i%2!=0)
    return a

num=(1,2,3,4,5)
print(odd(num))


