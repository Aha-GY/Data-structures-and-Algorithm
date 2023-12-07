class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        output = []
        for word in words:
            wordL  = word.lower()
            if wordL[0] in row1:
                temp = row1
            elif wordL[0] in row2:
                temp = row2
            else:
                temp = row3
            for ch in wordL:
                if ch not in temp:
                    break
            else:
                output.append(word)
                
        return output
        