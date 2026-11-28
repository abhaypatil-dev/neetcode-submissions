# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.getNumberFromLL(l1)
        n2 = self.getNumberFromLL(l2)

        n = n1 + n2
        dummy = ListNode(0, None)
        node = dummy

        if not n:
            return ListNode(0, None)
            
        while n:
            digit = n % 10
            node.next = ListNode(digit, None)
            node = node.next
            n //= 10

        return dummy.next

    def getNumberFromLL(self, node):
        ans = 0
        mlp = 1
        while node:
            ans += (mlp * node.val)
            mlp *= 10
            node = node.next
        return ans