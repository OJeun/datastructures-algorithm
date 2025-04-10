class RandomizedSet:

    def __init__(self):
        self.hash_dict = {}
        self.randomized_set = []

    def insert(self, val: int) -> bool:
        if val not in self.hash_dict:
            self.randomized_set.append(val)
            self.hash_dict[val] = len(self.randomized_set) - 1
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.hash_dict:
            removed_index = self.hash_dict[val]
            last_element_value = self.randomized_set[-1]

            self.randomized_set[removed_index] = last_element_value
            self.hash_dict[last_element_value] = removed_index

            self.randomized_set.pop()
            self.hash_dict.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:        
        random_index = random.randint(0, len(self.randomized_set) - 1)
        return self.randomized_set[random_index]
