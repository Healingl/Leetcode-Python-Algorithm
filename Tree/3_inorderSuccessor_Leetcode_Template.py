#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 3_inorderSuccessor_Leetcode_Template.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/12
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
通过中序遍历求解
找到当前节点为所求节点数，设置flag=1
当flag=1，说明上一节点已经找到，根据中序遍历顺序，当前节点就是所求节点
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:return None
        stack = []
        cur = root
        flag = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if flag:#如果前节点已经找到，当前节点就是所求节点
                    return cur
                if cur == p:#判断当前节点是否是所求节点
                    flag = 1
                cur = cur.right
        return None

