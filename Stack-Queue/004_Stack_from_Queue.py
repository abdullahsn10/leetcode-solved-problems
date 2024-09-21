class MyStack:

    def __init__(self):
        self.queue1 = deque()  # primary queue
        self.queue2 = deque()  # secondary queue for helping with pop

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        # Move all elements except the last one to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # Pop the last element (this is the stack's top)
        popped_element = self.queue1.popleft()

        # Move everything back to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        return popped_element

    def top(self) -> int:
        if not self.empty():
            return self.queue1[
                -1
            ]  # The last element in the queue represents the stack's top
        return None

    def empty(self) -> bool:
        return len(self.queue1) == 0
