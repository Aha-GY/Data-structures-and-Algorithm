class RandomizedSet:

    def __init__(self):
        self.name= set()

    def insert(self, val: int) -> bool:
        if val not in self.name:
            self.name.add(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.name:
            self.name.remove(val)
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(list(self.name))
