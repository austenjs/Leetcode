class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie(TrieNode('*'))
        for word in strs:
            trie.add_word(word)
        return trie.get_longest_prefix(len(strs))
    
class Trie:
    def __init__(self, node):
        self.root = node
    
    def add_word(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            else:
                root.children[char].inc()
            root = root.children[char]
    
    def get_longest_prefix(self, count):
        root = self.root
        ans = ''
        while True:
            if len(root.children) != 1:
                break
            new_char = list(root.children.keys())[0]
            root = root.children[new_char]
            if root.count != count:
                break
            ans += new_char
        return ans
            
    
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.count = 1
    
    def inc(self):
        self.count += 1
    
    def get_count(self):
        return self.count