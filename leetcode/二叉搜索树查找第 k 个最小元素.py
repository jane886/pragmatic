"""
假设给定的数组是 [5, 3, 6, 2, 4, null, null, 1]，其中 null 表示空节点。我们将按照以下步骤进行操作：

构建二叉搜索树：
首先，创建一个空的根节点。
遍历数组中的每个元素，按照二叉搜索树的规则将元素插入到树中。
如果当前节点为空，则将新节点插入为当前节点。
如果当前节点不为空，则根据元素的大小关系，将新节点插入为当前节点的左子节点或右子节点，直到找到合适的位置。
完成所有元素的插入后，得到一个构建好的二叉搜索树。
查找第 k 个最小元素：
我们可以使用中序遍历（Inorder Traversal）来获取有序的元素序列。
在中序遍历过程中，访问到第 k 个元素时，即为第 k 个最小元素。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBST(nums):
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    
    for i in range(1, len(nums)):
        insertNode(root, nums[i])
    
    return root

def insertNode(root, val):
    if val < root.val:
        if root.left:
            insertNode(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insertNode(root.right, val)
        else:
            root.right = TreeNode(val)

def kthSmallest(root, k):
    stack = []
    count = 0
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        count += 1
        
        if count == k:
            return curr.val
        
        curr = curr.right
    
    return None

# 示例数组
nums = [5, 3, 6, 2, 4, None, None, 1]

# 构建二叉搜索树
bst = constructBST(nums)

# 查找第 k 个最小元素
k = 3
result = kthSmallest(bst, k)
print(f"The {k}th smallest element is: {result}")


"""
在上述代码中，构建二叉搜索树和查找第 k 个最小元素的时间和空间复杂度如下：

构建二叉搜索树的时间复杂度：
遍历数组并插入每个元素的时间复杂度为 O(n)，其中 n 是数组的长度。
因此，构建整个二叉搜索树的时间复杂度为 O(n)。
构建二叉搜索树的空间复杂度：
需要使用额外的空间来存储树节点，节点数量与数组长度相同。
在最坏情况下，树的高度为 n，因此空间复杂度为 O(n)。
查找第 k 个最小元素的时间复杂度：
在最坏情况下，需要遍历整个二叉搜索树以找到第 k 个最小元素。
由于二叉搜索树是平衡的，平均情况下的时间复杂度为 O(log n)，其中 n 是树中节点的数量。但最坏情况下，树的高度为 n，因此时间复杂度为 O(n)。
查找第 k 个最小元素的空间复杂度：
在查找过程中，使用了一个栈来辅助中序遍历，栈的大小最多为树的高度。
在最坏情况下，树的高度为 n，因此空间复杂度为 O(n)。
综上所述，构建二叉搜索树的时间复杂度和空间复杂度均为 O(n)，查找第 k 个最小元素的时间复杂度和空间复杂度均为 O(n)。
"""
