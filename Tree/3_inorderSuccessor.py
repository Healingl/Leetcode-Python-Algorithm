#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 3_inorderSuccessor.py
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
        # 使用两个列表，一个存储值，一个存储对象
        self.nodeValueList = []
        self.nodeItemList = []

    def inOrder(self, node):
        """
        中序遍历
        :param node:
        :return:
        """
        if node is None:
            return

        self.inOrder(node.left)

        node_value = node.val
        self.nodeValueList.append(node_value)
        self.nodeItemList.append(node)
        self.inOrder(node.right)

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:


        if p is None:
            return None

        # 如果只有一个节点则返回空
        if root.right is None and root.left is None:
            return None

        self.inOrder(root)

        p_value = p.val
        p_loc = None
        if p_value not in self.nodeValueList:
            return None


        for i in range(len(self.nodeValueList)):
            if self.nodeValueList[i] == p_value:
                p_loc = i
                break

        p_next_loc = p_loc + 1


        if p_next_loc > len(self.nodeItemList)-1:
            return None
        else:
            return self.nodeItemList[p_next_loc]


