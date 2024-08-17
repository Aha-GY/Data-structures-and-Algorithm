rows, cols = map(int,input().split())
matrix = []
for i in range(rows):
    temp = list(map(int,list(input())))
    matrix.append(temp)
color = 11
a =0

for i in range(len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[i][j-1] != matrix[i][j]:
            print("NO")
            a =1
            break
        elif color != 11 and color == matrix[i][j]:
            print("NO")
            a = 1
            break
    else:
        color = matrix[i][0]
    if a == 1:
        break
    
else:
    print("YES")