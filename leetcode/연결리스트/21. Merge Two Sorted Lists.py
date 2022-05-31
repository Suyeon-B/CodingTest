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


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 작은 값이 왼쪽에 오도록 바꿔줌
    if not list1 or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    # list1이 None이 아니면
    if list1:
        list1.next = mergeTwoLists(list1.next, list2)
    return list1


if __name__ == '__main__':
    list1 = toLinkedList([1, 2, 4])
    list2 = toLinkedList([1, 3, 4])
    assert mergeTwoLists(list1, list2)
