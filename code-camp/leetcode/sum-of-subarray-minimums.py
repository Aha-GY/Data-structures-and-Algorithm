class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        
        nums.append(0)
        min_sum =0
        m_stack =[]
        for i in range(len(nums)):
            while m_stack and m_stack[-1][1] > nums[i]:
                j,m = m_stack.pop()
                if m_stack:
                    left = j - m_stack[-1][0]
                else:
                    left = j +1
                right = i -j
                min_sum = (min_sum + left*right*m)%(10**9 +7)
            m_stack.append((i,nums[i]))
        return min_sum