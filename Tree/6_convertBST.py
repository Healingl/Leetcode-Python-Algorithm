#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 6_convertBST.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/13
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
        self.accumulateSum = 0

    def reverse_inorder(self,root):
        """
        返序中序遍历，得到一个递减数列
        :param root:
        :return:
        """
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            # 逆中序遍历
            print(root.val)
            self.accumulateSum += root.val
            root.val = self.accumulateSum

            root = root.left

        return root

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None: return root
        self.reverse_inorder(root)
        return root
