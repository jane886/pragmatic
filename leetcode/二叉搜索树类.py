class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
    
    def search(self, val):
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if node is None or node.val == val:
            return node
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
        

# 前序遍历
def preorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.append(root.val)
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    return result

# 中序遍历
def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result

# 后序遍历
def postorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(postorder_traversal(root.left))
    result.extend(postorder_traversal(root.right))
    result.append(root.val)
    return result


"""
这些遍历函数都采用递归的方式实现。
对于前序遍历，先访问根节点，然后递归遍历左子树，最后递归遍历右子树。
对于中序遍历，先递归遍历左子树，然后访问根节点，最后递归遍历右子树。
对于后序遍历，先递归遍历左子树，然后递归遍历右子树，最后访问根节点。
"""


def main():
    # 创建一个二叉搜索树对象
    bst = BST()

    # 插入节点
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # 搜索节点
    result = bst.search(4)
    if result:
        print("节点值为 4 的节点存在于二叉搜索树中。")
    else:
        print("节点值为 4 的节点不存在于二叉搜索树中。")