def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
        
    write_pointer = 1
    
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer - 1] != nums[read_pointer]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
            
    return write_pointer
        
        