class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left_to_right = True
        result = []

        if not root:
            return result

        que = deque([root])

        while que:
            level = []
            length = len(que)
            for _ in range(length):
                if left_to_right:
                    node = que.popleft()
                    level.append(node.val)

                    if node and node.left:
                        que.append(node.left)
                    if node and node.right:
                        que.append(node.right)
                else:
                    node = que.pop()
                    level.append(node.val)
                    if node.right:
                        que.appendleft(node.right)
                    if node.left:
                        que.appendleft(node.left)
            left_to_right = not left_to_right
            result.append(level)
        
        return result