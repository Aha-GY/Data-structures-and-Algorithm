class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # turn [x[0] for x in Counter(nums).most_common(k)] 
        output = []
        count = Counter(nums)
        for i,j in count.items():
            output.append([i,j])
        output=sorted(output,key=lambda x:-x[1])
        arr=[]
        for i in range(k):
            arr.append(output[i][0])
        return arr
        