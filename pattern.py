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


# # rhombus
# r=6
# c=3
# c1=r-1
# for i in range(r):
#     for j in range(c1-i):
#         print("*",end="")
#     for k in range(c):
#         print("-",end="")
#     print()

# r=5
# # c=5
# for i in range(r+1):
#     for j in range(c-i):
#         print(" ",end="")
#     for k in range(c):
#         print("-",end="")
#     print()

# print("reverse rhombus")

# r=5
# c=5
# for i in range(r):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(c):
#         print("-",end="")
#     print()


# r=5
# n=r-1
# for i in range(r):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for k in range(temp):
#         print("*",end="")
#     print()

# reverse
r=5
n=r-1
for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()

# r=5
# n=r-1
# for i in range(r):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*r-1-(2*i)):
#         print("*",end="")
#     print()

# ben 10 watch
# r=5
# n=r-1
# for i in range(r-1,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for k in range(temp):
#         print("*",end="")
#     print()
# for i in range(1,r):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for k in range(temp):
#         print("*",end="")
#     print()


# r=4
# n=r-1
# for i in range(r):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for j in range(temp):
#         if j==0 or j==i*2 or i==r-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# r=4
# n=r-1
# for i in range(r,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for j in range(temp):
#         if j==0 or j==i*2 or i==r-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# r=4
# n=r-1

# for i in range(r-1):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for j in range(temp):
#         if j==0 or j==i*2 or i==r-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# for i in range(r-1,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     temp=i*2+1
#     for j in range(temp):
#         if j==0 or j==i*2 :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# r=5
# n=r-1 
# for i in range(r):
#     for j in range(n-i):  
#         print(" ",end="")
#     temp=i*2+1
#     for j in range(temp):
#         if j==0 or j==temp-1 or i==r-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


#     for j in range(temp):
#         if j==0 or j==temp-1 or i==r-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()










