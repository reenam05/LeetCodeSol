class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arrP = []
        arrQ = []

        def compare(x, arr):
            if x == None:
                return
            compare(x.left, arr)
            arr.append(x.val)
            compare(x.right, arr)
            arr.append(None)
        
        compare(p, arrP)
        compare(q,arrQ)
        print(arrP)
        print(arrQ)
        if arrP == arrQ:
            return True
        else:
            return False