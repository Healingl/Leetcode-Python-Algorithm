#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 9_maxAncestorDiff.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/18
# @Desc:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        #思路：递归加深度遍历，找左右子树的最小最大值
        def findmaxmin(node,min_,max_):
            # 如果为空，则进行最大最小值相减
            if node == None:
                return max_ - min_
            # 如果大于最大值更新
            if node.val > max_:
                max_ = node.val
            # 如果小于最小值更新
            if node.val < min_:
                min_ = node.val
            # 左右最大距离
            left_distance = findmaxmin(node.left,min_,max_)
            right_distance = findmaxmin(node.right,min_,max_)
            # 获得最终最大距离
            return max(left_distance,right_distance)
        res = findmaxmin(root,min_ = root.val,max_ = root.val)
        return res
