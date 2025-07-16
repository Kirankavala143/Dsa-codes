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

# bubble sort  (compare beside numbers)
# arr=[3,24,7,87,5,9,78]
# n=len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j+1]<arr[j]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

# insertion sort(insert elements at right position)
# arr=[3,24,7,87,5,9,78]
# n=len(arr)
# for i in range(1,n):
#     key=arr[i]
#     j=i-1
#     while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)

# merge sort(merging elements)
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2         # Step 1: Find the middle
#         left = arr[:mid]            # Step 2: Divide into left half
#         right = arr[mid:]           # Step 3: Divide into right half

#         merge_sort(left)            # Step 4: Sort the left half
#         merge_sort(right)           # Step 5: Sort the right half

#         i = j = k = 0

#         # Step 6: Merge the two sorted halves
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         # Step 7: Check for remaining elements
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1

# # Example usage
# arr = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(arr)
# print("Sorted array:", arr)

# # quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)