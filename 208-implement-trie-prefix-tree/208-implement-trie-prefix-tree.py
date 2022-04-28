class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end = False
    
    def is_word(self):
        return self.end
    
    def set_word(self):
        self.end = True
    
    def add_child(self, char, node):
        self.children[char] = node
        
        
    def is_child(self, char):
        return char in self.children
    
    def get_child(self, char):
        return self.children[char]

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.is_child(char):
                node = node.get_child(char)
            else:
                tmp_node = TrieNode(char)
                node.add_child(char, tmp_node)
                node = tmp_node
        node.set_word()

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not node.is_child(char):
                return False
            node = node.get_child(char)
        return node.is_word()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not node.is_child(char):
                return False
            node = node.get_child(char)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)