class Solution:
    def combine(self, n, k):
        
        ans =[]
        curr_num =[]
        def backtrack(curr_num):
            if len(curr_num) == k:
                ans.append(curr_num[:])
                return        
            last = curr_num[-1] if curr_num else 0
            for i in range(last+1,n+1):
                curr_num.append(i)
                backtrack(curr_num)
                curr_num.pop()
            # if i == n: return ans
        backtrack(curr_num)
        return ans
        
        