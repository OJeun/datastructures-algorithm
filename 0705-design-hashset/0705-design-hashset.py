class MyHashSet:

    def __init__(self):
        self.table_size = 769
        self.hashset = []

        for _ in range(self.table_size):
            self.hashset.append([])

    def _hash(self, key):
        return key % self.table_size

    def add(self, key: int) -> None:
        index = self._hash(key)

        if not self.contains(key):
            self.hashset[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        inner_list = self.hashset[index]

        if self.contains(key):
            inner_list.remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        inner_list = self.hashset[index]

        if key in inner_list:
            return True
        
        return False
        
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)