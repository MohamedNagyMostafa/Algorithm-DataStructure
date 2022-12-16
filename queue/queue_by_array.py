class Queue:
    def __init__(self, queue_size: int = 10):
        self.arr        = [0] * queue_size
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        if self.queue_size == len(self.arr):
            # do something
            self._handle_queue_capacity_full()

        self.arr[self.next_index] = value
        if self.front_index < 0:
            self.front_index = 0

        self.next_index = (self.next_index+1) % len(self.arr)
        self.queue_size +=1

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.front()

        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -=1

        if self.is_empty():
            self.front_index    = -1
            self.next_index     = 0

        return value

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0] * (len(self.arr) * 2)

        self.next_index = (self.next_index - 1) % len(old_arr) # point to last value
        pointer = 0         # index of new array

        while self.front_index < self.next_index:
            self.arr[pointer] = old_arr[self.front_index]
            self.front_index = (self.front_index + 1) % len(old_arr)
            pointer +=1

        # add last value
        self.arr[pointer] = old_arr[self.next_index]
        pointer +=1

        # reseating
        self.next_index = pointer
        self.front_index = 0


    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        return self.arr[self.front_index] if not self.is_empty() else None


q = Queue()

print('queue', q.arr)
print('is empty', q.is_empty())
print('front ', q.front())
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.enqueue(90)
q.enqueue(100)
print('queue', q.arr)
print('is empty', q.is_empty())
print('front ', q.front())
q.enqueue(110)
print('queue', q.arr)
print('is empty', q.is_empty())
print('front ', q.front())
q.enqueue(120)
print('queue', q.arr)
print('is empty', q.is_empty())
print('front ', q.front())

