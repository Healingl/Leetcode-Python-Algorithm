#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 1_Check_BitTree_Balance_Leetcode_Template.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/8
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = True
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs( node ) :
            if not self.flag:
                return 0
            if not node:
                return 0
            left , right = dfs(node.left) , dfs(node.right)
            if abs(left - right ) > 1:
                self.flag = False
            return max(left , right) +1
        dfs(root)
        return self.flag