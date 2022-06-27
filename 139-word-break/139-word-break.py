class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key = len, reverse = True)
        string_to_len = {word : len(word) for word in wordDict}
        N = len(s)
        visited = set()
        def backtrack(start):
            if start == N:
                return True
            visited.add(start)
            for word in wordDict:
                start_index = s.find(word, start)
                if start_index != start:
                    continue
                len_word = string_to_len[word]
                if start + len_word in visited:
                    continue
                if backtrack(start + len_word):
                    return True
            return False
        return backtrack(0)