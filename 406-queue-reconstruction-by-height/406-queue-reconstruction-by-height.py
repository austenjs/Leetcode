from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        for person in sorted(people, key = lambda x: (x[0], -x[1]), reverse = True):
            k = person[1]
            ans.insert(k, person)
        return ans