class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sumsMap,s,cnt={0:1},0,0
        for a in nums:
            s+=a
            if s-goal in sumsMap:
                cnt+=sumsMap[s-goal]
            sumsMap[s]=sumsMap.get(s,0)+1
            
        return cnt    