class LinkedListNode:

    def __init__(self, key, value):
        self.key    = key
        self.value  = value
        self.next   = None

class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array   = [None for _ in range(initial_size)]
        self.prime          = 37
        self.num_entries    = 0

    def put(self, key, value):
        # Get hash code location by key
        index = self.get_bucket_index(key= key)
        # Check if it is existed before
        if self.bucket_array[index] is not None:
            curr_node = self.bucket_array[index]
            while curr_node is not None:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                curr_node = curr_node.next
            # Not exist, add the value
            node = LinkedListNode(key= key, value= value)
            node.next, self.bucket_array[index] = self.bucket_array[index], node
            self.num_entries +=1
        else:
            # No previous list
            node = LinkedListNode(key=key, value=value)
            self.bucket_array[index] = node
            self.num_entries += 1

    def get(self, key):
        index = self.get_bucket_index(key= key)
        curr_node = self.bucket_array[index]
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next

        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key= key)

    def get_hash_code(self, key):

        hash_code = 0
        for i, character in enumerate(key):
            hash_code+= ord(character) * (self.prime**i % len(self.bucket_array))
            # compression
            hash_code %= len(self.bucket_array)

        return hash_code % len(self.bucket_array)

    def size(self):
        return self.num_entries
