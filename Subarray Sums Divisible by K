class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod = [0] * k
        mod[0] = 1
        running_mod = 0
        for num in nums:
            running_mod = (num + running_mod) % k
            mod[running_mod] += 1

        return sum([n*(n-1)//2 for n in mod])