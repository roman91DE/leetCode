from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        lpn = None
        lp1 = list1
        lp2 = list2
        head = lpn

        while lp1 and lp2:
            v1, v2 = lp1.val, lp2.val
            vmin = min(v1, v2)
            if v1 < v2:
                lp1 = lp1.next
            else:
                lp2 = lp2.next
            if lpn is None:
                lpn = ListNode(vmin)
                head = lpn
            else:
                lpn.next = ListNode(vmin)
                lpn = lpn.next
        if not head:
            if lp1:
                return lp1
            if lp2:
                return lp2
        if lp1:
            assert lpn is not None
            lpn.next = lp1

        if lp2:
            assert lpn is not None
            lpn.next = lp2

        return head
