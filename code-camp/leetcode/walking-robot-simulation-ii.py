class Robot:
    def __init__(self, width, height):
        from collections import deque
        self.width = height
        self.height = width
        self.directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        self.pos = (0, 0)
        self.direction_map = {(0, 1): 'East', (1, 0): 'North', (0, -1): 'West', (-1, 0): 'South'}

    def step(self, num):
        num = num % (2 * (self.width + self.height - 2))
        if not num:
            num = 2 * (self.width + self.height - 2)

        for i in range(num):
            x, y = self.pos
            i, j = self.directions[0]
            if not 0 <= x + i <= self.width - 1 or not 0 <= y + j <= self.height - 1:
                self.directions.append(self.directions.popleft())
            self.pos = x + self.directions[0][0], y + self.directions[0][-1]

    def getPos(self):
        return self.pos[1], self.pos[0]

    def getDir(self):
        return self.direction_map[self.directions[0]]
