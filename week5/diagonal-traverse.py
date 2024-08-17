class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        diagonal = defaultdict(list)
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                diagonal[row + column].append(mat[row][column])
        output =[]
        for key,val in diagonal.items():
            if key%2 ==0:
                val =val[::-1]
            output.extend(val)
        return output