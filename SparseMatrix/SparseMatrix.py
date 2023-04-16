sparseMatrix = [[0,0,3,0,4], [0,0,5,7,0], [0,0,0,0,0], [0,2,6,0,0]]
size = 0
m = len(sparseMatrix)
n = len(sparseMatrix[0])
# print(len(sparseMatrix[0]))

for i in range(m):
    for j in range(n):
        if sparseMatrix[i][j] != 0:
            size += 1

# print(size)

compacrMatrix = [[0 for i in range(size)] for j in range(3)]

k = 0
for i in range(m):
    for j in range(n):
        if sparseMatrix[i][j] != 0:
            compacrMatrix[0][k] = i
            compacrMatrix[1][k] = j
            compacrMatrix[2][k] = sparseMatrix[i][j]
            k += 1

for i in compacrMatrix:
    print(i)