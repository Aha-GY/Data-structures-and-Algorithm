class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in range(len(matrix)):
            left =0
            right = len(matrix[0])-1
            while left < right:
                matrix[row][left],matrix[row][right] =  matrix[row][right], matrix[row][left]
                left +=1
                right -=1
       
        
        