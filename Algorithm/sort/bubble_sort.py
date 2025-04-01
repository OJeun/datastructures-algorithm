def bubble_sort(my_list):
    for i in range(len(my_list), 1, -1):
        for j in range(i - 1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                
    return my_list

def bubble_sort(self):
    if self.length < 2:
        return
    
    sorted_until = None
    
    while sorted_until != self.head:
        current = self.head
        while current.next != sorted_until:
            if current.value > current.next.value:
                current.value, current.next.value = current.next.value, current.value
            current = current.next
            
        sorted_until = current