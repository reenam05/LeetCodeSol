class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        def minDepth(root,x, arr):
            if root == None:
                return
            else:
                x+=1
            minDepth(root.left,x, arr)
            minDepth(root.right,x, arr)
            if root.left == None and root.right == None:
                arr.append(x)
            return arr

        arr= []    
        new = minDepth(root, 0, arr)
        print(new)
        if new == None:
            return 0
        else:
            return min(new)