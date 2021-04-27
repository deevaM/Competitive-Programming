class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
            
        if l2 == None:
            return l1
            
        sval = l1.val + l2.val
        if sval < 10:
            ansNode = ListNode(sval)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        else:
            rval = l1.val + l2.val-10
            ansNode = ListNode(rval)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansNode
