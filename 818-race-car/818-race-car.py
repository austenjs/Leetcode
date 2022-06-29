from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(1, 0, 0)]) # speed, position, action
        visited = set()
        
        while queue:
            speed, pos, num_action = queue.popleft()
            if (speed, pos) in visited:
                continue
            if pos >= 1.5 * target:
                continue
            if pos == target:
                return num_action
            visited.add((speed, pos))
            queue.append((speed * 2, pos + speed, num_action + 1)) # A
            if speed > 0:
                new_speed = -1
            else:
                new_speed = 1
            queue.append((new_speed, pos, num_action + 1)) # R
        
        return -1