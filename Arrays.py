# largest element in an array
# arr = [1, 2, 3, 4, 5]
# print(max(arr))
def largest_element(arr):
    if not arr:
        return None  # Handle empty array case
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
arr = [1, 2, 3, 4, 5]
print(largest_element(arr))