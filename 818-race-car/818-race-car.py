from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(1, 0, 0)]) # speed, position, action
        visited = set()
        
        while queue:
            speed, pos, num_action = queue.popleft()
            if (speed, pos) in visited:
                continue
            if pos == target:
                return num_action
            visited.add((speed, pos))
            queue.append((speed * 2, pos + speed, num_action + 1)) # A
            
            #  Only consider changing the direction of the car if one of the following conditions is true
            #   i.  The car is driving away from the target.
            #   ii. The car will pass the target in the next move. 
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                queue.append((-1 if speed > 0 else 1, pos, num_action + 1))
        
        return -1