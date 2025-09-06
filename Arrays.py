# largest element in an array
# arr = [1, 2, 3, 4, 5]
# print(max(arr))
# def largest_element(arr):
#     if not arr:
#         return None  # Handle empty array case
#     largest = arr[0]
#     for num in arr:
#         if num > largest:
#             largest = num
#     return largest
# arr = [1, 2, 3, 4, 5]
# print(largest_element(arr))

# a=[1, 2, 3, 4, 5]
# largest = a[0]
# for i in range(len(a)):
#     if a[i] >largest:
#         largest=a[i]
# print(largest)

# largest and second largest element in an array
# a=[1,2,3,4,5,7,7]
# largest=a[0]
# second_largest=a[0]
# for i in range(len(a)):
#     if a[i] > largest:
#         second_largest = largest
#         largest = a[i]
#     elif a[i] >second_largest and a[i]  !=largest:
#         second_largest = a[i]
# print("Largest element is:", largest)
# print("Second largest element is:", second_largest)

# largest and second largest element in an array using max
# a = [1, 2, 3, 4, 5, 7, 7]
# largest = max(a)
# second_largest = max(x for x in a if x != largest)
# print("Largest element is:", largest)
# print("Second largest element is:", second_largest)

# array sorted
# a=[2,6,4,1,3,5]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# another way to sort an array using sorted function
# a = [2, 6, 4, 1, 3, 5]
# sorted_a = sorted(a)  # Sort the array in ascending order
# print(sorted_a)

# # another way to sort an array using sorted function
# a = [2, 6, 4, 1, 3, 5]
# sorted_a = sorted(a, reverse=False)  # Sort the array in descending order
# print(sorted_a)       


# remove duplicates from an array
# b=[1,2,1,2,3,1,2,3,4]
# b = list(set(b))  # Convert to a set to remove duplicates, then back to a list
# print(b)

# another way to remove duplicates from an array
# b = [1, 2, 1, 2, 3, 1, 2, 3, 4]
# b = []
# for i in range(len(a)):   
#     if a[i] not in b:
#         b.append(a[i])
# print(b)

# another way to rotate an array left
# a = [1, 2, 3, 4, 5]
# n = 2
# rotated_a = a[n:] + a[:n]
# print(rotated_a)  

# another way to rotate an array right
# a = [1, 2, 3, 4, 5]
# n = 2
# rotated_a = a[-n:] + a[:-n]
# print(rotated_a)

# a= [1, 2, 3, 4, 5]
# k=3
# k= k % len(a) 
# print(k) # Handle cases where k is larger than the array length
# rotated_a = a[-k:] + a[:-k]
# print(rotated_a)

# n=[20,0,0,3,45,670,3,0,80,0,7,0,0,7,0]
# lis=[]
# for i in range(len(n)):
#     if n[i]==0:
#         lis.append(n[i])
#     else :
#         lis.insert(0, n[i])
# print(lis)  # This will print the list of zeros found in the array

n = [20, 0, 0, 3, 45, 670, 3, 0, 80, 0, 7, 0, 0, 7, 0]
lis = []

# First add non-zero elements
for x in n:
    if x != 0:
        lis.append(x)
# Then add zeros
zero_count = n.count(0)
lis.extend([0] * zero_count)
print(lis)

# optimal solutionc
nums=[0,1,0,3,12]
pos = 0  # position to place the next non-zero
for i in range(len(nums)):
    if nums[i] != 0:
        nums[pos] = nums[i]
        pos += 1    
for i in range(pos, len(nums)):
    nums[i] = 0
print(nums)

# union
def find_union(arr1,arr2):
    s=set()
    union=[]
    for i in arr1:
        s.add(i)
    for i in arr2:
        s.add(i)
    for i in s:
        union.append(i)
    return union

arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
print(find_union(arr1,arr2))

#intersection
def find_intersection(arr1,arr2):
    s=set()
    intersection=[]
    for i in arr1:
        s.add(i)
    for i in arr2:
        if i in s:
            intersection.append(i)
    return intersection

arr1=[1,2,3,3,4,5]
arr2=[3,4,5,6,7]
print(find_intersection(arr1,arr2))


# find the missing number in a array
# def find_missing(arr):
#     for i in range(1, len(arr) + 1):
#         if i not in arr:
#             return i
# # arr = [1, 2, 3,4,6,9,7,5,8,10]
# arr=[0,1]
# print(find_missing(arr))

# summation
def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1, 2, 3, 5]
print(find_missing_number(arr))


# Find the number that appears once, and the other numbers twice
def find_single_number(arr):
    for i, num in enumerate(arr):
        if arr.count(num) == 1:
            return num

arr = [1,1,2, 2, 3, 4, 4, 5, 5]
print(find_single_number(arr))

# another way to find the number that appears once, and the other numbers twice
def find_single_number(arr):
    a={}
    for i in arr:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    for i in a:
        if a[i]==1:
            return i

arr = [1,1,2, 2, 3, 4, 4, 5, 5]
print(find_single_number(arr))

# Sort an array of 0's 1's & 2's

# def sort_012(arr):
#     low = 0
#     mid = 0
#     high = len(arr) - 1

#     while mid <= high:
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             low += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid], arr[high] = arr[high], arr[mid]
#             high -= 1
#     return arr

# arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# print(sort_012(arr))

# majority element in an array (Find the Majority Element that occurs more than N/2 times)
# def majority(a):
#     count={}
#     for i in a:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     for i in count:
#         if count[i] > len(a)//2:
#             return i

# a=[3,3,4,2,4,4,2,4,4]
# print(majority(a))


def kadane(arr):
    max_sum = float('-inf')  # Initialize to negative infinity
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        # If current_sum goes negative, reset it
        if current_sum < 0:
            current_sum = 0

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", kadane(arr))







# Longest Subarray with sum K
# def longest_subarray(arr, K):
#     max_len = 0
#     n = len(arr)

#     for i in range(n):
#         total = 0
#         for j in range(i, n):
#             total += arr[j]
#             if total == K:
#                 max_len = max(max_len, j - i + 1)

#     return max_len

# arr = [2, 1, 5, 2, 3, 2]
# k = 5
# print(longest_subarray(arr, k))



