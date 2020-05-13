# Leetcode-Python-Algorithm
使用python刷leetcode



## 树

### 1.检查平衡性

**题目：**

实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

示例 1:

```
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
```


示例 2:

```
给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。
```

**思路：**

```
由题目想到可以通过分别检查每个节点左右子树的高度，如果两者高度只差大于1，那么它不是平衡的。而高度的计算则是一个递归问题，本题的解决思路便是在递归计算树高度的过程中判断树的平衡性。

二叉树的高度可以递归来计算：
1.如果输入的是空节点，那么返回高度值0
2.如果输入的是叶子节点，那么返回高度1
3.如果输入的是非叶子节点，那么分别计算左右子树的高度，选取其中最大者加1作为本节点的高度。
```

**解题代码：**

```
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    isBalance = True
    def getTreeHeight(self, node):
        if node == None:
            return 0

        leftHeight = self.getTreeHeight(node.left)
        rightHeight =self.getTreeHeight(node.right)

        if abs(leftHeight - rightHeight) > 1:
            self.isBalance = False

        treeHeight = max(leftHeight,rightHeight) + 1

        return treeHeight


    def isBalanced(self, root: TreeNode) -> bool:

        self.getTreeHeight(root)

        return self.isBalance
```



### 2.合法二叉搜索树

**题目：**

实现一个函数，检查一棵二叉树是否为二叉搜索树。

```
示例 1:
输入:
    2
   / \
  1   3
输出: true
```

```
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```





**思路：**

```
二叉搜索树的性质：
任意节点的键值一定大于其左子树中的每一个节点的键值，并小于其右子树中的每一个节点的键值。
暴力破解法：
对每个节点，检查其值是否大于左子树的最大值，是否小于右子树的最小值
巧妙破解法：
观察其每个节点数值变化特点，满足中序遍历规律，采用中序遍历产生列表，若为递增，则是BST
```



**解题代码：**

```

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    nodeValueList = []
    isBST = True

    def inOrder(self, node):
        if node is None:
            return

        self.inOrder(node.left)

        node_value = node.val
        self.nodeValueList.append(node_value)

        self.inOrder(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.nodeValueList = []
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        self.inOrder(root)

        for i in range(len(self.nodeValueList) - 1):
            if self.nodeValueList[i] >= self.nodeValueList[i + 1]:
                self.isBST = False
        return self.isBST
```



### 3.后继者

**题目：**

设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。

如果指定节点没有对应的“下一个”节点，则返回`null`。

示例 1:

```
输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2
```

示例 2:

```
输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

输出: null
```

**思路：**

```
通过中序遍历求解。
找到当前节点为所求节点的值，设置flag=1，
当flag=1，说明上一节点已经找到，根据中序遍历顺序，当前节点就是所求节点
```

**解题代码：**

```
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:return None
        stack = []
        cur = root
        flag = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if flag:#如果前节点已经找到，当前节点就是所求节点
                    return cur
                if cur.val == p.val:#判断当前节点是否是所求节点
                    flag = 1
                cur = cur.right
        return None
```



### 4.首个共同祖先

**题目：**

设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。

例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]

```
    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4
```

示例1：

```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输入: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
```

示例2：

```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
```

说明:

```
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
```

**思路：**

思路来自于leetcode解题方案：

```
分析：
	对于当前的根节点root
		1.若root为空，直接返回root，表示没有找到目标
		2.若root为p或q
			若左子树或右子树中含有另外一个目标节点，那么root就是最终答案，返回root
			否则，也应当返回root，表示找到了其中一个目标
		3.否则
            若左子树和右子树分别含有p、q中的一个，那么root就是最终答案，返回root
            否则
                若两子树中含有p或q中的一个，即返回那个节点，表示找到了其中一个目标
                否则返回nullptr，表示没有找到目标
整理：
	经过整理我们发现
        若root为p或q，无论子树是否含有另外一个目标，都应该返回root
        另外，当左右子树的均含有目标节点时，返回root，否则只需返回找到的目标节点或空指针


难点在于如何书写递归函数，不妨这样思考：
	假设我们从跟结点开始，采用 DFS 向下遍历，如果当前结点到达叶子结点下的空结点时，返回空；如果当前结点为 p 或 q 时，返回当前结点；
	这样，当我们令 left = self.lowestCommonAncestor(root.left, p, q) 时，如果在左子树中找到了 p 或 q，left 会等于 p 或 q，同理，right 也是一样；
	然后我们进行判断：如果 left 为 right 都不为空，则为情况 1；如果 left 和 right 中只有一个不为空，说明这两个结点在子树中，则根节点到达子树再进行寻找。
```

**解题代码：**

```
class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # 1.如果当前结点到达叶子结点下的空结点时，返回空；如果当前结点为 p 或 q 时，返回当前结点；
        if root is None or root.val == p.val or root.val == q.val:
            return root
        # 令 left = self.lowestCommonAncestor(root.left, p, q) 时，如果在左子树中找到了 p 或 q，left 会等于 p 或 q，同理，right 也是一样；
        left = self.lowestCommonAncestor(root.left,p,q)
        righ  t = self.lowestCommonAncestor(root.right,p,q)
		
		# 2.若左子树和右子树分别含有p、q中的一个，那么root就是最终答案，返回root
        if left is not None and right is not None: 
        	return root
        	
		# 3.如果 left 和 right 中只有一个不为空，说明这两个结点在子树中，则根节点到达子树再进行寻找
        if left is None:
            return right
        else:
            return left
```

### 5.二叉搜索树的最小绝对差

**题目：**

给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

```
输入：

   1
    \
     3
    /
   2

输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。 
```

提示：

- 树中至少有 2 个节点。

**思路：**

```
由于二叉搜索树的中序遍历会产生一个递增数组，因此利用中序遍历产生的二叉搜索树递增数组计算树中的最小边，可以得到树中任意两节点的差的绝对值的最小值。
```

**解题代码：**

```
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.valueList = []

    def inOrder(self,node):
        if node is None:
            return None
        self.inOrder(node.left)
        self.valueList.append(node.val)
        self.inOrder(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return None

        self.inOrder(root)

        minDistance = abs(self.valueList[0] - self.valueList[1])

        for i in range(1, len(self.valueList)-1):
            edge_distance = abs(self.valueList[i] - self.valueList[i+1])
            if edge_distance < minDistance:
                minDistance = edge_distance

        return minDistance
```

