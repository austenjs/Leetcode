class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        cur = self.root

        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        
        # * means the end of this word
        cur['*'] = word
        
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        N = len(text)
        result = []
        
        for word in words:
            trie.insert(word)
        
        for i in range(N):
            dic = trie.root
            k = 0
            
            while i + k < N and text[i + k] in dic:
                dic = dic[text[i + k]]
                if '*' in dic:
                    result.append([i, i + k])       
                k += 1   
        return result