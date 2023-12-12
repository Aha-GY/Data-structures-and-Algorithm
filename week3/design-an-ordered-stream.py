class OrderedStream:

    def __init__(self, n: int):
        self.stream =[]
        self.j =1

    def insert(self, idKey: int, value: str) -> List[str]:
        output = []
        self.stream.append([idKey,value])
        self.stream.sort()
        for i in range(len(self.stream)):
            if self.j == self.stream[i][0]:
                output.append(self.stream[i][1])
                self.j += 1            
        return output

