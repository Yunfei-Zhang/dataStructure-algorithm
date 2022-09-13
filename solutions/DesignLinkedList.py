class LinkedNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index == 0:
            if self.head:
                return self.head.val
        
        cur = self.head
        if cur:
            while index != 0 and cur:
                cur = cur.next
                index -= 1
            
            if cur:
                return cur.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_head = LinkedNode(val)
        if self.head == None:
            self.tail = new_head
        new_head.next = self.head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        new_tail = LinkedNode(val)
        if self.tail:
            self.tail.next = new_tail
            self.tail = new_tail
        else:  # empty linked list
            self.tail = new_tail
            self.head = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = LinkedNode(val)
            cur = self.head
            while index != 0 and cur:
                prev_node = cur
                cur = cur.next
                index -= 1
            if cur:
                new_node.next = cur
                cur = new_node
                prev_node.next = cur
            elif self.tail:
                self.tail.next = new_node
                self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        else:
            cur = self.head
            prev_node = None

            while index != 0 and cur:
                prev_node = cur
                cur = cur.next
                index -= 1
            
            if prev_node and cur:
                prev_node.next = cur.next
                if prev_node.next == None:
                    self.tail = prev_node

        

if __name__ == "__main__":
    # # test 5
    # obj = MyLinkedList()
    # obj.addAtIndex(0,10)
    # obj.addAtIndex(0,20)
    # obj.addAtIndex(1,30)
    # obj.get(0)

    # # test 7
    # obj = MyLinkedList()
    # obj.addAtHead(1)
    # obj.addAtTail(3)
    # obj.addAtIndex(1,2)
    # obj.get(1)
    # obj.deleteAtIndex(0)
    # obj.get(0)

    # # test 10
    # obj = MyLinkedList()
    # obj.addAtHead(4)
    # obj.get(1)
    # obj.addAtHead(1)
    # obj.addAtHead(5)
    # obj.deleteAtIndex(3)
    # obj.addAtHead(7)
    # obj.get(3)
    # obj.get(3)
    # obj.get(3)
    # obj.addAtHead(1)
    # obj.deleteAtIndex(4)

    # # test 11
    # obj = MyLinkedList()
    # obj.addAtHead(7)
    # obj.addAtTail(0)
    # obj.deleteAtIndex(1)
    # obj.addAtTail(5)
    # obj.addAtIndex(1,1)
    # obj.addAtIndex(2,6)
    # obj.deleteAtIndex(2)
    # obj.deleteAtIndex(1)
    # obj.addAtTail(7)
    # obj.addAtIndex(1,7)
    # obj.addAtTail(6)

    # test 60
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1,2)
    obj.get(1)
    obj.deleteAtIndex(1)
    obj.get(1)
    obj.get(3)
    obj.deleteAtIndex(3)
    obj.deleteAtIndex(0)
    obj.get(0)
    obj.deleteAtIndex(0)
    obj.get(0)