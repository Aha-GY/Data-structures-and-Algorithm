class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alien = {}
        for i, ch in enumerate(order):
            alien[ch] = i

        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            for ch1, ch2 in zip(word1, word2):
                if alien[ch1] < alien[ch2]:
                    break
                elif alien[ch1] > alien[ch2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True
