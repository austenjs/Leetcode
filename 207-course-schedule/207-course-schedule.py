from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = self.create_adj_list(prerequisites)
        checked = set()
        for i in range(numCourses):
            if i in checked:
                continue
            queue = deque([i])
            visited = set()
            while queue:
                cur = queue.popleft()
                if cur == i and cur in visited:
                    return False
                elif cur in visited:
                    continue
                visited.add(cur)
                for target in adj_list[cur]:
                    queue.append(target)
            checked.add(i)
        return True
        
    def create_adj_list(self, prerequisites):
        '''
        prereq -> target
        '''
        adj_list = defaultdict(set)
        for target, prereq in prerequisites:
            adj_list[prereq].add(target)
        return adj_list