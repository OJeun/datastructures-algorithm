from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        index = self._binarySearch(0, len(self.values[key]) -1, self.timestamps[key], timestamp)

        return "" if index == -1 else self.values[key][index]

    def _binarySearch(self, start, end, timestamps, target, ans=-1):
        mid = (start + end) // 2
        if start > end:
            return ans

        if target == timestamps[mid]:
            return mid

        if target < timestamps[mid]:
            return self._binarySearch(start, mid - 1, timestamps, target, ans)

        if target > timestamps[mid]:
            return self._binarySearch(mid + 1, end, timestamps, target, mid)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)