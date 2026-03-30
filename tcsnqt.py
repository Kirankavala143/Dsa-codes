# to find prime numbers
# n = 47
# for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# reverse a string
#  a="kiran"
# print(a[::-1])

# Reverse a string using recursion
# def reverse_string(s):
#     if len(s) == 0:
#         return ""
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("hello"))

# factorial
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#palindrome 
# a="madam"
# if a[::-1]==a:
#     print("pali")
# else:
#     print("nonpali")

# largest ele
# a=[1,2,4,35,6]
# l=a[0]
# for i in a:
#     if i>l:
#         l=i
# print(l)

# # Count frequency of characters
# a="kirankumar"
# c={}
# for i in a:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1

# print(c)

# sum of digits
# n = int(input())
# total = 0
# for i in str(n):
#     total += int(i)
# print(total)

# Check Armstrong number
num=int(input("enter a number:"))
orginal_num=num
length=len(str(num))
sum_of_powers=0
while (num>0): #15
    digit=num%10 # %= remainder=3,5
    sum_of_powers+=digit**length 
    num=num//10
if sum_of_powers==orginal_num:  
    print("armstrong number")       
else:       
    print("not an armstrong number")


