t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())

    letter = []
    if len(s) >= 2:
        letter.append(s[:2])
    i =2
    while i< len(s):
        if s[i:i+2] in letter:
            print("YES")
            break
        else:
            letter.append(s[i:i+2])
        i+=2
    else:
        print("NO")
