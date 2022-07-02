# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(inorder)
        if N == 0:
            return None
        if N == 1:
            return TreeNode(inorder[0])
        
        root_val = postorder[-1]
        index = inorder.index(root_val)
        num_left_subtree = index
        num_right_subtree = N - index - 1
        
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:index], postorder[:num_left_subtree])
        root.right = self.buildTree(inorder[index + 1:], postorder[-num_right_subtree - 1:-1])
        return root