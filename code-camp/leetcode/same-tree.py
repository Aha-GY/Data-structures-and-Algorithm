class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not q and not p:return True
            
        if not q or not p:return False
        
        if q.val == p.val and  self.isSameTree(p.left,q.left) and  self.isSameTree(p.right,q.right):return True
            