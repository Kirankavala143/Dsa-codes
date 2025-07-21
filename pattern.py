# r=3
# c=7
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#         if j!=c-1:
#             print("-",end="")
#     print()

# r=5
# c=5
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#         if j!=c-1:
#             print("-",end="")
#     print()

# square matrix 
r=5
c=5
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
        # if j!=c-1:
        #     print(" ",end="")
    print()

# r=5
# c=20
# for i in range(r):
#     for j in range(c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

r=6
c=6
for i in range(r):
    for j in range(c-i):
        print("*",end="")
    print()