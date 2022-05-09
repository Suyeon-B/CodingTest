from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toList(node: ListNode):
    List = []
    while node:
        List.append(node.val)
        node = node.next
    return List


def toLinkedList(List):
    head: ListNode = ListNode()
    curr = head
    for r in List:
        node = ListNode(r)
        curr.next = node
        curr = curr.next

    return head.next


# left~right 사이 reverse
def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    L = toList(head)
    L = L[:left-1]+list(reversed(L[left-1:right]))+L[right:]
    # print(L)
    L = toLinkedList(L)

    return L


if __name__ == '__main__':
    head = toLinkedList([1, 2, 3, 4, 5])
    left = 2
    right = 4
    assert reverseBetween(head, left, right)
