from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        L = self.toList(head)
        while len(L) > 1:
            s, e = L.pop(0), L.pop()
            if s != e:
                return False
        return True
