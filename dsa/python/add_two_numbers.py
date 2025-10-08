from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def helper(
            l1: Optional[ListNode],
            l2: Optional[ListNode],
            acc: Optional[ListNode] = None,
            carry: bool = False,
        ) -> Optional[ListNode]:
            if (l1 is None) and (l2 is None) and (not carry):
                return acc

            d = 0

            if l1 is not None:
                d += l1.val
                l1 = l1.next

            if l2 is not None:
                d += l2.val
                l2 = l2.next

            if carry:
                d += 1

            carry = d > 9
            d = d % 10

            if acc is None:
                acc = ListNode(val=d)
            else:
                p = acc
                while p.next is not None:
                    p = p.next
                else:
                    p.next = ListNode(val=d)

            return helper(l1, l2, acc, carry)

        return helper(l1, l2)
