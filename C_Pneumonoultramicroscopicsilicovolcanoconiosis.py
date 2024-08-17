t = int(input())
for _ in range(t):
    lett = str(input())
    ans = []
    if len(lett) <=10:
        print(lett)
    else:
        n = len(lett)
        ans.append(lett[0])
        ans.append(str(n-2))
        ans.append(lett[-1])
        temp = "".join(ans)
        print(temp)