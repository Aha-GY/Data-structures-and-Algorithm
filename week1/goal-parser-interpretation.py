class Solution:
    def interpret(self, command: str) -> str:
        
        output = []
        for i in range(len(command)):
            if command[i] == "G":
                output.append("G")
            elif command[i] == "(":
                if command[i+1] == ")":
                    output.append("o")
                else:
                    output.append("al")
        return "".join(output)
        