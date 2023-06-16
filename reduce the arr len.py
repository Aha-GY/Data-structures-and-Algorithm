class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        output = []
        nums_Elm = 0
        k = 0 
        count = Counter(arr)
        
        # for j in count.values():
        #     output.append(j)
        # output = list(count.values)
        # output.sort(reverse = True )
        output = sorted(count.values(),reverse = True)
       
        for i in output:
            if i + k < len(arr)//2:
                nums_Elm +=1
                k = i +k 
                continue 
            break 
        return (nums_Elm +1)


       