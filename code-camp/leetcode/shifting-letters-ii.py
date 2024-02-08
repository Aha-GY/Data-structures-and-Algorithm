class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        update = [0]*(len(s)+1)
        for shift in shifts:
            if shift[2] == 0:
                update[shift[1]+1] +=1
                update[shift[0]] -=1
            else:
                update[shift[1]+1] -=1
                update[shift[0]] +=1
        moves =0
        for i in range(len(update)):
            moves += update[i]
            update[i] = moves 
        
        char = list(s)
        for i in range(len(s)):
            temp = (ord(char[i]) - ord("a") + update[i])%26
            char[i] = chr( temp  + ord("a"))
        return "".join(char)
    