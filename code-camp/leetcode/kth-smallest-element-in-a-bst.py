class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans =[]
        def helper(curr):
            if not curr:return 
            
            ans.append(curr.val)
            helper(curr.left)
            helper(curr.right)
        helper(root)
        ans.sort()
        return ans[k-1]
        