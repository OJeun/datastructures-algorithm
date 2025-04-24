# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.populate_stack(root)

    def populate_stack(self, temp):
        while temp:
            self.stack.append(temp)
            temp = temp.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.populate_stack(node.right)
        return node.val

    def hasNext(self) -> bool:
        return True if self.stack else False


        

