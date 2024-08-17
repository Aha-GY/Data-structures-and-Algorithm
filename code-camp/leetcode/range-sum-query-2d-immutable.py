class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
       
        self.prefix = []
        for row in range(len(matrix)):
            temp =0
            sub_sum =[]
            for col in range(len(matrix[0])):
                temp += matrix[row][col]
                sub_sum.append(temp)
            sub_sum.append(0)
            self.prefix.append(sub_sum)
      
        for col in range(len(matrix[0])):
            temp =0
            for row in range(len(matrix)):
                temp += self.prefix[row][col]
                self.prefix[row][col] = temp
        self.prefix.append([0]*len(matrix[0]))
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1 -1][col1 -1]
