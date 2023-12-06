class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        output = [0]*len(s)
        for indx,val in enumerate(indices):
            output[val] = s[indx]
        return "".join(output)