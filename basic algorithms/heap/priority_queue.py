class PriorityQueue:

    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def insert(self, data):
        self.insert_to_heap(data)
        self.up_heapify(self.next_index - 1)

    def remove(self):
        value  = self.remove_from_heap()
        self.down_heapify()

        return value

    def remove_from_heap(self):
        value = self.cbt[0]
        self.cbt[0], self.cbt[self.next_index - 1] = self.cbt[self.next_index - 1], self.cbt[0]
        self.cbt[self.next_index - 1 ] = None
        self.next_index -=1

        return value
    def insert_to_heap(self, data):
        if self.next_index < len(self.cbt):
            self.cbt[self.next_index] = data
            self.next_index+=1
        #else do something.

    def down_heapify(self, curr_index = 0):
        l_child = 2 * curr_index + 1
        r_child = 2 * curr_index + 2

        if self.cbt[l_child] is None and self.cbt[r_child] is None:
            return
        elif self.cbt[l_child] is None:
            min_value = min([self.cbt[r_child], self.cbt[curr_index]])
        elif self.cbt[r_child] is None:
            min_value = min([self.cbt[l_child], self.cbt[curr_index]])
        else:
            min_value = min([self.cbt[l_child], self.cbt[r_child], self.cbt[curr_index]])

        if min_value == self.cbt[curr_index]:
            #print('min value is parent, stop')
            return
        elif self.cbt[l_child] is not None and min_value == self.cbt[l_child]:
            #print(f'min value is left child {self.cbt[l_child]}')
            self.cbt[curr_index], self.cbt[l_child] = self.cbt[l_child], self.cbt[curr_index]
            #print(f'new tree is {self.cbt}')
            self.down_heapify(l_child)
        else:
            #print(f'min value is right child {self.cbt[r_child]}')
            self.cbt[curr_index], self.cbt[r_child] = self.cbt[r_child], self.cbt[curr_index]
            #print(f'new tree is {self.cbt}')
            self.down_heapify(r_child)

    def up_heapify(self, curr_index):
        parent_index = (curr_index - 1)//2

        if parent_index < 0:
            return
        if self.cbt[parent_index] > self.cbt[curr_index]:
            self.cbt[parent_index], self.cbt[curr_index] = self.cbt[curr_index], self.cbt[parent_index]
            self.up_heapify(curr_index= parent_index)

        return

# test
queue = PriorityQueue(initial_size=12)

print(f'Current Heap is {queue.cbt}')
queue.insert(10)
queue.insert(20)
queue.insert(40)
queue.insert(50)
queue.insert(30)
queue.insert(70)
queue.insert(60)
queue.insert(75)
queue.insert(15)

print(f'Current Heap is {queue.cbt}')

print('Remove minimum value from the tree')
queue.remove()
print(f'Current Heap is {queue.cbt}')

