# print even words in a Dictionary
# n=int(input())
# words=list(map(str,input().split()))[:n]
# d={i:len(i) for i in words}
# x=[]
# for i,j in d.items():
#     if j%2==0:
#         x.append(f"{i}={j}")
# print("{"+", ".join(x)+"}")
        
# container with most water
# n=int(input())
# height=list(map(int,input().split()))
# left,right=0,n-1
# max_area=0
# while left<right:
#     width=right-left
#     ht=min(height[left],height[right])
#     area=width*ht
#     max_area=max(max_area,area)

#     if height[left]<height[right]:
#         left+=1
#     else:
#         right-=1
# print(max_area)
# 1,8,6,2,5,4,8,3,7


m = input()   # taking input for the start day (e.g., "mon", "tue", etc.)
n = int(input())  # taking input for number of days in the month

w = ["mon","tue","wed","thu","fri","sat","sun"]  # list of weekdays
x = w.index(m) + 1   # find the position of the starting day in the list and add 1
print((n + x) // 7)  # calculate and print result
