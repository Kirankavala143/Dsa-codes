l=[1,2,3,4,5,6,7,8]
n=len(l)
ans=0 
left=0
count=0
k=2
for right in range(n):
    if l[right] %2 ==1:
        count+=1
    while count > k:
        if l[left] %2 ==1:
            count-=1
        left+=1
    ans=max(ans,right-left+1)
print(ans)        
