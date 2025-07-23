# for i in range(3):
#     print(i,"kiran wants to grow a tree")
#     for j in range(2):
#         print("tree",j)
#     print(i,"Exited")

# 2114
# s = ["one problem a day", "hi this is kiran kumar", "hello welcome"]
# max=0
# for sentence in s:
#     c=len(sentence.split())
#     if max<c:
#         max=c
# print(max)

# s=["hi", "This is kiram from csm","to get a job"]
# ans=0
# for i in range(len(s)):
#     a=s[i]
#     # print(a)
#     temp=1
#     for j in range(len(a)):
#         ch=a[j]
#         if ch == " ":
#             temp=temp+1
#     ans=max(ans,temp)
# print(ans)


# for i in range(1, 3):
#     for j in range(1, 3):
#         # print(i, j)
#         for k in range(1, 3):
#             print(i, j, k) 


# for i in range(1,9):
#     for j in range(i+1):
#         print(i,end=" ")
#     print()

# for i in range(3):
#     for j in range(1,4):
#         print("*",end="")
#     print()


# SUB ARRAY [1,33,56]  CONSIDER LINE
# [1], [1,33], [1,33,56], [33], [33,56], [56]
# SUB STRING "abc"
# SUB SEQUENCE [1,2,3]   NOT CONSIDER LINE ( FOLLOWS ORDER OF INDEX(CAN SKIP BETWEEN ELEMENT))



# li=[1,33,56]
# n=len(li)
# ans=[]
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(li[k])
#         ans.append(temp)
# print(ans)

# s="abc"
# n=len(s)
# ans=[]
# for i in range(n+1):
#     for j in range(i,n):
#         temp=[]
#         for k in range(i,j+1):
#             temp.append(s[k])
#         ans.append(temp)
# print(ans)

