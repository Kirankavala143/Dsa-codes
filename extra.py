# # li=[2,34,6,3,2,3,4,3,2,32]
# li=["hello","hi","hello","hi","hello"]
# s={}
# for i in li:
#     if i not in s:
#         s[i]=1
#     else:
#         s[i]+=1
# print(s)

# leet code 169
# li=[2,2,1,1,1,2,2]
# s={}
# for i in li:
#     if i not in s:
#         s[i]=1
#     else:
#         s[i]+=1
#     print(s)
# ans=-1
# temp=len(li)//2
# for i in s:
#     if s[i]> temp:
#         ans=i
# print(ans)


# l=[2,2,1,1,1,2,2]
# l.sort()
# temp=len(l)//2
# print(l[temp])

# 1512
# def numIdenticalPairs(self, nums: List[int]) -> int:
#     n=len(nums)
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] == nums[j]:
#                 count+=1
#     return count

li=[4,4,4,4,4]
n=len(li)
count=0
k=n-1
count=k*(k-1)//2
print(count)
# for i in range(n):
#     count+=i
# print(count)

# optimal solution
# nums=[1,2,3,1,1,3]
# dici={}
# for i in nums:
#     if i in dici:
#         dici[i]+=1
#     else:
#         dici[i]=1
# ans=0
# for i in dici:
#     n=dici[i]
#     temp=n*(n-1)//2
#     ans+=temp
# return ans

# def numIdenticalPairs(self, nums: List[int]) -> int:
#     n=len(nums)
#     count=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] == nums[j]:
#                 count+=1
#     return count

jewels="aA"
stones="aAAbbbb"
count=0
for i in jewels:
    if i in stones:
        count+=stones.count(i)
print(count)