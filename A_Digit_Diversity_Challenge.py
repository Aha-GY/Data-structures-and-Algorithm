# first , second = map(int,input().split())
# diff = second - first
# i =1
# while i <= diff:
#     first += 1
#     if len(set(str(first))) == len(list(str(first))):
#         print(first)
#         break
#     i+=1
# else:
#     print(-1)
l, r = map(int, input().split())

for x in range(l, r):
    if len(set(str(x))) == len(str(x)):
        print(x)
        break
else:
    print(-1)

