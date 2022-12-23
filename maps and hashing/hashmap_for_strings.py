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
        self.load_factor    = 0.7

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

        # check load factor
        if self.num_entries / len(self.bucket_array) > self.load_factor:
            print('rehashing', self.num_entries / len(self.bucket_array))
            self._rehash()

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

    def _rehash(self):
        old_bucket_array    = self.bucket_array
        self.bucket_array   = [None for _ in range(len(old_bucket_array) * 2)]
        self.num_entries    = 0
        for bucket in old_bucket_array:
            while bucket is not None:
                self.put(key= bucket.key, value= bucket.value)
                bucket = bucket.next


hash_map = HashMap(7)

hash_map.put("one", 1)
print(hash_map.num_entries/len(hash_map.bucket_array))
print(len(hash_map.bucket_array))
hash_map.put("two", 2)
print(hash_map.num_entries/len(hash_map.bucket_array))
print(len(hash_map.bucket_array))
hash_map.put("three", 3)
print(hash_map.num_entries/len(hash_map.bucket_array))
print(len(hash_map.bucket_array))
hash_map.put("neo", 11)
print(hash_map.num_entries/len(hash_map.bucket_array))
print(len(hash_map.bucket_array))
hash_map.put("nea", 11)
print(hash_map.num_entries/len(hash_map.bucket_array))
print(len(hash_map.bucket_array))

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))
