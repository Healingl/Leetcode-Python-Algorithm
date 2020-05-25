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


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
解题思路：DFS + 最大最小值寻找
"""


class Solution:
    def __init__(self):
        pass

    def find_minmax_diff_dfs(self, root, _min_value, _max_value):
        # 从根节点搜索最大绝对值差值
        if root is None:
            return abs(_min_value - _max_value)
        # 更新最大值和最小值
        if root.val > _max_value:
            _max_value = root.val
        elif root.val < _min_value:
            _min_value = root.val

        # 利用递归获得左右子树的最大绝对值差
        left_minmax_diff = self.find_minmax_diff_dfs(root.left, _min_value, _max_value)
        right_minmax_diff = self.find_minmax_diff_dfs(root.right, _min_value, _max_value)

        # 选择最大值进行返回
        return max(left_minmax_diff, right_minmax_diff)

    def maxAncestorDiff(self, root: TreeNode) -> int:

        if root is None:
            return 0

        return self.find_minmax_diff_dfs(root, root.val, root.val)
