
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == target):
                return True


matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
    ]
target = 3

print(searchMatrix(matrix,target))