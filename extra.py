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

# jewels
jewels="aA"
stones="aAAbbbb"
# count=0
# for i in stones:
#     if i in jewels:
#         count+=1
# print(count)

# dic={}
# for i in stones:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# ans=0
# for i in range(len(jewels)):
#     ch=jewels[i]
#     if ch in dic:
#         ans+=dic[ch]
#         print(ans)

# question1 
    # def processStr(self, s: str) -> str:
    #     a=[]
    #     for i in s:
    #         if i.islower():
    #             a.append(i)
    #         elif i=='*':
    #             if a:
    #                 a.pop()
    #             break
    #         elif i=='#':
    #             a+=a[:]
    #         elif i=='%':
    #             a.reverse()
    #     return ''.join(a)

    # 3
    # class Solution:
    # def processStr(self, s: str, k: int) -> str:
    #     a=[]
    #     for i in s:
    #         if i.islower():
    #             a.append(i)
    #         elif i=='*':
    #             if a:
    #                 a.pop()
                
    #         elif i=='#':
    #             a+=a[:]
    #         elif i=='%':
    #             a.reverse()
    #     res=''.join(a)
    #     if 1 <= k <= len(res):
    #         # If k is within the valid range, return the character at index k-1.
    #         return res[k]
    #     else:
    #         # If k is out of bounds (e.g., k=0, k < 1, or k > len(res)), return '.'.
    #         return '.'
