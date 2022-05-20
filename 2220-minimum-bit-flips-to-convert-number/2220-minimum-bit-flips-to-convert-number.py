class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binary_start = ''
        binary_goal = ''
        
        while start:
            binary_start += '1' if start % 2 else '0'
            start //= 2
            
        while goal:
            binary_goal += '1' if goal % 2 else '0'
            goal //= 2
        
        while len(binary_start) < len(binary_goal):
            binary_start += '0'
        
        while len(binary_start) > len(binary_goal):
            binary_goal += '0'
        
        ans = 0
        for i in range(len(binary_start)):
            ans += binary_start[i] != binary_goal[i]
        return ans