# xor on tuple
# nums=tuple(map(int,input().split()))
# res=nums[0]
# for n in nums[1:]:
#     res^=n 
# print(res)

# bitwise and
# a=tuple(map(int,input().split()))
# b=tuple(map(int,input().split()))
# print(tuple(a[i] & b[i] for i in range(len(a))))

# convert binary to decimal
# a=tuple(input().split())
# print(int(''.join(a),2))

# moduls
nums=tuple(map(int,input().split()))
res=nums[0]
for i in nums[1:]:
    res %=i 
print(res)