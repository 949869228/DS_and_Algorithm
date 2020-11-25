# 树的节点的定义
class TreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 树的各种遍历方式
#### 前序遍历
def preorder(root):
    """前序遍历的递归实现
    遍历顺序：根节点——左子节点——右子节点
    """
    if not root:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def preorder(root):
    """"前序遍历的迭代实现
    """"
    if not root:
        print(None)
    stack = [root]
    while stack:
        curr_node = stack.pop()
        print(curr_node.value)
        if not curr_node.left:
            stack.append(curr_node.right)
        if not curr_node.right:
            stack.append(curr_node.left)

#### 中序遍历
def inorder(root):
    """中序遍历的递归实现
    遍历顺序：左子节点——根节点——右子节点
    """
    if not root:
        return
    preorder(root.left)
    print(root.value)
    preorder(root.right)

def inorder(root):
    """中序遍历的迭代
    遍历顺序：左子节点——根节点——右子节点
    """
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val)
        root = root.right
#### 后序遍历
def postorder(root):
    """后序遍历的递归实现
    遍历顺序：左子节点——右子节点——根节点
    """
    if not root:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.value)

def postorder(root):
    """后序遍历的迭代
    遍历顺序：左子节点——右子节点——根节点
    """
    stack = []
    while stack or root:
        while root:                 # 下行循环，直到找到第一个叶子节点
            stack.append(root)
            if root.left:           # 能左就左，不能左就右
                root = root.left 
            else:
                root = root.right     
        s = stack.pop()
        print(s.val)
        #如果当前节点是上一节点的左子节点，则遍历右子节点
        if stack and s == stack[-1].left: 
            root = stack[-1].right
        else:
            root = None

#### 层次遍历（宽度优先遍历）
def BFS(root):
    if not None:
        return
    queue = [root]
    while queue:
        curr_node = queue.pop(0)
        print(queue.value)
        if not curr_node.left:
            queue.append(curr_node.left)
        if not curr_node.right:
            queue.append(curr_node.right)
#### 深度优先遍历 DFS
def DFS(root):
    if not None:
        return
    stack = [root]
    while stack:
        curr_node = stack.pop()
        print(curr_node.value)
        if not curr_node.right:
            stack.append(curr_node.right)
        if not curr_node.left:
            stack.append(curr_node.left)

# 树的基本操作
#### 二叉树的最大深度
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

#### 二叉树的最小深度
def min_depth(root):
    """递归方法
    用递归解决该题和"二叉树的最大深度"略有不同。
    主要区别在于对“结点只存在一棵子树”这种情况的处理，在这种情况下最小深度存在的路径肯定包括该棵子树上的结点.
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.right:
        return 1 + min_depth(root.left)
    if not root.left:
        return 1+ min_depth(root.right)
    return 1 + min(min_depth(root.left), min_depth(root.right))

def min_depth(root):
    """迭代方法
    分别遍历每一层，若当前层右节点无左右子节点，则返回当前深度
    """
    if not root:
        return 0
    curr_level = [root]
    next_level = []
    depth = 1
    while next_level:
        curr_node = curr_level.pop()
        if not curr_node.left and curr_node.right:
            return depth
        if curr_node.left:
            next_level.append(curr_node.left)
        if curr_node.right:
            next_level.append(curr_node.right)
        if not curr_level:
            if not next_level:
                return depth
            curr_level = next_level
            next_level = []
            depth += 1

#### 二叉树的所有路径
def traverse(root):
    if not root.left and not root.right:
        return [str(root.value)]
    left, right = [], []
    if root.left:
        left = [str(root.value) + x for x in traverse(root.left)]
    if root.right:
        right = [str(root.value) + x for x in traverse(root.right)]
    return left + right


