# find occurence of an element
# a=[2,4,6,4,4,4,8]
# x=6
# count=0
# for i in range(len(a)):
#     if a[i]==x:
#         count+=1
# print(count)

# Count frequency of each element in the array

def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
frequency = count_frequency(arr)
print(frequency)
