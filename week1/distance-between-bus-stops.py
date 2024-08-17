class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        i = min(start,destination)
        j = max(start,destination)
        clock = 0
        while i <j :
            clock += distance[i]
            i+=1
        anti_clock = (sum(distance)-clock)
        return min(clock ,anti_clock)
        
        