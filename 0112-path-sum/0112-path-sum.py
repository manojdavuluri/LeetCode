# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        listOfTuples = [ (root, targetSum - root.val) ]
        while listOfTuples:
            node, curr_sum = listOfTuples.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                listOfTuples.append((node.right, curr_sum - node.right.val))
            if node.left:
                listOfTuples.append((node.left, curr_sum - node.left.val))
        return False
        