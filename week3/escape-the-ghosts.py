class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        for ghost in ghosts:
            x_direction = abs(ghost[0]- target[0])
            y_direction = abs(ghost[1]- target[1])
            distans = x_direction + y_direction
            if distans <= abs(target[0]) + abs(target[1]):
                return False
        return True 
        