# reverse an array
a=[1,2,3,4,5]
a.reverse()
print(a)

# another way to reverse an array
a=[1,2,3,4,5]
n=len(a)
for i in range(n//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
print(a)

# another way to reverse an array using slicing
a=[1,2,3,4,5]
a=a[::-1]

# check if array is sorted or not
a=[1,2,3,4,5]
is_sorted=True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        is_sorted=False
        break
print(is_sorted)

# another way to check if array is sorted or not
a=[1,2,3,4,5]
print(a==sorted(a))

# count frequency of each element in an array
a=[1,2,3,4,5,1,2,3,4,5]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

# another way to count frequency of each element in an array using collections module
from collections import Counter 
a=[1,2,3,4,5,1,2,3,4,5]
freq=Counter(a)
print(freq)
#
# another way to count frequency of each element in an array using set
# a=[1,2,3,4,5,1,1,1,1,1]
# for i in set(a):
#     print(i,a.count(i))


# Twp sum problem
# l=[1,2,3,4,5]
# target=5
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print(i,j)
   
l=[0,1,2,0,3,4,5,0,0]
for i in l:
    if l[i]==0:
        l.remove(0)
        l.append(0)
print(l)


# find the missing number in an array of n-1 numbers
l=[1,2,4,5]
n=len(l)+1
total=n*(n+1)//2
sum_of_l=sum(l)
print(total-sum_of_l)

# another way to find the missing number in an array of n-1 numbers
l=[1,2,4,5]
n=len(l)+1
for i in range(1,n+1):
    if i not in l:
        print(i)
        break


