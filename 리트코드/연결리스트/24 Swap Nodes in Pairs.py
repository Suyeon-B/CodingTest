# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def toList(self, node):
        List = []
        while node:
            List.append(node.val)
            node = node.next
        return List

    def toLinkedList(self, result):
        prev = ListNode()
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def swap(self, List):
        n = len(List)
        for i in range(1, n):
            List[i-1], List[i] = List[i], List[i-1]

        return List

    def swapPairs(self, head):
        output = self.toLinkedList(self.swap(self.toList(head)))

        return output
