s = str(input())
k  = int(input())

ss = set(s)
if len(s) <k:
    print("impossible")
elif k <= len(ss):
    print(0)
elif k > len(ss):
    print(k - len(ss))
