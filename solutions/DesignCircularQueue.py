class LinkedNode:

    def __init__(self, k) -> None:
        self.value = k
        self.prev = None
        self.next = None

    def assign_prev(self, LN) -> None:
        self.prev = LN

    def assign_next(self, LN) -> None:
        self.next = LN
    
    def assign_value(self, k) -> None:
        self.value = k

class MyCircularQueue:

    def __init__(self, k: int):
        # initiate all a queue with fixed length of k
        # take a virtual ward linkednode
        self.ward_ln = LinkedNode(-1)
        curr_ln = self.ward_ln

        for i in range(k):
            new_ln = LinkedNode(-1)

            # prev & next for the new node
            new_ln.assign_prev(curr_ln)

            # prev & next for the old node 
            curr_ln.assign_next(new_ln)

            curr_ln = new_ln

            if i == k-1:
                new_ln.assign_next(self.ward_ln)
                self.ward_ln.assign_prev(new_ln)
        
        # head and tail pointer
        self.head = self.ward_ln
        self.tail = self.ward_ln

    def enQueue(self, value: int) -> bool:
        # add the value where the tail pointer is
        if self.isFull():
            return False
        # only enQueue when it is not full
        if self.isEmpty():
            new_ln = self.tail.next
            new_ln.assign_value(value)
            self.head = new_ln
            self.tail = new_ln
        else:
            if self.tail.next == self.ward_ln:
                self.tail = self.tail.next
            self.tail.next.assign_value(value)
            self.tail = self.tail.next
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # delete the value where the head pointer is
        self.head.assign_value(-1)
        if self.isEmpty():
            self.head = self.ward_ln
            self.tail = self.ward_ln
        else:
            if self.head.next == self.ward_ln:
                self.head = self.head.next.next
            else:
                self.head = self.head.next
        return True

    def Front(self) -> int:
        # return head
        return self.head.value

    def Rear(self) -> int:
        # return tail
        return self.tail.value

    def isEmpty(self) -> bool:
        # head = tail
        if (self.tail == self.head) & (self.head.value<0):
            return True 
        else: 
            return False

    def isFull(self) -> bool:
        if self.tail.next == self.ward_ln:
            if self.tail.next.next == self.head:
                return True
        if self.tail.next == self.head:
            print('full queue')
            return True
        else:
            return False

if __name__ == "__main__":
    # # Your MyCircularQueue object will be instantiated and called as such:
    # myCircularQueue = MyCircularQueue(3)
    # myCircularQueue.enQueue(1)
    # myCircularQueue.enQueue(2)
    # myCircularQueue.enQueue(3)
    # myCircularQueue.enQueue(4)
    # myCircularQueue.Rear()
    # myCircularQueue.isFull()
    # myCircularQueue.deQueue()
    # myCircularQueue.enQueue(4)
    # myCircularQueue.Rear()

    # # test case 32
    # myCircularQueue = MyCircularQueue(6)
    # myCircularQueue.enQueue(6)
    # myCircularQueue.Rear()
    # myCircularQueue.Rear()
    # myCircularQueue.deQueue()
    # myCircularQueue.enQueue(5)
    # myCircularQueue.Rear()
    # myCircularQueue.deQueue()
    # myCircularQueue.Front()
    # myCircularQueue.deQueue()
    # myCircularQueue.deQueue()
    # myCircularQueue.deQueue()

    # test case 57
    myCircularQueue = MyCircularQueue(2)
    myCircularQueue.enQueue(1)
    myCircularQueue.enQueue(2)
    myCircularQueue.deQueue()
    myCircularQueue.enQueue(3)
    myCircularQueue.deQueue()
    myCircularQueue.enQueue(3)
    myCircularQueue.deQueue()
    myCircularQueue.enQueue(3)
    myCircularQueue.deQueue()
    myCircularQueue.Front()
