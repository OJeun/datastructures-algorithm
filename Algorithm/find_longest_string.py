def find_longest_string(string_list):
    maximum_length_word = ''
    
    for string in string_list:
        if len(string) > len(maximum_length_word):
            maximum_length_word = string
        
    return maximum_length_word