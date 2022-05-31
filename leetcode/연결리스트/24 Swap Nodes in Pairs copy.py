from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def toLinkedList(self, result: int) -> ListNode:
        head: ListNode = ListNode()
        curr = head
        for r in result:
            node = ListNode(r)
            curr.next = node
            curr = curr.next

        return head.next

    def swapPairs(self, head):
        head: ListNode = ListNode()
        curr = head

        return output
