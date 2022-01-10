class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.array = [None for _ in range(n)]
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey - 1] = value
        ans = []
        while self.pointer < self.n and self.array[self.pointer] is not None:
            ans.append(self.array[self.pointer])
            self.pointer += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)