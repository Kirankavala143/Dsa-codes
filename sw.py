# s=[5,9,1,8,7]
# n=len(s)
# for i in range(n):
#     for j in range(i+1,n):
#         if s[i]<s[j]:
#             s[i],s[j]=s[j],s[i]
# print(s)

# s=[5,9,1,8,7]
# n=len(s)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         temp=[]
#         tsum=0
#         for k in range(i,j+1):
#             temp.append(s[k])
#             tsum+=s[k]
#         if len(temp) == 3:
#             print(temp,tsum)
#             ans=max(ans,tsum)
# print(ans)

# s=[5,9,1,8,7]
# n=len(s)
# l=0
# temp=0
# for r in range(n):
#     temp+=s[r]
 
#     if (r-l==3):
#         temp-=s[l]
#         l+=1
    
#     if (r-l+1 ==3):
#         print(temp)
    
# s=[5,9,1,8,7]
# n=len(s)
# temp=0
# l=0
# k=3
# ans=0
# for r in range(n):
#     temp+=s[r]
#     if (r-l== k):  #move l to front and decrement the lastelement 
#         temp-=s[l]
#         l+=1
#     if (r-l+1 ==k): # 
#         ans=max(ans,temp)
# print(ans)
    
s = [5, 9, 1, 8, 7]
n = len(s)
l = 0
window_sum = 0

for r in range(n):
    window_sum += s[r]

    if (r - l + 1 == 3):  # when window size is 3
        print(window_sum)
        window_sum -= s[l]  # remove leftmost
        l += 1

# sort dictionary by keys
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items()))

# input first line number next line inputs

# sort dictionary by values
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

# find max and min in a set

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



        

