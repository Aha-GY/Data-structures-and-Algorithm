class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tt = sorted(t)
        ss = sorted(s)
        
        if len(t) != len(s):
            return False 
        elif tt != ss :
            return False
        else :
            for i in t:
                if not  i in s:
                    return False 
            return True 
