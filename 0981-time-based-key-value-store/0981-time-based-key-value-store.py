from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if not self.timestamps[key] or timestamp < self.timestamps[key][0]:
            return ""

        index = self._binarySearch(0, len(self.values[key]) -1, self.timestamps[key], timestamp)

        return "" if index == -1 else self.values[key][index]

    def _binarySearch(self, start, end, timestamps, target):
        mid = (start + end) // 2
        if start > end:
            return -1

        if start == end:
            return start
        
        if start + 1 == end:
            if target < timestamps[end]:
                return start
            else:
                return end

        if target == timestamps[mid]:
            return mid

        if target < timestamps[mid]:
            return self._binarySearch(start, mid - 1, timestamps, target)

        if target > timestamps[mid]:
            return self._binarySearch(mid, end, timestamps, target)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)