def searchMatrix(matrix, target):
    col = len(matrix[0])-1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][-1]<target:
                continue
            if j > col:
                return False
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                col = j

    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(searchMatrix(matrix, target))