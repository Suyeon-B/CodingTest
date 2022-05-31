def main():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class SinglyLinkedList:
        def __init__(self):
            self.head = None
            self.size = 0

        def __len__(self):
            return self.size

        def pushBack(self, key):
            new_node = ListNode(key)
            if self.size == 0:
                self.head = new_node
            else:
                tail = self.head
                while tail.next != None:
                    tail = tail.next
                tail.next = new_node
            self.size += 1

        def getList(self):
            result = []
            v = self.head
            while(v):
                result.append(v.val)
                v = v.next
            return result

    L = SinglyLinkedList()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1 = list(reversed(l1))
    l2 = list(reversed(l2))
    if len(l1) < len(l2):
        short_num = l1
        long_num = l2
    else:
        short_num = l2
        long_num = l1
    n = len(long_num)

    next_digit, two_sum = 0, 0
    for i in range(n):
        # 길이 짧은 수가 끝나기 전에는
        if i < len(short_num):
            two_sum = l1[i]+l2[i]+next_digit
            next_digit = two_sum // 10
            now = two_sum % 10
            L.pushBack(now)
        # 길이 긴 수만 남았다면
        else:
            two_sum = long_num[i]+next_digit
            next_digit = 10 // two_sum
            now = 10 % two_sum
            L.pushBack(now)

    # get result
    return L.getList()


print(main())
