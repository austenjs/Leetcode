class MyHashSet:

    def __init__(self):
        self.ans = [False for _ in range(10**6 + 1)]

    def add(self, key: int) -> None:
        self.ans[key] = True

    def remove(self, key: int) -> None:
        self.ans[key] = False

    def contains(self, key: int) -> bool:
        return self.ans[key]        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)