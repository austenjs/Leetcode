class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or 0.5 * num in seen:
                return True
            seen.add(num)
        return False