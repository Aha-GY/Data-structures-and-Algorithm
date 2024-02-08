from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        l , sum_fru , ans = 0 ,0 ,0
        
        for r in range(len(fruits)):
            window[fruits[r]] += 1
            sum_fru += 1
            while len(window) >2:
                f = fruits[l]
                window[f] -= 1
                sum_fru -= 1
                l += 1
                if not window[f]:
                    window.pop(f)
            ans = max(ans , sum_fru)
        return ans
        