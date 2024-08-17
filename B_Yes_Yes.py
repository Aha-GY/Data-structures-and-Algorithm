t = int(input())
for _ in range(t):
    s = str(input())
    yes = {"Y":"e","e":"s","s":"Y"}
    if s[0] not in yes:
        print("NO")
        continue
    for i in range(1,len(s)):
        if s[i] not in yes:
            print("NO")
            break
        elif yes[s[i-1]] != s[i]:
            print("NO")
            break
    else:

        print("YES")
