class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        n = max(costs)+1
        stor = [0]*n
        for cost in costs:
            stor[cost] +=1
        idx = 0
        for i in range(n):
            occurans = stor[i]
            while occurans >0:# and idx < len(costs):
                costs[idx] = i
                occurans -=1
                idx +=1
        ice_cream,curr_sum = 0,0
        for cost in costs:
            curr_sum += cost
            if coins < curr_sum:
                break
            ice_cream +=1
        return ice_cream