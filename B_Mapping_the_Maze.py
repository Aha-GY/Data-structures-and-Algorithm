from collections import defaultdict, Counter

node, n = map(int, input().split())
matrix = []

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

graph = defaultdict(int)
for i in range(n):
    graph[matrix[i][0]] += 1
    graph[matrix[i][1]] += 1

values = list(graph.values())
count = Counter(values)

if count[2]== len(values):
    print("ring topology")
elif values.count(1) == 2 and values.count(2) == node - 2:
    print("bus topology")
elif count[1] == node-1 and values.count(node-1) == 1:
    print("star topology")
else:
    print("unknown topology")
