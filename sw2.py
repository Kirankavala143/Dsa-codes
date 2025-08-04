l=[5,9,1,8,7]
n=len(l)
for i in range(n):
    for j in range(i,n):
        temp=[]
    for k in range(i,j+1):
        temp.append(l[k])
        print(temp)