class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l=[set()]
        for x in arr:
            s1=set(x)
            if len(s1)!=len(x):continue
            for y in l:
                if y&s1:continue
                l.append(s1|y)
        return max(len(x) for x in l)