#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 7_sumRootToLeaf.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time:  2020/5/18
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

