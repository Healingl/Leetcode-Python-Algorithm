#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 18_mergeTrees.py
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 1.如果当前位置的两个节点均不存在，则返回空
        if t1 is None and t2 is None:
            return None
        # 2.如果当前位置仅有一个节点存在，则返回存在的那个节点
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # 3. 如果当前位置节点均存在，则进行节点值加和并赋值给t1的节点，创建t1的左右子树，并返回t1
        t1.val += t2.val

        # 对下一个位置进行遍历
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)

        return  t1