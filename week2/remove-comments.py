class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        opened = False
        for line in source:
            if not opened:
                output.append('')
            i = 0
            while i < len(line):
                if not opened:
                    if line[i:i+2] == '//':
                        break
                    elif line[i:i+2] == '/*':
                        opened = True
                        i += 1
                    else:
                        output[-1] += line[i]
                    i += 1
                elif line[i:i+2] == '*/':
                    opened = False
                    i += 2
                else:
                    i += 1
            if not opened and output[-1] == '': output.pop()
        return output