# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        if N == 0:
            return None
        if N == 1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]
        root_idx_inorder = inorder.index(root_val)
        
        num_left_elements = root_idx_inorder
        num_right_elements = N - num_left_elements
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:num_left_elements + 1], inorder[:root_idx_inorder])
        root.right = self.buildTree(preorder[num_left_elements + 1:], inorder[root_idx_inorder + 1:])
        
        return root