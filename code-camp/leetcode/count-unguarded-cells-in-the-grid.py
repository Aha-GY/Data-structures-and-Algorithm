class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid, ans = [['' for I in range(n)] for _ in range(m)], 0
        for guard in guards:
            grid[guard[0]][guard[1]] = 'G'
        for wall in walls:
            grid[wall[0]][wall[1]] = 'W'
            
        def dfs(m: int, n: int, x: int, y: int, grid: List[List[int]], idx: int) -> None:
            if x >= m or y >= n or x < 0 or y < 0 or grid[x][y] == 'G' or grid[x][y] == 'W':
                return
            
            grid[x][y] = 'V'
            dfs(m, n, x + directions[idx][0], y + directions[idx][1], grid, idx)
            
        for guard in guards:
            grid[guard[0]][guard[1]] = 'V'
            for idx in range(4):
                dfs(m, n, guard[0], guard[1], grid, idx)
            grid[guard[0]][guard[1]] = 'G'
        for row in grid:
            ans += row.count('')
        return ans
