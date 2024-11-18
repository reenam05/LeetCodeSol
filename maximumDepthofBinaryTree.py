class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        def inorder(root, x, arr):
            if root == None:
                return
            elif root != None:
                x+=1
            inorder(root.left, x, arr)
            inorder(root.right, x, arr)
            print(root.val)
            arr.append(x) #adds the depth of all nodes in tree in an array
            return arr
        
        y = []
        i = 0
        return max(inorder(root, i,y)) # max finds the highest number in the array