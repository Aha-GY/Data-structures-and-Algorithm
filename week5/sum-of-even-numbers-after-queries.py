class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even,output = defaultdict(int) ,[]
        even_sum =0
        
        for i in range(len(nums)):
            if nums[i]%2 ==0:
                even[i] = nums[i]
        even_sum = sum(even.values())
        
        for quer in queries:
            if nums[quer[1]]%2:
                nums[quer[1]] += quer[0]
                if nums[quer[1]]%2:
                    output.append(even_sum)
                else:
                    even_sum += nums[quer[1]]
                    even[quer[1]] = nums[quer[1]]
                    output.append(even_sum ) 
            else:
                nums[quer[1]] += quer[0]
                if nums[quer[1]]%2:
                    even_sum -= even[quer[1]]
                    even.pop(quer[1])
                    output.append(even_sum)
                else:
                    even_sum += quer[0]
                    even[quer[1]] = nums[quer[1]]
                    output.append(even_sum )
        return output
