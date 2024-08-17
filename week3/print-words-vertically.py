class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        words = s.split()
        max_len = 0
        for word in words:
            max_len = max(max_len ,len(word))
            
        output =[""]*max_len
        for i in range(len(words)):
            for j in range(len(words[i])):
                output[j] +=words[i][j]
            if max_len - len(words[i]) !=0:
                for k in range(len(words[i]),max_len):
                    output[k] +=" "
        # print(output)
        ans =[]
        for word in output:
            ans.append(word.rstrip())
        return ans