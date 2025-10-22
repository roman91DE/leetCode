#!/usr/bin/env python
# coding: utf-8

from typing import Optional

# In[37]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return f(head, n)


def f(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    if head is None:
        return None

    def llen(lst: Optional[ListNode]) -> int:
        c = 0
        cur = lst
        while cur is not None:
            cur = cur.next
            c += 1
        return c

    length = llen(head)
    i = length - n
    
    newList = None
    newPtr = None
    oldPtr = head

    for j in range(length):
        if newList is None:
            newList = ListNode(oldPtr.val)
            newPtr = newList

        if i == j:
            break





    
        




# In[39]:


def print_ll(head: Optional[ListNode]) -> None:
    cur = head
    while cur is not None:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

l = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
print_ll(l)


# In[ ]:


f(l, 4)

