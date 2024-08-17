class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        dic = {"T":0,"F":0}
        max_count =0
        left =0
        for right in range(len(answerKey)):
            dic[answerKey[right]] +=1
            min_count = min(dic["T"],dic["F"])
            while left < right and min_count > k:
                dic[answerKey[left]] -=1
                min_count = min(dic["T"],dic["F"])
                left +=1
            max_count = max(max_count , right -left+1)
        return max_count