class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = Stack()
        str_to_list = path.split("/")
        
        for directory in str_to_list:
            if directory == ".":
                continue
            elif directory == "":
                continue
            elif directory == "..":
                prev = stack.pop()
                if prev == None:
                    continue
            else: # file or folder name
                stack.push(directory)

        return "/" + "/".join(stack.stack_list)
 
class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def pop(self):
        if len(self.stack_list) > 0:
            return self.stack_list.pop()
        else:
            return None

        