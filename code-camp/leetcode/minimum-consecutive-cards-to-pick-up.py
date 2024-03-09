class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)

        start = 0
        min_len = float("inf")
        dic = defaultdict(int)

        for end in range(n):
            dic[cards[end]] += 1

            while dic[cards[end]] >= 2:
                min_len = min_len if min_len <= end-start+1 else end-start+1
                dic[cards[start]] -= 1
                start += 1

        return min_len if min_len != float("inf") else -1