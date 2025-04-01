# Almost or already sorted array : O(n)
# unless O(n^2)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > temp:
            my_list[j + 1] = my_list[j]  
            j -= 1
        my_list[j + 1] = temp  
    return my_list

def insertion_sort(self):
        if self.length < 2:
            return
        sorted_head = self.head
        unsorted = sorted_head.next
        sorted_head.next = None
        
        while unsorted:
            next_unsorted = unsorted.next
            
            if unsorted.value <= sorted_head.value:
                unsorted.next = sorted_head
                sorted_head = unsorted
                
            else:
                temp = sorted_head
                while temp.next and unsorted.value > temp.next.value:
                    temp = temp.next
                unsorted.next = temp.next
                temp.next = unsorted
                
            unsorted = next_unsorted
            
        self.head = sorted_head
        
        while sorted_head.next:
            sorted_head = sorted_head.next
            
        self.tail = sorted_head
