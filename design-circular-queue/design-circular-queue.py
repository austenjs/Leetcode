class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k)]
        self.size = 0
        self.head = -1
        self.tail = -1
        self.K = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail + 1) % self.K
        self.queue[self.tail] = value
        self.size += 1
        self.head = 0 if self.head == -1 else self.head
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.K
        self.size -= 1
        if self.isEmpty():
            self.head = self.tail = -1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.K


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()