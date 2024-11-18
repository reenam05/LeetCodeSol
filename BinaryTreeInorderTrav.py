class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return arr