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

# optimal solution
nums=[0,1,0,3,12]
pos = 0  # position to place the next non-zero
for i in range(len(nums)):
    if nums[i] != 0:
        nums[pos] = nums[i]
        pos += 1    
for i in range(pos, len(nums)):
    nums[i] = 0
print(nums)