class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def symmertric(lef,righ):
            if not lef and not righ: return True
            if not lef or not righ:return False
            
            return True if lef.val == righ.val and symmertric(lef.left,righ.right) and symmertric(lef.right,righ.left) else  False
        
        return  symmertric(root.left,root.right)
         