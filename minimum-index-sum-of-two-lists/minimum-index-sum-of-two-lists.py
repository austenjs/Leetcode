math.inf

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map2 = {res : i for i, res in enumerate(list2)}
        
        best_res = []
        best_dist = math.inf
        for i, res in enumerate(list1):
            if res not in map2:
                continue
            if i + map2[res] < best_dist:
                best_res = [res]
                best_dist = i + map2[res]
            elif i + map2[res] == best_dist:
                best_res.append(res)
        return best_res