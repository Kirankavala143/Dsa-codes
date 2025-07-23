# min ,max positon value
# n = int(input())  # Number of elements
# l = list(map(int, input().split()))  # List of integers

# # Initialize max and min with the first element
# max_val = l[0]
# min_val = l[0]
# max_index = 0
# min_index = 0

# # Loop through the list to find max and min
# for i in range(1, n):
#     if l[i] > max_val:
#         max_val = l[i]
#         max_index = i
#     if l[i] < min_val:
#         min_val = l[i]
#         min_index = i

# print(max_index)
# print(min_index)

# a = input().lower()
# vowels = "aeiou"
# found = ""

# for i in a:
#     if i in vowels and i not in found:
#         found += i

# if len(found) == 5:
#     print("true")
# else:
#     print("false")

# a=list(map(str,input().split()))
# print("contents of list:",*a)
# print(len(a))



# Extract unique digits from tuple list

# n = int(input())
# digits = set()

# for _ in range(n):
#     a, b = input().split()
#     digits.update(a)
#     digits.update(b)

# # Filter only digits (in case of any non-digit input)
# unique_digits = sorted(set(filter(str.isdigit, digits)))

# print("The extracted digits :", ' '.join(unique_digits))


n = int(input())  # number of tuples
digits = set()    # to store unique digits

for _ in range(n):
    a, b = map(int, input().split())
    
    # Convert both numbers to strings and iterate over each digit
    for num in (a, b):
        for ch in str(num):
            digits.add(int(ch))  # add digit to the set

# Sort the digits and print them
sorted_digits = sorted(digits)
print("The extracted digits :", *sorted_digits)
