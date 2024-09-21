class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int) -> None:
        self.stack1.append(x)

    def dequeue(self) -> int:
        while not self.empty():
            self.stack2.append(self.stack1.pop())
        front = self.stack2.pop()
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        return front

    def front(self) -> int:
        if not self.empty():
            return self.stack1[0]

    def empty(self) -> bool:
        return True if len(self.stack1) == 0 else False
