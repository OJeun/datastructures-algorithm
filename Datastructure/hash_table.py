class HashTable:
    # The size of the map should be prime number to increase the randomness of the hash
    def __init__(self, size = 7):
        self.data_map = [None] * size

    # limit the access and to use name mangling(make it like a private)
    # _ClassName__functionName
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            container = self.data_map[index]
            for pair in container:
                if pair[0] == key:
                    return pair[1]
            
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
# O(n)
def item_in_common(list1, list2):
    my_dict = dict()
    for item in list1:
        my_dict[item] = True

    for element in list2:
        if element in my_dict:
            return True
        
    return False

def find_duplicates(nums):
    my_dict = {}
    
    for num in nums:
        my_dict[num] = my_dict.get(num, 0) + 1
    
    duplicates = []
    for num, counts in my_dict.items():
        if counts > 1:
            duplicates.append(num)
            
    return duplicates