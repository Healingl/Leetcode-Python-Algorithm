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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #
    def dfs_sum(self,root, bit_sum):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 2*bit_sum + root.val

        bit_sum = 2*bit_sum + root.val

        left_sum = self.dfs_sum(root.left,bit_sum)
        right_sum =  self.dfs_sum(root.right,bit_sum)

        return  left_sum+right_sum


    def sumRootToLeaf(self, root: TreeNode) -> int:

        return self.dfs_sum(root, 0)


