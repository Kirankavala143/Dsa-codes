# s=[5,9,1,8,7]
# n=len(s)
# for i in range(n):
#     for j in range(i+1,n):
#         if s[i]<s[j]:
#             s[i],s[j]=s[j],s[i]
# print(s)

s=[5,9,1,8,7]
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for k in range(i,j+1):
            temp.append(s[k])
            tsum+=s[k]
        if len(temp) == 3:
            print(temp,tsum)
            ans=max(ans,tsum)
print(ans)



        

