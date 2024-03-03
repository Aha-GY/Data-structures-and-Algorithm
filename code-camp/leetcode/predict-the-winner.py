class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(start, end):
            if start == end:
                return nums[start]
            
            score_start = nums[start] - backtrack(start + 1, end)
            score_end = nums[end] - backtrack(start, end - 1)
            
            return max(score_start, score_end)
        
        max_score = backtrack(0, len(nums) - 1)
        return max_score >= 0
