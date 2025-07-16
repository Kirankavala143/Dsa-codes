# linear search
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1   

# arr = [1, 2, 3, 4, 5]
# target = 3
# print(linear_search(arr, target))

# selection sort (select minimum and place front)
# arr=[3,24,7,87,5,9,78]
# n=len(arr)
# for i in range(n-1):
#     min_index=i
#     for j in range(i+1,n):
#         if arr[j]<arr[min_index]:
#             min_index=j
#     arr[i],arr[min_index]=arr[min_index],arr[i]
# print(arr)

# another way


arr=[4,32,3,34,46,54,12,45]
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)

