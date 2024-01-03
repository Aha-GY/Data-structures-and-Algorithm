class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        ans = 0
        counstant = skill[0] + skill[-1]
        i = 0
        j = len(skill) -1
        
        while i < j:
            temp = skill[i] + skill[j]
            if temp != counstant:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans
        
        