from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


def llen(l: Optional[ListNode]) -> int:
    if l is None:
        return 0
    c = 0
    p = l
    while p is not None:
        p = p.next
        c += 1
    return c


class Solution:
    def addTwoNumbersRec(
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

    def addTwoNumbersIt(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2

        if llen(l1) < llen(l2):
            return self.addTwoNumbersRec(l2, l1)

        p1 = l1
        p2 = l2
        carry: bool = False

        while p1 is not None:
            # Calculate the sum for current position
            temp = p1.val

            if p2 is not None:
                temp += p2.val
                p2 = p2.next

            if carry:
                temp += 1

            rest, nval = divmod(temp, 10)
            carry = rest > 0
            p1.val = nval

            # Move to next node or handle end of list
            if p1.next is not None:
                p1 = p1.next
            else:
                # We're at the last node of l1
                if carry:
                    p1.next = ListNode(1)
                break

        return l1
