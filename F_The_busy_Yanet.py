from collections import Counter
t = int(input())
for _ in range(t):
  s = str(input())
  count = Counter(s)
  if count["A"] > count["B"]:
    print("A")
  else:
    print("B")