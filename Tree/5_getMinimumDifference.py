#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 5_getMinimumDifference.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/12
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
        self.valueList = []

    def inOrder(self,node):
        if node is None:
            return None
        self.inOrder(node.left)
        self.valueList.append(node.val)
        self.inOrder(node.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return None

        self.inOrder(root)

        minDistance = abs(self.valueList[0] - self.valueList[1])

        for i in range(1, len(self.valueList)-1):
            edge_distance = abs(self.valueList[i] - self.valueList[i+1])
            if edge_distance < minDistance:
                minDistance = edge_distance

        return minDistance
