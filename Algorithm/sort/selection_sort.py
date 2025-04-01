def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
                
        if min_index != i:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
                
    return my_list

def selection_sort_LL(self):
    if self.length < 2:
        return
    
    current = self.head
    
    while current.next is not None:
        inner_current = current.next
        smallest = current
        while inner_current is not None:
            if inner_current.value < smallest.value:
                smallest = inner_current
            
            inner_current = inner_current.next
        if smallest != current:
            smallest.value, current.value = current.value, smallest.value
        
        current = current.next