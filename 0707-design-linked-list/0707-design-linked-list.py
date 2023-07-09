class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
        self.size -= 1
