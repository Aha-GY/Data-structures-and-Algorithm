class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        loser , winner ={},{}
        for matche in matches:
            loser[matche[1]] = loser.get(matche[1],0) +1 
            winner[matche[0]] = winner
            
        good, best =[],[]
        for winn in winner.keys():
            if winn not in loser.keys():
                best.append(winn)
                
        for lose,count in loser.items():
            if count ==1:
                good.append(lose)
        best.sort()
        good.sort()
        return [best,good]
                
#         loser,winner =[],[]
#         for matche in matches:
#             loser.append(matche[1])
#             winner.append(matche[0])
            
#         best,good=[],[]
#         loser_c = Counter(loser)
        
#         for i in winner:
#             if i not in loser and i not in best:
#                 best.append(i)
                
#         for lose,count in loser_c.items():
#             if count ==1:
#                 good.append(lose)
#         best.sort()
#         good.sort()
        return [best,good]
                
            
        
        
        
        
        