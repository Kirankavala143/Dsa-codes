#  how many times a specific element appears in a array.
# def count_occurrences(arr, x):
#     count = 0
#     for num in arr:
#         if num == x:
#             count += 1
#     return count
# arr = [1, 2,1, 3, 4, 2, 5, 2]
# x = 1
# print(count_occurrences(arr, x))

# print(arr.count(x))

# Find the highest and lowest frequency element.
def find_highest_lowest_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    highest_freq = max(frequency.values())
    lowest_freq = min(frequency.values())

    highest_freq_elements = [num for num, freq in frequency.items() if freq == highest_freq]
    lowest_freq_elements = [num for num, freq in frequency.items() if freq == lowest_freq]

    return highest_freq_elements, lowest_freq_elements
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_highest_lowest_frequency(*arr))

def find_high_low_frequency(arr):
    freq = {}

    # Count frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find highest and lowest frequency element
    highest = max(freq, key=freq.get)
    lowest = min(freq, key=freq.get)

    print("Frequencies:", freq)
    print("Highest frequency element:", highest, "→ occurs", freq[highest], "times")
    print("Lowest frequency element:", lowest, "→ occurs", freq[lowest], "times")

# Example
arr = [4, 5, 6, 4, 3, 5, 4, 2, 6, 6, 6, 3]
find_high_low_frequency(arr)
