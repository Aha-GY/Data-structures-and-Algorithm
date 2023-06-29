class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        prev = 0

        for x in spaces:
            ans.append(s[prev:x])
            prev = x
        ans.append(s[prev:])
        return  ' '.join(ans)  


