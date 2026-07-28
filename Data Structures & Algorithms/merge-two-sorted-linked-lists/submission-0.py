# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = None
        head2 = None
        outHead = None

        while list1 != None:
            node1 = ListNode()
            node1.next = head1
            node1.val = list1.val
            head1 = node1
            list1 = list1.next
        while list2 != None:
            node2 = ListNode()
            node2.next = head2
            node2.val = list2.val
            head2 = node2
            list2 = list2.next
        while True:
            out = ListNode()
            out.next = outHead
            if head1 != None and head2 != None:
                if head1.val > head2.val:
                    out.val = head1.val
                    head1 = head1.next
                else:
                    out.val = head2.val
                    head2 = head2.next
                outHead = out
            else:
                if head1 == None and head2 == None:
                    return outHead
                elif head1 == None:
                    out.val = head2.val
                    head2 = head2.next
                elif head2 == None:
                    out.val = head1.val
                    head1 = head1.next
                outHead = out



        return outHead




            
        