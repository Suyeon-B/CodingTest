class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toLinkedList(result):
    head: ListNode = ListNode()
    curr = head
    for r in result:
        node = ListNode(r)
        curr.next = node
        curr = curr.next

    return head.next


result = [1, 2, 3, 4, 5]
temp = toLinkedList(result)
print(temp)
