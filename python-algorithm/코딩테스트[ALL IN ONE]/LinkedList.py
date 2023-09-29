class LinkedList(object):
    def __init__(self):
        self.head = None

    # 시간 복잡도: O(n)
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # 시간 복잡도: O(n)
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert_at(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            idx -= 1
            current = self.head
            for _ in range(idx):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            idx -= 1
            prev = self.head
            for _ in range(idx):
                prev = prev.next

            current = prev.next
            prev.next = current.next


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


#
#
# first = Node(1)
# second = Node(2)
# third = Node(3)
# first.next = second
# second.next = third
# first.value = 6


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
