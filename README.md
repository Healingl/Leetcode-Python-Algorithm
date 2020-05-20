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



### 6.把二叉搜索树转换为累加树

**题目：**

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

```
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

```



**思路：**

```
解法的关键在于应该按照节点值降序遍历所有节点，同时记录我们已经遍历过的节点值的和，并把这个和加到当前节点的值中。返序中序遍历，一个反序中序遍历的方法是通过递归实现。通过调用栈回到之前的节点，我们可以轻松地反序遍历所有节点。
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
        self.accumulateSum = 0

    def reverse_inorder(self,root):
        """
        返序中序遍历，得到一个递减数列
        :param root:
        :return:
        """
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            # 逆中序遍历
            print(root.val)
            self.accumulateSum += root.val
            root.val = self.accumulateSum

            root = root.left

        return root

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        self.reverse_inorder(root)
        return root
```



### 7. 从根到叶的二进制数之和

**题目：**

给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

以 10^9 + 7 为模，返回这些数字之和。

示例：

![img](README.assets/sum-of-root-to-leaf-binary-numbers.png)

```
输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```



**提示：**

1. 树中的结点数介于 `1` 和 `1000` 之间。
2. node.val 为 `0` 或 `1` 。



**思路：**

```
从根节点传值至叶子节点，从上至下，采用深度优先搜索算法即dfs，有递归公式：

h代表当前点深度，s(h)代表当前点二进制数（实际上是十进制表示的）,s(h-1)当前节点父节点的二进制数值，于是有递推关系，

s(h) = s(h - 1) * 2 + r.val

每次递归一层就多迭代一次公式，递归到底时就累加到全局总和里面，也可直接递归写返回值。
```



**解题代码：**

```
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs_sum(root, 0)
    def dfs_sum(self, root, base):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 2 * base + root.val
        base = 2 * base + root.val
        return self.dfs_sum(root.left, base) + self.dfs_sum(root.right, base)
```



### 8.二叉树的直径

**题目：**

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

**示例 :**
给定二叉树

```
          1
         / \
        2   3
       / \     
      4   5   
```

返回 **3**, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

**注意：**两结点之间的路径长度是以它们之间边的数目表示。



**思路：**

```
深度优先搜索算法遍历左右子树
```





**解题代码：**

```

```





### 9.节点与其祖先之间的最大差值

**题目：**

给定二叉树的根节点 root，找出存在于不同节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

示例：

![img](README.assets/2whqcep.jpg)



```
输入：[8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
解释： 
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
```

**思路：**

```

```



**解题代码：**

```

```



### 10.从先序遍历还原二叉树

**题目：**

我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。

示例1：

![img](README.assets/recover-a-tree-from-preorder-traversal.png)

```
输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]
```



示例2：

![img](README.assets/screen-shot-2019-04-10-at-114101-pm.png)

```
输入："1-2--3---4-5--6---7"
输出：[1,2,5,3,null,6,null,4,null,7]
```

**示例 3：**

![img](README.assets/screen-shot-2019-04-10-at-114955-pm.png)

```
输入："1-401--349---90--88"
输出：[1,401,null,349,88,90]
```

**提示：**

- 原始树中的节点数介于 `1` 和 `1000` 之间。
- 每个节点的值介于 `1` 和 `10 ^ 9` 之间。

**思路：**

```

```

**解题代码：**

```

```

