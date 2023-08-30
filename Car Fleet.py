class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
    
        for i,j in sorted(zip(position , speed))[::-1]:
            p = target - i
            t = p/j
            
            if not stack:
                stack.append(t)
            elif  stack[-1] < t:
                stack.append(t)
        return len(stack)
        