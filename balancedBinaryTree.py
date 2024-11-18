class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balance(root, x, arr):
            if root == None:
                return
            else:
                x+=1
            balance(root.left, x , arr)
            balance(root.right, x , arr)
            if root.left == None and root.right == None:
                arr.append(x)
            return arr
        
        array = []
        depthArr = balance(root, 0, array)
        
        if depthArr == None:
            return True
        elif len(depthArr) == 1 and depthArr[0] > 1:
            return false
        else:
            a = depthArr
        
        if min(a) == max(a) or min(a) + 1 == max(a) or min(a) - 1 == max(a):
            return True
        else:
            return False