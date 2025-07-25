s="abc"
n=len(s)
ans=[]
for i in range(n+1):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(s[k])
        ans.append(temp)
print(ans)

