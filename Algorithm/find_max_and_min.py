def find_max_min(myList):
    minimum = maximum = myList[0]
    
    for num in myList:
        if num < minimum:
            minimum = num
            
        if num > maximum:
            maximum = num
            
    return maximum, minimum

            
    