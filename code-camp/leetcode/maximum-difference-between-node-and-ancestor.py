class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        max_val , min_val = float("-inf"), float("inf")
        diff = 0
        def helper(root,max_val,min_val):
            if not root:return None
            nonlocal diff
            if root.val > max_val:
                max_val = root.val
            if root.val < min_val:
                min_val = root.val
            diff = max((max_val - min_val),diff)
            helper(root.left,max_val,min_val)
            helper(root.right,max_val,min_val)
        helper(root,max_val,min_val)
        return diff