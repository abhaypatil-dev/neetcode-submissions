# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        node = slow.next
        slow.next = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        node1 = head
        node2 = prev

        # while node1:
        #     print(node1.val, end=' ')
        #     node1 = node1.next
        # print()
        # while node2:
        #     print(node2.val, end=' ')
        #     node2 = node2.next

        curr = ListNode(0, None)
        i = 0
        while node1 or node2:
            if i % 2 == 0:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            
            curr = curr.next
            i += 1

# 2 4
# 8 6




