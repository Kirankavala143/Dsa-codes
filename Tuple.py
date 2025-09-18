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

# tuple1 = tuple(map(int, input().split()))
# sorted_tuple = sorted(tuple1, reverse=True)
# second_largest = sorted_tuple[1]
# print(second_largest)

# Question 5
# Title: Tuple Elements in Reverse Pairs

# Problem Statement:
# Given a tuple of even number of elements, group them into pairs and reverse each pair.
# def reverse_pairs(tup):
#     # Group into pairs using zip and unpacking
#     pairs = list(zip(tup[::2], tup[1::2]))  # [(1,2), (3,4), ...] even
#     result = [i for a, b in pairs for i in (b, a)]
    
#     return tuple(result)

# print(reverse_pairs((1, 2, 3, 4)))         # Output: (2, 1, 4, 3)
# print(reverse_pairs((5, 6, 7, 8, 9, 10)))  # Output: (6, 5, 8, 7, 10, 9)

# numbers = tuple(map(int, input().split()))
# result = ()
# for i in range(0, len(numbers), 2):
#     result += (numbers[i+1], numbers[i])
# print(result)


# Question 6
# Title: Filter Positive Numbers from Tuple

# Problem Statement:
# Given a tuple of integers, filter out all negative numbers and print a tuple containing only the positive values.

# tuple1 = tuple(map(int, input().split()))
# filtered_tuple = tuple(filter(lambda x: x > 0, tuple1))
# print(filtered_tuple)

# Question 7
# Title: Create Tuple from First N Natural Numbers

# Problem Statement:
# Given a number N, create a tuple that contains the first N natural numbers (starting from 1).

# n = int(input())
# tuple1 = tuple(range(1, n + 1))
# print(tuple1)

# Question 8
# Title: Count Even and Odd Numbers in Tuple
# Problem Statement:
# Given a tuple of integers, count how many even and how many odd numbers it contains.

# tuple1 = tuple(map(int, input().split()))
# even_count = len(list(filter(lambda x: x % 2 == 0, tuple1)))
# odd_count = len(list(filter(lambda x: x % 2 != 0, tuple1)))
# print("Even count:", even_count)
# print("Odd count:", odd_count)

#another way
# a=tuple(map(int,input().split()))
# even=0
# odd=0
# for i in a:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)

# Question 9
# Title: Multiply All Elements of Tuple# Problem Statement:
# You are given a tuple of integers. Write a program to compute the product of all elements in the tuple.

# tuple1 = tuple(map(int, input().split()))
# product = 1
# for i in tuple1:
#     product *= i
# print(product)

# Question 10
# Title: Find the Minimum and Maximum Elements in a Tuple   
# Problem Statement:
# You are given a tuple of integers. Write a program to find the minimum and maximum elements in the tuple.

# tuple1 = tuple(map(int, input().split()))
# min_element = min(tuple1)
# max_element = max(tuple1)
# print("Minimum element:", min_element)
# print("Maximum element:", max_element)    

# Question 10
# Title: Remove First and Last Element of Tuple
# Problem Statement:
# Given a tuple, create a new tuple after removing the first and last elements.

# tuple1 = tuple(map(int, input().split()))
# new_tuple = tuple1[1:-1]
# print(new_tuple)

# Title: Create Tuple from User-defined Range

# Problem Statement:
# Given two integers start and end, create a tuple of numbers from start to end (inclusive).

# start = int(input())
# end = int(input())
# tuple1 = tuple(range(start, end + 1))
# print(tuple1)

# Question 12
# Title: Find Tuple Element with Maximum Frequency
# Problem Statement:
# Given a tuple of values, find and print the element that appears most frequently.

# tuple1 = tuple( input().split())
# max_count = max(tuple1, key=tuple1.count)
# print(max_count)

# a=tuple(input().split())
# for i in dict.fromkeys(a):
#     print(f"{i}:{a.count(i)}")




# xor on tuple
# nums=tuple(map(int,input().split()))
# res=nums[0]
# for n in nums[1:]:
#     res^=n 
# print(res)

# bitwise and
# a=tuple(map(int,input().split()))
# b=tuple(map(int,input().split()))
# print(tuple(a[i] & b[i] for i in range(len(a))))

# convert binary to decimal
# a=tuple(input().split())
# print(int(''.join(a),2))

# moduls
# nums=tuple(map(int,input().split()))
# res=nums[0]
# for i in nums[1:]:
#     res %=i 
# print(res)

# Python program to find tuples which have all elements divisible by K from a list of tuples
# Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6

# Output : [(6, 24, 12), (60, 12, 6)]

# test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
# K = 6
# result = [t for t in test_list if all(t[i] % K == 0 for i in range(len(t)))]
# print(result)

# another way
# test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
# K = 6
# result = []
# for t in test_list:
#     if all(t[i] % K == 0 for i in range(len(t))):
#         result.append(t)
# print(result)

# l=[]
# n=int(input())
# for i in range(n):
#     l.append(tuple(map(int,input().split())))
# k=int(input())
# for i in l:
#     if all(i[j]%k==0 for j in range(len(i))):
#         print(*i)

# test_list = []
# n = int(input())

# for i in range(n):
#     element = list(map(int, input().split()))
#     test_list.append(tuple(element))  # FIXED this line
# k = int(input())
# res = []
# for tup in test_list:
#     if all(element % k == 0 for element in tup):  # FIXED spacing
#         res.append(tup)
# for t in res:
#     print(*t)






# n=int(input())
# l=[tuple(map(int,input().split())) for i in range(n)]
# k=int(input())
# for t in l:
#     if all(x%k==0 for x in t):
#         print(*t)

# filter the postive number using list comprehension
# n=int(input())
# l=list(map(int,input().split()))
# l=[x for x in l if x>0]
# print(*l)

# sort a dictionary by keys
n = int(input())
data = {}
for _ in range(n):
    name, score = input().split()
    data[name] = int(score)

for name in sorted(data):
    print(f"{name}: {data[name]}")

#  print 1 letter of the words














