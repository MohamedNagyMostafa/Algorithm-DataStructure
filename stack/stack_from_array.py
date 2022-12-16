
class Stack:

    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        if self.num_elements > len(self.arr) - 1:
            self._handle_stak_capacity_full()

        self.arr[self.next_index] = value
        self.next_index +=1
        self.num_elements +=1

    def _handle_stak_capacity_full(self):
        old_arr = self.arr
        self.arr = old_arr + [0 for _ in range(len(old_arr))]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.num_elements == 0:
            return None

        element = self.arr[self.next_index - 1]
        self.next_index -=1
        self.num_elements -=1

        return element