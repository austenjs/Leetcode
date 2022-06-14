# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generatePossibleCombination(1, n)
    
    def generatePossibleCombination(self, start, end):
        if start > end:
            return []
        if start == end:
            return [TreeNode(start)]

        ans = []
        for i in range(start, end + 1):
            possible_left = self.generatePossibleCombination(start, i - 1)
            possible_right = self.generatePossibleCombination(i + 1, end)
            if possible_left == []:
                for right in possible_right:
                    root = TreeNode(i)
                    root.right = right
                    ans.append(root)
            elif possible_right == []:
                for left in possible_left:
                    root = TreeNode(i)
                    root.left = left
                    ans.append(root)
            else:
                for left in possible_left:
                    for right in possible_right:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
        return ans