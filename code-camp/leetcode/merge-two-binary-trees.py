class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if not root1 and not root2:return 
        
        if root1 and root2:
            root1.val += root2.val
            root1.right = self.mergeTrees(root1.right,root2.right)
            root1.left = self.mergeTrees(root1.left,root2.left)
           
        if root1:
            return root1
        else:
            return root2
        
        
        