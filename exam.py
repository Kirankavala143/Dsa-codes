# sort dictionary by keys
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items()))

# find max and min in a list
# n=int(input())
# l=list(map(int,input().split()))
# print(max(l))
# print(min(l))

# l = [1, 2, 3, 4, 5]
# max_val = max(l)
# min_val = min(l)

# square even numbers using list comprehension
# n=int(input())
# l=list(map(int,input().split()))
# even_squares = [x**2 for x in l if x % 2 == 0]
# print(*even_squares)


# find the range (max-min) using args:
# def range(*args):
#     return max(args) - min(args)

# l=list(map(int,input().split()))
# print(max(l)-min(l))


        

# print all posttive number from list
# n=int(input())
# l=list(map(int,input().split()))
# l=[x for x in l if x>0]
# print(*l)

# reverse a list
# n=int(input())
# l=list(map(int,input().split()))
# l.reverse()
# print(*l)

# another way
# n=int(input())
# l=list(map(int,input().split()))
# l=l[::-1]
# print(*l)

# count digits
# n=int(input())
# l=list(map(int,input().split()))
# count=0
# for i in l:
#     count+=1
# print(count)

# automorphic number:

# n= int(input())
# s = n ** 2
# if str(s).endswith(str(n)):
#     print("Automorphic")
# else:
#     print("Not Automorphic")

n=int(input())
l=list(map(int,input().split()))


