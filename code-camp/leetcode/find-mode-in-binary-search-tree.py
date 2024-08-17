class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        count = {}
        ans =[]
        def find(root):
            if not root:
                return 
            count[root.val] = count.get(root.val, 0)+1
            find(root.right)
            find(root.left)
            
        find(root)
        max_duplicat = max(count.values())
        for key,val in count.items():
            if val == max_duplicat:
                ans.append(key)
        return ans            
    