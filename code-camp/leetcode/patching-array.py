class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        tar=1
        counter=0
        i=0
        while(tar<=n and i <len(nums)):
            
            if nums[i]>tar:
                counter+=1
                tar*=2
            else:
                tar+=nums[i]
                i+=1
                
            if tar>n:
                return counter
            
        print(tar,n,counter)
        while tar<=n:
            
            counter+=1
            tar*=2
            print(tar,counter,n)
            
        return counter
        
            
            
                
        
                