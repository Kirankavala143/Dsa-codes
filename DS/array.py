# find occurence of an element
# a=[2,4,6,4,4,4,8]
# x=6
# count=0
# for i in range(len(a)):
#     if a[i]==x:
#         count+=1
# print(count)

# Count frequency of each element in the array
# def count_frequency(arr):
#     frequency = {}
#     for num in arr:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
#     return frequency
# arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# frequency = count_frequency(arr)
# print(frequency)

# Find the highest/lowest frequency element
# a=[2,4,6,4,4,4,8]
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(max(d,key=d.get),d)
# print(min(d,key=d.get))

# second largest number in an array
# a=[1,2,3,4,5,1,2,3,4,5,5,5,9]
# largest=a[0]
# second_largest=a[0]
# for i in a:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif i>second_largest and i!=largest:
#         second_largest=i 
# print(largest,second_largest)

# sort an array
# a=[2,6,4,1,3,5]
# print(sorted(a,reverse=False)) #sort the array in ascending order
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

# dupliate elements in an array
# a=[1,2,3,4,5,1,2,3,4,5]
# s=[]
# for i in a:
#     if i not in s:
#         s.append(i)
# print(s)

# rotate an array
# a= [1, 2, 3, 4, 5]
# k=2
# k= k % len(a) 
# print(k) # Handle cases where k is larger than the array length
# right_rotated_a = a[-k:] + a[:-k]
# left_rotated_a = a[k:]+ a[:k]
# print(right_rotated_a)
# print(left_rotated_a)


# move all zeros to end of array
# a=[2,5,67,0,3,0,5,0,4,0]
# l=[]
# for i in a:
#     if i!=0:
#         l.append(i)
# for i in range(a.count(0)):
#     l.append(0)
# print(l)

# another way to move all zeros to end of array
# a = [2, 5, 67, 0, 3, 0, 5, 0, 4, 0]
# non_zero_elements = [i for i in a if i != 0]
# zero_elements = [i for i in a if i == 0]
# a = non_zero_elements + zero_elements
# print(a)

# a=[2,5,67,0,3,0,5,0,4,0]
# l=[]
# for i in range(len(a)):
#     if a[i]==0:
#         l.append(a[i])
#     if a[i]!=0:
#         l.insert(0,a[i])
# print(l)


# union of two arrays
# def union_of_arrays(arr1, arr2):
#     return list(set(arr1) | set(arr2))

# intersection of two arrays
# def intersection_of_arrays(arr1, arr2):
#     return list(set(arr1) & set(arr2))
# # example usage
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [4, 5, 6, 7, 8]
# print("Union:", union_of_arrays(arr1, arr2))
# print("Intersection:", intersection_of_arrays(arr1, arr2))


# find the missing number in an array
# def find_missing(arr):
#     for i in range(1, len(arr) + 1):
#         if i not in arr:
#             return i

# # arr = [1, 2, 3,4,6,9,7,8,10]
# arr=[0,2]
# print(find_missing(arr))

# def find_missing_number(arr):
#     n=len(arr)+1
#     total_sum=(n*(n+1))//2
#     actual_sum=sum(arr)
#     return total_sum-actual_sum

# arr=[1,2,3,5]
# print(find_missing_number(arr))

# kth smallest and kth largest element in an array
# k=3
# n=4
# a=[1,2,5,4]
# a.sort()
# print(a)
# print(a[k-1],a[n-k])

k=3
a=[1,2,5,4]
a.sort()
n = len(a)   # auto calculate length
print(a)
print(a[k-1], a[n-k])

























































































































































