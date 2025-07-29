# s=[5,9,1,8,7]
# n=len(s)
# for i in range(n):
#     for j in range(i+1,n):
#         if s[i]<s[j]:
#             s[i],s[j]=s[j],s[i]
# print(s)

# s=[5,9,1,8,7]
# n=len(s)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         tsum=0
#         for k in range(i,j+1):
#             temp.append(s[k])
#             tsum+=s[k]
#         if len(temp) == 3:
#             print(temp,tsum)
#             ans=max(ans,tsum)
# print(ans)

# s=[5,9,1,8,7]
# n=len(s)
# l=0
# temp=0
# for r in range(n):
#     temp+=s[r]
 
#     if (r-l==3):
#         temp-=s[l]
#         l+=1
    
#     if (r-l+1 ==3):
#         print(temp)
    
# s=[5,9,1,8,7]
# n=len(s)
# temp=0
# l=0
# k=3
# ans=0
# for r in range(n):
#     temp+=s[r]
#     if (r-l== k):  #move l to front and decrement the lastelement 
#         temp-=s[l]
#         l+=1
#     if (r-l+1 ==k): # 
#         ans=max(ans,temp)
# print(ans)
    
s = [5, 9, 1, 8, 7]
n = len(s)
l = 0
window_sum = 0

for r in range(n):
    window_sum += s[r]

    if (r - l + 1 == 3):  # when window size is 3
        print(window_sum)
        window_sum -= s[l]  # remove leftmost
        l += 1
# 1876
# s="xyzzaz"
# n=len(s)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         tsum=0
#         for k in range(i,j+1):
#             temp.append(s[k])
#             a=set(temp)
#         if len(a)==3 and len(temp)==3:
#             ans+=1
# print(ans)

# optimize    
# s="xyzzaz"
# n=len(s)
# ans=0
# dic={}
# l=0
# k=3
# for r in range(n):
#     if s[r] in dic:
#         dic[s[r]] +=1
#     else:
#         dic[s[r]] = 1
#     if r-l ==3:
#         dic[s[l]] -=1
#     if dic[s[l]]==0:
#         dic.pop(s[l])
#         l+=1
#     if len(dic)==3:
#         ans+=1
# print(ans)

# 1984
# l=[9,4,1,7]
# l.sort()
# n=len(l)
# k=3
# ans=float('inf')
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for m in range(i,j+1):
#             temp.append(l[m])
#         if len(temp) == k:
#             last=temp[2] 
#             first=temp[0]
#             ans=min(ans,last-first)
# print(ans)

# OPTIMAL SLIDING WINDOW
# 1.VARAIBLE INCREMENT    
# 2.L INCREMENT
# 3.UPDATE ANS    

nums=[3,4,8,1,5]
nums.sort()
n=len(nums)
k=3
l=0
ans=float('inf')
for r in range(n):

    if (r-l==k): #array elements = 3 , increment
        l+=1
    if (r-l+1 == k): #len size =k

        ans=min(ans,nums[r]-nums[l])
print(ans)


# 561
# l=[6,2,6,5,1,2]
# l.sort()
# n=len(l)
# ans=0
# for i in range(0,n,2):
#     ans+=l[i]
# print(ans)

# 2144
l=[1,2,3]
l.sort(reverse=True)
n=len(l)
ans=0
# took=0
for i in range(n):
#     if took==2:
#         took=0
#     else:
#         ans+=l[i]
#         took+=1
# print(ans)
    if i%3!=2:
        ans+=l[i]
print(ans)

