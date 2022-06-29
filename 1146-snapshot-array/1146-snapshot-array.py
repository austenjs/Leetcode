from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.states = { 0 : defaultdict(int)}
        self.length = length
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.snap_id not in self.states:
            self.states[self.snap_id] = self.states[self.snap_id - 1].copy()
        self.states[self.snap_id][index] = val

    def snap(self) -> int:
        if self.snap_id not in self.states:
            self.states[self.snap_id] = self.states[self.snap_id - 1].copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if self.snap_id not in self.states:
            self.states[self.snap_id] = self.states[self.snap_id - 1].copy()
        return self.states[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)