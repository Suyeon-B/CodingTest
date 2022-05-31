from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 디버깅용
# 연결 리스트를 파이썬 리스트로 변환


def toList(node: ListNode):
    List = []
    while node:
        List.append(node.val)
        node = node.next
    return List


# 디버깅용
# 파이썬 리스트를 연결 리스트로 변환
def toLinkedList(List):
    head: ListNode = ListNode()
    curr = head
    for r in List:
        node = ListNode(r)
        curr.next = node
        curr = curr.next

    return head.next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr, prev = head, None
    while curr:
        next, curr.next = curr.next, prev
        prev, curr = curr, next
    print(toList(prev))
    return prev


if __name__ == '__main__':
    head = toLinkedList([1, 2, 3, 4, 5])
    assert reverseList(head)
