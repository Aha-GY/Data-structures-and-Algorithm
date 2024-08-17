class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        crr, stack = 0, []
        for pos in range(len(S)):
            if S[pos] == '(':
                stack.append('(')
            else:
                while stack[-1] != '(':
                    crr += stack[-1]
                    stack.pop()
                stack[-1] = crr * 2 if crr else 1
                crr = 0
        return sum(stack)