class TrieNode:

    def __init__(self):
        self.children = {}
        self.termination = False

class TrieTree:

    def __init__(self):
        self.head = TrieNode()

    def add(self, word):

        char_idx = 0
        curr_node = self.head
        while True:
            char = word[char_idx]
            # print('curr node childrens', curr_node.children)
            if char not in curr_node.children:
                # add all chars as new nodes
                while char_idx < len(word):
                    # print('add new node for ', word[char_idx])
                    node = TrieNode()
                    curr_node.children[word[char_idx]] = node
                    curr_node   = curr_node.children[word[char_idx]]
                    char_idx    += 1
                curr_node.termination = True
                break
            else:
                # print('found before')
                curr_node = curr_node.children[char]
                char_idx+=1

    def is_exist(self, word):

        char_idx    = 0
        curr_node   = self.head

        while char_idx < len(word):
            if word[char_idx] in curr_node.children:
                curr_node = curr_node.children[word[char_idx]]
                # print('found char ', word[char_idx])
                char_idx+=1
            else:
                # print('search for ', word[char_idx], ' in ', curr_node.children)
                return False

        return curr_node.termination



word_to_check = 'mohamed'
validation_tree = TrieTree()

validation_tree.add(word_to_check)
print(f'check name {word_to_check}  is exist in the tree: {validation_tree.is_exist(word_to_check)}')

word_to_check = 'mohamedd'

print(f'check name {word_to_check}  is exist in the tree: {validation_tree.is_exist(word_to_check)}')

word_to_check = 'ab'
validation_tree.add(word_to_check)
print(f'check name {word_to_check}  is exist in the tree: {validation_tree.is_exist(word_to_check)}')
word_to_check = 'abbb'
validation_tree.add(word_to_check)
print(f'check name {word_to_check}  is exist in the tree: {validation_tree.is_exist(word_to_check)}')

word_to_check = 'abb'
print(f'check name {word_to_check}  is exist in the tree: {validation_tree.is_exist(word_to_check)}')
