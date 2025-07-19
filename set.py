# SET -O(N), NO DUPLICATES
# s=set()
# s.add(5)
# s.add(3)
# s.add(5)
# s.remove(5)
# s.add(6)
# print(s)

# if 5 in s:
#     print("5 is present")
# else:
#     print("5 is not present")
# for i in s:
#     print(i)

# # 645 
# a=[1,2,2,4]
# seen=set()
# missing=-1
# duplicate=-1
# for num in a:
#     if num in seen:
#         duplicate = num
#     else:
#         seen.add(num)
# for i in range(len(a)+1):
#     if i not in a:
#         missing=i
# print(missing)
# print(duplicate)


n=[1,2,2,4]
n=len(n)
for i in range(n):
    for j in range(i,n):
        print(i,j)



# generate sub arrays
# def generate_subarrays(arr):
#     subarrays = []
#     for i in range(len(arr) + 1):
#         for j in range(i + 1, len(arr) + 1):
#             subarrays.append(arr[i:j])
#     return subarrays

# arr = [1, 2, 3, 4, 5]
# subarrays = generate_subarrays(arr)
# print(subarrays)