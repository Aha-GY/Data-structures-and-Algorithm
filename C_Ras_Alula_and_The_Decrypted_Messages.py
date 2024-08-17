t = int(input())
for _ in range(t):
    n,t = map(int,input().split())
    incr = str(input())
    s = str(input())
    i =0
    j =0
    while i<n:
        while j<t and abs(ord(incr[i]) - ord(s[j])) < 