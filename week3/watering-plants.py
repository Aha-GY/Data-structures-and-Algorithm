class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        steps =0
        i=0
        while i <len(plants):
            cap = capacity
            while i < len(plants) and  cap >= plants[i] :
                cap -= plants[i]
                steps += 1
                i+=1
            if i != len(plants):
                steps += i*2
        return steps
        