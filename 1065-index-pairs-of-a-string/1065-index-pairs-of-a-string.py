class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for word in words:
            ans.extend(self.findWord(text, word))
        return sorted(ans, key = lambda x: (x[0], x[1]))        
        
    def findWord(self, text, word):
        ans = []
        N = len(text)
        n = len(word)
        for i in range(N):
            match = True
            for k in range(n):
                if i + k == N or text[i + k] != word[k]:
                    match = False
                    break
            if match:
                ans.append([i, i + n - 1])
        return ans