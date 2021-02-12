class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        x = None
        if self.size > 0:
            self.size -= 1
            x = self.storage.pop(0)
            return x
        return x
