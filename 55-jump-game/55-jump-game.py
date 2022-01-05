class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [False for _ in range(n)]
        visited[0] = True
        for i in range(n - 1):
            if not visited[i]:
                continue
            for k in range(nums[i], 0, -1):
                if visited[min(i + k, n - 1)]:
                    break
                visited[min(i + k, n - 1)] = True
        print(visited)
        return visited[n - 1]