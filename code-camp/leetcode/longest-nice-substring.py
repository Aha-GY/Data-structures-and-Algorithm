class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(string):
            for char in string:
                if char.lower() not in string or char.upper() not in string:
                    return False
            return True

        maxNice = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n):
                substring = s[i:j + 1]
                if isNice(substring) and len(substring) > len(maxNice):
                    maxNice = substring

        return maxNice
