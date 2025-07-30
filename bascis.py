# sum of digits
# n = int(input())
# total = 0
# for i in str(n):
#     total += int(i)
# print(total)

# Sum of Digit of a Number using Recursion

# def sum_digit(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digit(n // 10)

# n = int(input())
# print(sum_digit(n))

# no of digits
# n=543654
# n=str(n)
# print(len(n))

#  Print Binary Equivalent of a Number

# n = int(input())
# a=bin(n)
# print(a[2:])

# to find prime numbers
# n = 47
# for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# # n to m

# n=9
# m=50
# for i in range(n,m+1):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         print(i)

# perfect number
# n=6
# total=0
# for i in range(1,n):
#     if n%i==0:
#         total+=i
# if n==total:
#     print("perfect")
# else:
#     print("not perfect")

# sum of first n natural numbers
# n=4
# sum=0
# while n>0:
#     sum+=n
#     n-=1
# print(sum)

# strong number
# import math
# n=145
# temp=n
# total=0

# while temp>0:
#     digit=temp%10
#     total+=math.factorial(digit)
#     temp=temp//10

# if total==n:
#     print("strong")
# else:
#     print("not strong")

# Python Program to Calculate the Power
# def power(base, exponent):
#     result = 1
#     for i in range(exponent):
#         result *= base
#     return result

# base = 2
# exponent = 3
# result = power(base, exponent)
# print(result)

# armstrong
# n=153
# l=len(str(n))
# total=0
# while n>0:
#     digit=n%10
#     total+=digit**l
#     n=n//10

# if total==n:
#     print("armstrong")
# else:
#     print("not armstrong")