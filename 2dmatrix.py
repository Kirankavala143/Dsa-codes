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