#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 13_tree2str.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/25
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        if t.left is None and t.right is None:
            return str(t.val) + ""
        if t.right is None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"
