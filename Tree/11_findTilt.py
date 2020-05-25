#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 11_findTilt.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/22
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.filt_sum = 0
    # 我们使用递归函数 cal_sum，在任何结点调用该函数，都会返回当前结点下面（包括其自身）的结点和。
    def cal_sum(self,root):

        # 递归终止条件
        if root is None:
            return 0
        # 该节点左子树的结点之和和右子树结点之和
        left_tree_filt = self.cal_sum(root.left)
        right_tree_filt = self.cal_sum(root.right)

        # 节点的坡度为左子树的结点之和和右子树结点之和的差的绝对值，filt_sum+=坡度  即为总坡度
        self.filt_sum = self.filt_sum + abs(left_tree_filt-right_tree_filt)

        # 返回当前结点下面（包括其自身）的结点和
        return root.val + left_tree_filt + right_tree_filt

    def findTilt(self, root: TreeNode) -> int:
        self.cal_sum(root)
        return self.filt_sum
