t = int(input())
s = str(input())
vowel = ["a","e","i","o","u","y"]
ans = [s[0]]
for i in range(1,t):
    if s[i] not in vowel:
        ans.append(s[i])
    elif s[i-1] not in vowel:
        ans.append(s[i])
print("".join(ans))
