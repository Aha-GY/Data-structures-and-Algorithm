class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans =[]
        curr_sum =[]
        # candidates.sort()
        def backtrack(idx,deff):
            if idx >= len(candidates) or sum(curr_sum) >= target:
                if sum(curr_sum) == target:
                    ans.append(curr_sum.copy())
                return
            if deff < min(candidates):return
            
            if min(candidates) <= deff:
                curr_sum.append(candidates[idx])
                backtrack(idx,deff-candidates[idx])
                curr_sum.pop()
                backtrack(idx+1,deff)
                
        backtrack(0,target)
        return ans