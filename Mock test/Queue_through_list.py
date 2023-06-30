class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0
    
# Create a new queue
queue1 = Queue()

# Enqueue elements into the queue
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

# Check if the queue is empty
print(queue1.isEmpty())  # False

# Dequeue elements from the queue
print(queue1.dequeue())  # 1
print(queue1.dequeue())  # 2
print(queue1.dequeue())  # 3
print(queue1.dequeue())  # None

# Check if the queue is empty again
print(queue1.isEmpty())  # True