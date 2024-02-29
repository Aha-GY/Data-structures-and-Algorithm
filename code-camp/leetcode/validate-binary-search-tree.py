class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(tree,left,right):
            if not tree: return True
            if not (tree.val > left and tree.val <right): return False
            return valid(tree.left,left,tree.val) and valid(tree.right,tree.val,right)
            
        return valid(root,float("-inf"),float("inf"))
            