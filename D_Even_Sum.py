t = int(input())
nums= list(map(int,input().split()))
odd_num = float("inf")
if sum(nums)%2:
    for i in range(t):
        if nums[i]%2:
            odd_num = min(odd_num,nums[i])
    print(sum(nums)-odd_num)

else:
    print(sum(nums))


import sys

# Set new recursion limit
# Function to accept matrix input
def accept_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix





# Example usage:
rows, cols = map(int, input().split())  # Input the number of rows and columns
matrix = accept_matrix(rows, cols)       # Call the function to accept the matrix

# Example printing the matrix
for row in matrix:
    print(row)

sys.setrecursionlimit(new_limit)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        
        def dfs(curr_row, curr_col):
            visited.add((curr_row, curr_col))
            
            perimeter_count = 0 
            
            for cx, cy in directions:
                new_x , new_y = curr_row + cx, curr_col + cy
                
                if inbound(new_x, new_y) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    perimeter_count += dfs(new_x, new_y)
            
                if not inbound(new_x, new_y) or grid[new_x][new_y] ==0:
                    perimeter_count += 1
            
            return perimeter_count
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)