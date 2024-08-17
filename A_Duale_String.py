from collections import Counter
t = int(input())
for _ in range(t):
    s = str(input())
    
    i = 0
    j = len(s)//2
    if len(s)%2:
        print("NO")
    else:
        while j< len(s):
            if s[i] != s[j]:
                print("NO")
                break
            i+=1
            j+=1

        else:
            print("YES")