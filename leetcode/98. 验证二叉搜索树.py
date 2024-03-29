"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：
输入：root = [2,1,3]
输出：true

示例 2:
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

提示：

树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # 增加 helper 方法，判断节点的值大于左子节点，小于右子节点
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if node is None:
                return True

            value = node.val
            if value <= lower or value >= upper:
                return False

            # 判断右子节点大于头节点，小于右无穷大值
            if not helper(node.right, value, upper):
                return False

            # 判断左子节点大于无穷小值，小于头节点
            if not helper(node.left, lower, value):
                return False

            return True

        return helper(root)
