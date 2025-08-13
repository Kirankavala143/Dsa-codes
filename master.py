# arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k=4
# n=len(arr)
# left =0
# ans =0
# temp =0
# for right in range(n):
#     temp+=arr[right]

#     if right - left == k:
#         temp-=arr[left]
#         left+=1
#     if right - left +1 ==k:
#         ans=max(ans,temp)
# print(ans)


# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 2
# n=len(arr)
# left =0
# ans =0
# temp =0
# for right in range(n):
#     if right <0:
#         if right - left == k:
#             temp-=arr[left]
#             left+=1
#         if right - left +1 ==k:
#             print(temp)

# arr = [2, 3, 1, 2, 4, 3]
# target = 7
# temp=0
# ans=float('inf')
# n=len(arr)
# left=0
# for right in range(n):
#     temp+=arr[right]

#     while temp>=target:
#         ans=min(ans,right-left+1)
#         temp-=arr[left]
#         left+=1
# print(ans if ans !=float('inf')else 0)

# s = "abcabcbb"
# n=len(s)
# temp=set()
# ans=0
# left=0
# for right in range(n):
#     while s[right] in temp:
#         temp.remove(s[left])
#         left+=1
#     temp.add(s[right])
#     ans=max(ans,right-left+1)
# print(ans)



# arr = [1, 2, 3, 4, 5]
# k = 2
# n=len(arr)
# temp=0
# ans=0
# left=0
# for right in range(n):
#     if arr[right] %2 ==1:
#         temp+=1
#     while temp>k:
#         if arr[left]%2==1:
#             temp-=1
#         left+=1
#     ans=max(ans,right-left+1)
# print(ans)


# fruits = [1, 2, 1, 2, 3]
# k=2
# n=len(fruits)
# left=0
# temp=0
# ans=0
# for right in range(n):
#     while 