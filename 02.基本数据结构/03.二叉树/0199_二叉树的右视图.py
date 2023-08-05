# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost_value_at_depth = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                max_depth = max(max_depth, depth)

                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
                
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        ans = []
        while queue:
            currentSize = len(queue)
            flag = 1
            while currentSize:
                node = queue.pop(0)
                if flag == 1:
                    ans.append(node.val)
                    flag = 0
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                currentSize -= 1
        return ans