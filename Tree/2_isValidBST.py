#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 2_isValidBST.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/9
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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