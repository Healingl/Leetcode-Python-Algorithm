#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 15_checkSubTree.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/25
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
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

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        if t1 and t2:
            return self.isSameTree(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
        return False