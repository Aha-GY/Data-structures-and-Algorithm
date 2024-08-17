n,t = map(int,input().split())

class UnionFind:
    def __init__(self, n):
        self.n  = n
        self.root =[i for i in range(n)] 
        self.representation = [[i, i, 1] for i in range(n)]

    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.representation[rootX][2] > self.representation[rootY][2]:
                self.root[rootY] = rootX
                self.representation[rootX][2] += self.representation[rootY][2]
                self.representation[rootX][0] = min(self.representation[rootX][0], self.representation[rootY][0])
                self.representation[rootX][1] = max(self.representation[rootX][1], self.representation[rootY][1])
            else:
                self.root[rootX] = rootY
                self.representation[rootY][2] += self.representation[rootX][2]  
                self.representation[rootY][0] = min(self.representation[rootX][0], self.representation[rootY][0])
                self.representation[rootY][1] = max(self.representation[rootX][1], self.representation[rootY][1]) 


uf = UnionFind(n)

for _ in range(t):
    accepted = input().split()
    if accepted[0] == "union":
        uf.union(int(accepted[1]) - 1, int(accepted[2])- 1)
    else:
        root = uf.find(int(accepted[1])- 1)
        minim, maxim, size = uf.representation[root]
        print(minim+ 1, maxim+ 1, size)