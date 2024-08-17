class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        i =0
        ans =[]
        def helper(curr,i):
            if not curr:return None
            
            if i >= len(ans):
                ans.append([curr.val])
            elif i<len(ans):
                ans[i].append(curr.val)
            helper(curr.left,i+1)
            helper(curr.right,i+1)
        helper(root,i)
        idx =1
        while idx<len(ans):
            ans[idx] = ans[idx].copy()[::-1]
            idx +=2
        return ans
        