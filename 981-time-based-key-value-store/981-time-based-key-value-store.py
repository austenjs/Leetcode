from collections import defaultdict, OrderedDict
class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = {}
        self.storage[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        time = timestamp
        while time:
            if time in self.storage[key]:
                ans = self.storage[key][time]
                for t in range(time, timestamp + 1):
                    self.storage[key][time] = ans
                return ans
            time -= 1
        return ""
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)