#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 17_inorderTraversal.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/26
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:

        inorderList = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorderList.append(root.val)
            root = root.right

        return inorderList