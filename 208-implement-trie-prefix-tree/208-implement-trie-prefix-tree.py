class Trie:

    def __init__(self):
        self.trienode = TrieNode('')

    def insert(self, word: str) -> None:
        root = self.trienode
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.set_word()

    def search(self, word: str) -> bool:
        root = self.trienode
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.check_word()      

    def startsWith(self, prefix: str) -> bool:
        root = self.trienode
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True   

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False
        
    def check_word(self):
        return self.is_word
    
    def set_word(self):
        self.is_word = True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)