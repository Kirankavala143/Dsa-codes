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
cost=[6,5,7,9,2,2]
cost.sort()
# n=len(cost)
ans=0
took=0
for i in range(len(cost)-1,-1,-1):
    if took == 2:
        took = 0
    else:
        ans += cost[i-1]
        took += 1
print(ans)  
