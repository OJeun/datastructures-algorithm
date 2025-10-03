class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def isSameTree(rootTree, subTree):
            if not rootTree and not subTree:
                return True
            
            if (rootTree and not subTree) or (not rootTree and subTree) or (rootTree.val != subTree.val):
                return False
            
            left = isSameTree(rootTree.left, subTree.left)
            right = isSameTree(rootTree.right, subTree.right)

            return left and right

        def traverse(node):
            if not node:
                return False

            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True

            if node.left:
                if traverse(node.left):
                    return True

            if node.right:
                if traverse(node.right):
                    return True

            return False
        
        return traverse(root)