# highest subarray sum of length 3
# l=[5,9,1,8,7]
# n=len(l)
# ans=0
# k=3
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(l[k])
#         if len(temp) ==k:
#             print(temp, sum(temp))
#             ans=max(ans,sum(temp))
# print(ans)  
            

l=[5,9,1,8,7]
n=len(l)
left=0
k=3
temp=0
ans=0
for right in range(n):
    temp+=l[right]

    if right-left ==k:  #index first
        temp-=l[left]
        left+=1
    if right-left+1 == k:
        ans=max(ans,temp)
print(ans)  

