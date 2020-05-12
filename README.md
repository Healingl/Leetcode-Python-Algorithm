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