# count=1
# while count <=5:
#     print("hello",count)
#     count+=1
# print(count)
# nums=[1,4,5,6,8,9,23,35,57,78]
# idx=0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1
# n=5
# sum=0
# i=0
# while i <=5:
#     sum+=i
#     i+=1
# print(sum)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# def sum(l):
#     return l
# l=[1,2,3,4,5]
# print(sum(l))
# def fact(n):
#     if n==0:
#         return 0
#     else:
#         return fact(n-1) + n
# sum=fact(5)
# print(sum)

# f=open("ss.txt","w")
# data=f.read()
# print(data)

# print("hiss")
# cot=0
# while cot<3:
#     cot+=1
#     print("hi")
# else:
#     print("hello")

#code here
# def fun(*args):
#     return sum(args)
# print(fun(1,2,3,4,5,6))

# def fun(**kwargs):
#     return kwargs

# print(fun(a=1,b=2,c=3,d=4))

n=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print(n(0))
print(n(-5))
print(n(5))

# li=[lambda  x,n=n :x*n for n in range(1,6)]
# for i in li:
#     print(i(1))

a=lambda x,y:(x+y,x*y)
print(a(2,3))

li=filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9])
print(list(li))

a=[1,2,3,4,5,6,7,8,9]

def fun(x):
    return x*2

res=list(map(fun,a))
print(res)

l=[2,67,3,3,2,3,5,7,9,9,6,9]
b=list(dict.fromkeys(l))
print(b)

n=int(input("enter a number:"))
a,b=0,1
for i in range(0,n+1):
    print(a)
    a,b=b,a+b

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

    