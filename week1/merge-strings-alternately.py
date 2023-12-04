class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merg =[]
        i=0
        while i<len(word1) and i<len(word2):
            merg.append(word1[i])
            merg.append(word2[i])
            i+=1
        if len(word1)> len(word2):
            temp = word1[i:]
            merg.append(temp)
        elif len(word2) > len(word1):
            temp = word2[i:]
            merg.append(temp)
        return "".join(merg)
            