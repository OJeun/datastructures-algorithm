# Heap is a different kind of tree from binary search tree
# Heap is a COMPLETE binary tree
# Heap use a list
# Order doesn't matter so it is not good for sorting => Tracking max and remove that
# Max: Each node has a number that is higher than all of its descendants or Min heap

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index

        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)
        
            if left_child < len(self.heap) and self.heap[left_child] > self.heap[index]:
                max_index = left_child
            
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_index]:
                max_index = right_child
                
            if index != max_index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
    
    # Time complexity: O(logn)
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
            
# Time complexity: O(n * logk)
def find_kth_smallest(nums, k):
    max_heap = MaxHeap()

    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()
            
    return max_heap.remove()


# O(nlogn), if not use list, it will be O(n)
def stream_max(nums):
    max_heap = MaxHeap()
    max_stream = []

    for num in nums:
        max_heap.insert(num)             # O(log n)
        max_stream.append(max_heap.heap[0])  

    return max_stream