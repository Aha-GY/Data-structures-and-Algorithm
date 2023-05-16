class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        i = 0
        output = 0
        current_max = 0
        while True:
            if len(grid[i]) == 0:
                break
            grid[i] = sorted(grid[i])
            current_max = max(current_max,grid[i][-1])
            grid[i].pop(-1)
            i+=1
            if i == len(grid):
                output += current_max
                current_max = 0
                i = 0
        return output
        