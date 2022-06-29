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
        while timestamp:
            if timestamp in self.storage[key]:
                return self.storage[key][timestamp]
            timestamp -= 1
        return ""
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)