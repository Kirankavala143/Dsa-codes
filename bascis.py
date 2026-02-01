# sum of digits
# n = int(input())
# total = 0
# for i in str(n):
#     total += int(i)
# print(total)

# Sum of Digit of a Number using Recursion

def sum_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_digit(n // 10)

n = int(input())
print(sum_digit(n))

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

# fibnoacci number
# n=10
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# fibnocaai from 3 to 50
# n=50
# a,b=0,1
# while a<=50:
#     if a>=3:
#         print(a,end=" ")
#     a,b=b,a+b

# panagram
# s="the quick brown fox jumps over the lazy dog"
# s=s.lower()
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i not in s:
#         print("not panagram")
#         break
# else:
#     print("panagram")


# even index
# a="kiran"
# print(a[::2])
# l=len(a)
# for i in range(0,l,2):
#     print(a[i])

# # replace # with 6
# s="#1a2b3c4d5e6f7g8h9i0j"
# print(s.replace("#","6"))

# how many times a letter occurs in a string
# s="kiran"
# dic={}
# for i in s:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)

# sqrt of number i don't want decimal value
# n=8
# print(round(n**0.5))

# do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j,end=" ")
#     print()


