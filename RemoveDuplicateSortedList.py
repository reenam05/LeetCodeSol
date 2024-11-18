class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = ListNode()
        dummy = first

        while head:
            if head.val != dummy.val:
                dummy.next = head
                dummy = dummy.next
            elif head.val == dummy.val and head.next == None:
                dummy.next = None
            head = head.next

        return first.next