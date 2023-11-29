class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = []
        i = 0
        
        strs.sort()
        temp = min(len(strs[0]),len(strs[-1]))
        while i < temp and strs[0][i] == strs[-1][i]:
            stack.append(strs[0][i])
            i+=1
        return "".join(stack)
            
        