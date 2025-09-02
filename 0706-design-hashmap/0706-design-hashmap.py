class MyHashMap:
    BUCKET_SIZE = 769

    def __init__(self):
        self.map = [[] for _ in range(self.BUCKET_SIZE)]

    def put(self, key: int, value: int) -> None:
        index = hash(key) % MyHashMap.BUCKET_SIZE
        if self.map[index]:
            for pair in self.map[index]:
                if key == pair[0]:
                    pair[1] = value
                    return

        self.map[index].append([key, value])

    def get(self, key: int) -> int:
        index = hash(key) % MyHashMap.BUCKET_SIZE
        if self.map[index]:
            for k, v in self.map[index]:
                if key == k:
                    return v
        return -1

    def remove(self, key: int) -> None:
        index = hash(key) % MyHashMap.BUCKET_SIZE
        if self.map[index]:
            for k, v in self.map[index]:
                if key == k:
                    self.map[index].remove([k, v])
    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)