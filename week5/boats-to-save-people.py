class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        i =0
        j = len(people)-1
        people.sort()
        while i <= j:
            temp = people[i] + people[j]
            if temp <= limit:
                i += 1
            count += 1
            j -= 1
        return count
        