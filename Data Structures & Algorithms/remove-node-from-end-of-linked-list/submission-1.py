# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find total number of nodes
        node = head
        k = 1
        while node.next:
            k += 1
            node = node.next

        dummy = ListNode(0, head)
        node = dummy
        for i in range(k - n):
            node = node.next

        next_node = node.next
        if not next_node:
            return None
        node.next = next_node.next
        return dummy.next