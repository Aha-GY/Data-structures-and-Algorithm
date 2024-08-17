t = int(input())
for _ in range(t):
    l,n = map(int,input().split())
    s = str(input())
    ans =[]
    if n ==0:
      ans.append(s)
      ans.append(str(n))
      print("".join(ans))
      continue
    for i in range(l):
        if int(s[i]) < n:
            ans.append(str(n))
            ans.append(s[i:])
            break
        ans.append(s[i])
    else:
        ans.append(str(n))
    print("".join(ans))