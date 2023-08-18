class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        minBoatRequired = 0
        lastIndex = len(people) - 1
        firstIndex = 0
        while firstIndex <= lastIndex:
            if people[firstIndex] + people[lastIndex] <= limit:
                minBoatRequired += 1
                firstIndex += 1
                lastIndex -= 1
            else:
                minBoatRequired += 1
                lastIndex -= 1
        return minBoatRequired