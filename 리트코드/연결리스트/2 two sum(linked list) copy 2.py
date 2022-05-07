"""def main():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    num1, num2 = 0, 0
    for i in range(len(l1)-1, -1, -1):
        num1 += l1[i] * 10**i
    for i in range(len(l2)-1, -1, -1):
        num2 += l2[i] * 10**i

    SUM = list(reversed(list(str(num1+num2))))

    output = []
    for i in range(len(SUM)-1):
        output.append(ListNode(SUM[i], SUM[i+1]))

    def getList(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    return getList(output[0])


print(main())
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
            int(''.join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))
