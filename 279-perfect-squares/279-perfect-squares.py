class Solution:
    def numSquares(self, n: int) -> int:
        candidates = [num * num for num in range(1, int(n ** 0.5) + 1)]
        queue = set()
        
        level = 0
        queue.add(n)
        
        while queue:
            level += 1
            new_queue = set()
            for remainder in queue:
                for candidate in candidates:
                    if candidate == remainder:
                        return level
                    elif candidate > remainder:
                        break
                    else:
                        new_queue.add(remainder - candidate)
            queue = new_queue
        return level