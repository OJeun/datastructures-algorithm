class RandomizedSet:

    def __init__(self):
        self.hash_dict = {}
        self.randomized_set = []
        self.index = -1

    def insert(self, val: int) -> bool:
        if val not in self.hash_dict:
            self.randomized_set.append(val)
            self.index += 1
            self.hash_dict[val] = self.index
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.hash_dict:
            removed_index = self.hash_dict.get(val)

            # Swap the elements between last and removed element
            self.randomized_set[-1], self.randomized_set[removed_index] = self.randomized_set[removed_index], self.randomized_set[-1]

            # Find a value of new element at the index that is removed 
            last_element_value = self.randomized_set[removed_index]
            self.hash_dict[last_element_value] = removed_index

            self.hash_dict.pop(val) # remove val in hash map
            self.randomized_set.pop()
            self.index -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:        
        random_index = random.randint(0, len(self.randomized_set) - 1)
        return self.randomized_set[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()