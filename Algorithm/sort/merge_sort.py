# list1 and list2 are sorted lists. This functon will merge them into one sorted list.
def merge(first_list, second_list):
    first_index = 0
    second_index = 0
    combined = []
    
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] > second_list[second_index]:
            combined.append(second_list[second_index])
            second_index += 1
        else:
            combined.append(first_list[first_index])
            first_index += 1
        
    if first_index < len(first_list):
        for i in range(len(first_list) - first_index, len(first_list)):
            combined.append(first_list[i])
    elif second_index < len(second_list):
        for j in range(len(second_list) - second_index, len(second_list)):
            combined.append(second_list[j])

    return combined


# Space complexity: O(n), time complexity: O(nlogn)
def merge_sort(my_list):
    mid_index = len(my_list)//2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

