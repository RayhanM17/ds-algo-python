class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        
        def helper(node, path):
            
            left_path = path
            
            right_path = path
            
            if node.left:
            
                left_path = helper(node.left, left_path + 1)
                
            if node.right:
            
                right_path = helper(node.right, right_path + 1)
            
                
            return max(left_path, right_path)
        
        return helper(root, 1)
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)
        return max(l, r) + 1

