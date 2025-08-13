# # highest subarray sum of length 3
# l=[5,9,1,8,7]
# n=len(l)
# ans=0

# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         tsum=0
#         for k in range(i,j+1):
#             temp.append(l[k])
#             tsum+=l[k]
#         if len(temp) ==3:
#             ans=max(ans,tsum)
# print(ans)
            # print(temp, sum(temp))
#             ans=max(ans,sum(temp))
# print(ans)  
            

# l=[5,9,1,8,7]
# n=len(l)
# left=0
# k=3
# temp=0
# ans=0
# for right in range(n):
#     temp+=l[right]

#     if right-left ==k:  #index first
#         temp-=l[left]
#         left+=1
#     if right-left+1 == k:
#         ans=max(ans,temp)
# print(ans)  

# s="xyzzaz"
# n=len(s)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(s[k])
#             a=set(temp)
#     if len(temp) and len(a) == 3:
#         ans+=1
# print(ans)

# s="xyzzaz"
# n=len(s)
# left=0
# temp=[]
# ans=0
# dic={}
# for right in range(n):
#     if s[right] in dic:
#         dic[s[right]]+=1
#     else:
#         dic[s[right]]=1

#     if right-left ==3:
#         dic[s[left]]-=1
#         if dic[s[left]] == 0:
#             dic.pop(s[left])
#         left+=1
#     if len(dic) ==3:
#         ans+=1
# print(ans)

# l=[3,4,8,1,5]
# l.sort()
# n=len(l)
# k=3
# left=0
# ans=float('inf')
# for right in range(n):
#     if right-left == 3:
#         left+=1
#     if right-left+1 == 3:
#         ans=min(ans,l[right] - l[left])
# print(ans)


# 
# l=[10,1000,1,100]
# l.sort()
# ans=0
# for i in range(0,len(l),2):
#     ans+=l[i]
# print(ans)

# 2144
# cost=[6,5,7,9,2,2]
# cost.sort()
# # n=len(cost)
# ans=0
# took=0
# for i in range(len(cost)-1,-1,-1):
#     if took == 2:
#         took = 0
#     else:
#         ans += cost[i-1]
#         took += 1
# print(ans)  

# 1343
# l=[2,2,2,2,5,5,5,8]
# n=len(l)
# t=4
# k=3
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         tsum=0
#         for m in range(i,j+1):
#             temp.append(l[m])
#             tsum+=l[m]
#         if len(temp) == k:
#             avg= tsum/k
#             if avg >=t:
#                 ans+=1
# print(ans)            

# OPTIMAL
# l=[2,2,2,2,5,5,5,8]
# n=len(l)
# t=4
# k=3
# ans=0
# temp=0
# left=0
# for right in range(n):
#     temp+=l[right]
#     if right-left ==k:
#         temp-=l[left]
#         left+=1
#     if right-left+1 == k:
#         print(left, right, temp)
#         if temp/k >= t:
#             ans+=1
# print(ans)

# l=[9,3,4,8,1]
# n=len(l)
# k=3
# left=0
# ans=0
# temp=0
# for right in range(n):
#     temp+=l[right]

#     if right-left == k:
#         temp-=l[left]
#         left+=1
#     if right-left+1 == k:
#         ans=max(ans,temp)
# print(ans)
#   VARAIABLE SIZE SLIDING WINDOW

# l=[9,3,4,8,1]
# n=len(l)
# k=10
# left=0
# ans=0
# temp=0
# for right in range(n):
#     temp+=l[right]

#     while temp > k:
#         temp-=l[left]
#         left+=1
#     print(l[left:right+1],sum(l[left:right+1]))
#     ans=max(ans,right-left+1)
# print(ans)

# find max length os subarray with atmost k ones
# l=[0,1,3,1,1,6,7,1,0,1]
# n=len(l)
# left=0
# temp=0
# ans=0
# k=2
# for right in range(n):
#     if l[right] == 1:
#         temp+=1

#     while temp>k:
#         if l[left] == 1:
#             temp-=1
#         left+=1
#     print(l[left:right+1], sum(l[left:right+1]))
#     ans=max(ans,right-left+1)
# print(ans)

# # 1004
# l=[1,1,1,0,0,0,1,1,1,1,0]
# n=len(l)
# left=0
# temp=0
# ans=0
# k=2
# for right in range(n):
#     if l[right] == 0:
#         temp+=1

#     while temp>k:
#         if l[left] == 0:
#             temp-=1
#         left+=1
#     # print(l[left:right+1], sum(l[left:right+1]))
#     ans=max(ans,right-left+1)
# print(ans)

# optimize 
# l=[1,1,1,0,0,0,1,1,1,1,0]
# n=len(l)
# left=0

# ans=0
# count1=0
# count0=0
# k=2
# for right in range(n):
#     if l[right] ==0:
#         count0+=1
#     else:
#         count1+=1
#     while min(count0,count1) >k:
#         if l[left] ==0:
#             count0-=1
#         else:
#             count1-=1
#         left+=1
#     ans=max(ans,right-left+1)
# print(ans)
# print(l)


# 2024
# l="TTFF"
# n=len(l)
# left=0
# temp=0
# ans=0
# k=2
# countT=0
# countF=0
# for right in range(n):
#     if l[right] =='T':
#         countT+=1
#     else:
#         countF+=1
#     while min(countT,countF) > k:
#         if l[left] == 'T':
#             countT-=1
#         else:
#             countF-=1
#         left+=1
#     ans=max(ans,right-left+1)
# print(ans)

# 3
# s="abcbaa"
# n=len(s)
# a=set()
# l=0
# ans=0
# count=0
# for i in range(n):
#     ch=s[i]
#     if ch not in a:
#         a.add(ch)
#     else:
#         while ch in a:
#             a.remove(s[l])
#             l+=1
#         a.add(ch)
    
#     ans=max(ans,i-l+1)
# print(ans)
s="abcabcbb"
n=len(s)
left=0
temp=set()
ans=0
for right in range(n):
    while s[right] in temp:
        temp.remove(s[left])
        left+=1
    temp.add(s[right])
    ans=max(ans,right-left+1)
print(ans)   

# 904
# l=[1,2,3,2,2]
# n=len(l)
# ans=0
# k=2
# left=0
# dic={}
# for right in range(n):
#     val=l[right]
#     if val in dic:
#         dic[val]+=1
#     else:
#         dic[val]=1
#     while len(dic) > k:
#         ss=l[left]
#         dic[ss]-=1
#         if dic[ss] ==0:
#             dic.pop(ss)
#         left+=1
#     ans=max(ans,right-left+1)
# print(ans)


# 438
def findAnagrams(s, p):
    n = len(s)
    m = len(p)
    ans = []
    dic = {}
    for i in p:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1  
    left = 0
    for right in range(n):
        if s[right] in dic:
            dic[s[right]] -= 1
        else:
            dic[s[right]] = -1
        
        while dic[s[right]] < 0:
            dic[s[left]] += 1
            left += 1
        
        if right - left + 1 == m:
            ans.append(left)
    return ans  
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))

# 209 minimum size of subarray sum
# l=[2,3,1,2,4,3]
# n=len(l)
# ans=float('inf')
# left=0
# temp=0    
# k=7
# for right in range(n):
#     temp+=l[right]
#     while temp>=k:
#         ans=min(ans,right-left+1)
#         temp-=l[left]
#         left+=1
# print(ans)

# 1248 return length of longest subarray with atmost k odd numbers
def atMost(arr,k):
    n=len(l)
    ans=0 
    left=0
    temp=0
    for right in range(n):
        if l[right] %2 ==1:
            temp+=1
        while temp > k:
            if l[left] %2 ==1:
                temp-=1
            left+=1
        # ans=max(ans,right-left+1)
        # print(l[left:right+1],right)
        ans+=right-left+1
    return ans

l=[6,1,2,1]
k=2
a=atMost(l,k) - atMost(l,k-1)
print(a)


# 930
def atMost(l,k):
    if k<0:
        return 0
    l=[1,0,1,0,1]
    n=len(l)
    temp=0
    k=2
    left=0
    for right in range(n):
        if l[right] ==1:
            temp+=1
        while temp>k:
            if l[left] == 1:
                temp-=1
            left+=1
        ans+=right-left+1
    return ans
# return atMost(nums,goal) - atmost(nums,goal)
            

# 992
#     def atMost(l,k):
#        l=[1,2,1,2,3]
#         n=len(l)
#         left=0
#         temp=0
#         dic={}
#         ans=0
#         for right in range(n):
#             val=l[right]
#             if val in dic:
#                 dic[val]+=1
#             else:
#                 dic[val] = 1
#             while (len(dic)>k):
#                 ival=l[left]
#                 dic[ival]-=1
#                 if dic[ival] == 0:
#                     dici.pop(ival)
#                 left+=1
                
#             ans+=right+left-1
#     return ans
# ans=atMost(l,k)-atMost(l,k-1)
# return ans

