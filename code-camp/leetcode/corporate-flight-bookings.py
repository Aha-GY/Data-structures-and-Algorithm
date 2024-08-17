class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefix =[0]*n
        prefix.append(0)
        prefix.append(0)
        for book in bookings:
            prefix[book[0]] += book[2]
            prefix[book[1]+1] -= book[2]
        curr = 0
        prefix.pop(0)
        for i in range(len(prefix)):
            curr += prefix[i]
            prefix[i] = curr
        prefix.pop()
        return prefix