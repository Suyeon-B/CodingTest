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


def mergeKLists(lists):
    n = len(lists)
    temp = []
    for i in range(n):
        temp += toList(lists[i])
    temp.sort()
    
    return toLinkedList(temp)


if __name__ == '__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    temp = []
    for i in range(len(lists)):
        temp.append(toLinkedList(lists[i]))
    print(mergeKLists(temp))
