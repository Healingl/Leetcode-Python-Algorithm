#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 12_isSubtree.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/24
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.isSub = False

    def isSameTree(self,s,t):

        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        """
        判断两个树是否相等的三个条件是与的关系，即：
        1.当前两个树的根节点值相等；
        2.并且，s 的左子树和 t 的左子树相等；
        3.并且，s 的右子树和 t 的右子树相等。
        """
        return s.val == t.val and self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        """
        判断两个树是否相等的三个条件是与的关系，即：
        1.当前两棵树相等；
        2.或者，t 是 s 的左子树；
        3.或者，t 是 s 的右子树
        """
        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

