class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        same = set()
        output = set()
        for back,front in zip(backs,fronts):
            if back == front :
                same.add(back)
                if back in output:
                    output.remove(back)
            else:
                output.add(back)
                output.add(front)
        ans = float("inf")
        for i in output:
            if i not in same:
                ans = min(i,ans)
        return ans if ans != float("inf") else 0