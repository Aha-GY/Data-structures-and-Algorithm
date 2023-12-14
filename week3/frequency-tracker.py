class FrequencyTracker:

    def __init__(self):
        
        self.count = defaultdict(int)
        self.repation = defaultdict(int)
            
    def add(self, number: int) -> None: 
        self.repation[self.count[number]] = self.repation.get(self.count[number],1) - 1
        self.count[number] = self.count.get(number,0) +1
        self.repation[self.count[number]] = self.repation.get(self.count[number],0) + 1
        
    def deleteOne(self, number: int) -> None:
        self.repation[self.count[number]] = self.repation.get(self.count[number],1) - 1
        self.count[number] = self.count.get(number,0) -1
        self.repation[self.count[number]] = self.repation.get(self.count[number],0) + 1
        if self.count[number] <0:
            del(self.count[number])
    def hasFrequency(self, frequency: int) -> bool:
        
        return self.repation[frequency]
            