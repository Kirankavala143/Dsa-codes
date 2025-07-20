# a=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[i][j])

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# a=[[1,2,3,4],[5,6,7,8]]
r=len(a)
c=len(a[0])
# for i in range(r):
for j in range(c):
    print(a[0][j])






# search a element in 2d matrix return true or false

# def search(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == target:
#                 return True
#     return False

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# target = 5
# print(search(matrix, target))

# search a element in 2d matrix return its position

def search(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return None

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    
target = 9
print(search(matrix, target))