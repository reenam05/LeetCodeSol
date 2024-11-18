class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arrLeft = []
        arrRight = []

        def symmetryOne(root, arr):
            if root == None:
                return
            symmetryOne(root.left, arr)
            arr.append(root.val)
            symmetryOne(root.right,arr)
            arr.append(None)
        
        def symmetryTwo(root, arr):
            if root == None:
                return
            symmetryTwo(root.right,arr)
            arr.append(root.val)
            symmetryTwo(root.left, arr)
            arr.append(None)
        
        symmetryOne(root.left, arrLeft)
        symmetryTwo(root.right, arrRight)

        if arrLeft == arrRight:
            return True
        else:
            return False