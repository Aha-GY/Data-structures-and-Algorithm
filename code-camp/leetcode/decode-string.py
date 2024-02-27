class Solution:
    def decodeString(self, s: str) -> str:
        open_br = []
        bracket = {}

        # Find matching brackets and store their indices
        for i in range(len(s)):
            if s[i] == "[":
                open_br.append(i)
            elif s[i] == "]":
                bracket[open_br.pop()] = i

        # Define decode function to recursively decode substrings
        def decode(start, end):
            ans = ""
            i = start
            while i <= end:
                if s[i].isdigit():
                    num_start = i
                    while s[i + 1].isdigit():
                        i += 1
                    num = int(s[num_start:i + 1])
                    br_start = i + 2
                    br_end = bracket[i + 1] - 1
                    ans += decode(br_start, br_end) * num
                    i = bracket[i + 1]
                elif s[i].isalpha():
                    ans += s[i]
                i += 1
            return ans

        return decode(0, len(s) - 1)
