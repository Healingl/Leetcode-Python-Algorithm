#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 8_diameterOfBinaryTree.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/18
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0

            # 左儿子为根的子树的深度
            L = depth(node.left)

            # 右儿子为根的子树的深度
            R = depth(node.right)

            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L+R+1)

            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1




