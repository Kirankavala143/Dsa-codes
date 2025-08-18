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


# n = int(input())  # number of tuples
# digits = set()    # to store unique digits

# for _ in range(n):
#     a, b = map(int, input().split())
    
#     # Convert both numbers to strings and iterate over each digit
#     for num in (a, b):
#         for ch in str(num):
#             digits.add(int(ch))  # add digit to the set

# # Sort the digits and print them
# sorted_digits = sorted(digits)
# print("The extracted digits :", *sorted_digits)

# sum of all values in dictionary by taking user input

# n = int(input())
# d = {}
# for i in range(n):
#     key, values = input().split()
#     d[key] = int(values) 
# print(sum(d.values()))

# sort keys in ascending order print values too

# n = int(input())
# d = {}
# for i in range(n):
#     key, values = input().split()
#     d[key] = int(values) 
# for name in sorted(d.keys()):
#     print(f"{name}: {d[name]}")

# n = int(input())
# a = input()
# b = input()

# result = ""
# for i in range(n):
#     if a[i] == b[i]:
#         result += "0"
#     else:
#         result += "1"

# print(result)

# print 1 letter of the words
# a=input().split()
# for i in a:
#     print(i[0])

# neon number
# n = int(input())
# square = n ** 2
# total = 0
# for digit in str(square):
#     total += int(digit)

# if total == n:
#     print("Neon Number")
# else:
#     print("Not Neon Number")

# perfect number
# n = int(input())
# total = 0
# for i in range(1, n):
#     if n % i == 0:
#         total += i
# if total == n:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")



# sum of digits
# n = int(input())
# total = 0
# for i in str(n):
#     total += 1
# print(total)



# MATRICS

# def  transpose_matrix(matrix, m, n):
#     lists = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             row.append(matrix[j][i])
#         lists.append(row) 
#     return lists 


# def convert_str_to_int(list_a):
#     new_list = []
#     for i in list_a:
#         i = int(i)
#         new_list.append(i)
#     return new_list  

# m = int(input())
# n = int(input())
# new_list = []
# for i in range(n):
#     list_a = input().split()
#     list_b = convert_str_to_int(list_a)
#     new_list.append(list_b)

# result = transpose_matrix(new_list, m,n)
# for i in result:
#     print(i)

li=[5,9,1,8,7]
n=len(li)
ans=float('-inf')
left=0
temp=0
for r in range(n):
    temp+=li[r]

    if (r-left ==3):
        temp-=li[left]
        left+=1

    if (r-left+1 ==3):
        ans=max(ans,temp)

print(ans)

s="xyzzaz"
# n=len(s)
# for i in range(n)


# reverse a array
l = [1, 2, 3, 4, 5]
# l.reverse()  # In-place reversal
print(l[::-1])

# generate 2,4,6,8,10 
# -2,-4,-6,-8,-10
l = [2 * i for i in range(1, 6)]  # Generates [2, 4, 6, 8, 10]
print(l)
l = [-2 * i for i in range(1, 6)]  # Generates [-2, -4, -6, -8, -10]
print(l)

# determine whether n is power of 3 or not
# n = int(input("Enter a number: "))
# is_power_of_three = False
# while n > 1:
#     if n % 3 != 0:
#         break
#     n //= 3
# if n == 1:
#     is_power_of_three = True
# print(is_power_of_three)

# another way 
# import math
# n=int(input("Enter a number: "))
# a=pow(3,3)
# print(a)
# if n==a:
#     print("true")
# else:
#     print("false")


# n=int(input("Enter a number: "))
# while n > 1:
#     if n % 3 != 0:
#         break
#     n //= 3
# if n == 1:
#     print("true")
# else:
#     print("false")

# print("Enter a number:")
# n = int(input())  

# if n % 3 == 0:
#     print("true")
# else:
#     print("false")

def find_intersection(arr1, arr2):
    intersection = []
    set_arr2 = set(arr2)  # Convert arr2 to a set for O(1) lookups
    for num in arr1:
        if num in set_arr2:
            intersection.append(num)
    return intersection 
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
result = find_intersection(arr1, arr2)
print(result)

find art
