# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = None
        while head != None:
            node = ListNode()
            node.next = node1
            node.val = head.val
            node1 = node
            head = head.next
        return node1

        