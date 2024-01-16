class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        curr_card = sum(cardPoints[:k])
        max_card = curr_card
        left = k-1
        right = len(cardPoints)-1
        while left >= 0 and right >=0:
            curr_card += cardPoints[right] - cardPoints[left]
            max_card = max(max_card , curr_card)
            left -=1
            right -=1
        return max_card