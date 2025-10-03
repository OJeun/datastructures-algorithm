
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
            
            left, right = False, False

            if node.left:
                left = traverse(node.left)
                if left:
                    return True

            if node.right:
                right = traverse(node.right)
                if right:
                    return True

            return left or right
        
        return traverse(root)