class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        str_to_list = path.split("/")
        
        for directory in str_to_list:
            if directory == "." or directory == "":
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            else: # file or folder name
                stack.append(directory)

        return "/" + "/".join(stack)
 
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

        