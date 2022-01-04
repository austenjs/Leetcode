class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0 for _ in range(n)]
        if k == 0:
            return ans
        elif k > 0:
            for i in range(n):
                for j in range(1, k + 1):
                    ans[i] += code[(i + j) % n]
        else:
            for i in range(n):
                for j in range(-k, 0, -1):
                    new_index = i - j
                    if new_index < 0:
                        new_index += n
                    ans[i] += code[new_index]
        return ans