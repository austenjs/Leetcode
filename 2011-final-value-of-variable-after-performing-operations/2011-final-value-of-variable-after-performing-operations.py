symbol_to_number = {
            "--X" : -1,
            "X--" : -1,
            "++X" : 1,
            "X++" : 1
        }

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(map(lambda x : symbol_to_number[x], operations))