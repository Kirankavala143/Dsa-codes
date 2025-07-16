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