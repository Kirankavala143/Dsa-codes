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
a=[1,2,3,4,5,7,7]
largest=a[0]
second_largest=a[0]
for i in range(len(a)):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    elif a[i] >second_largest and a[i]  !=largest:
        second_largest = a[i]
print("Largest element is:", largest)
print("Second largest element is:", second_largest)
