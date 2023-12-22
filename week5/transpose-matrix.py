class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        column = len(matrix[0])
        row = len(matrix)
        ans ,temp=[],[]
        j =0
        
        for i in range(column):
            while j<(row):
                temp.append(0)
                j+=1
            ans.append(temp.copy())
        for i in range(len(matrix[0])):
            n=0
            while n <len(matrix):
                ans[i][n] = matrix[n][i]
                n+=1
        return ans
    
