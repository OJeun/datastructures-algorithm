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

# sorted("eat")  # ['a', 'e', 't'] # O(nlogn)
# ''.join(['a', 'e', 't'])  # "aet" # O(n)

# Time Complexity = O(n * klogk), k = the length of each word
def group_anagrams(strings):
    anagrams = {}

    for word in strings:
        canonical = ''.join(sorted(word))
        if canonical not in anagrams:
            anagrams[canonical] = [word]
        else:
            anagrams_list = anagrams[canonical]
            anagrams_list.append(word)
    
    return list(anagrams.values())

# O(n)
def two_sum(nums, target):
    num_map = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], index]
            
        num_map[num] = index
        
    return []

def subarray_sum(nums, target):
    accumulated = {0: -1}
    accumulated_sum = 0

    for index, num in enumerate(nums):
        accumulated_sum += num 
        complement = accumulated_sum - target 

        if complement in accumulated:
            return [accumulated[complement] + 1, index]
        
        accumulated[accumulated_sum] = index  
    return []

def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

# O(n + m)
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    
    return pairs