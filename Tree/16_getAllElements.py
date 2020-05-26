#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 16_.py
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

    def merge(self, left, right):
        """
        合并操作
        :param left:
        :param right:
        :return:
        """

        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:  # 筛选排序将left与right最小元素按序加入新序列
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result

    def inOrder(self,root:TreeNode,order_list:list)-> list:

        stack = []
        while stack or root:
            while root:
                # pre
                stack.append(root)
                root = root.left

            root = stack.pop()
            # in
            order_list.append(root.val)
            root = root.right
        return order_list

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list:
        list1 = []
        list2 = []
        list1 = self.inOrder(root1,list1)
        list2 = self.inOrder(root2,list2)
        return self.merge(list1,list2)