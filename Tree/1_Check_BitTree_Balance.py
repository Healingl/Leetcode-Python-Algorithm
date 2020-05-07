#!/usr/bin/env python
# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 1_Check_BitTree_Balance.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/7
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def getHeight(self, node):
        if node.left == None and node.right == None:
            return 1
        elif node.left != None and node.right != None:
            return max(self.getHeight(node.left),self.getHeight(node.right)) + 1
        elif node.left == None and node.right != None:
            return self.getHeight(node.right)+ 1
        elif node.left != None and node.right == None:
            return self.getHeight(node.left) + 1
        else:
            pass


    def isBalanced(self, root: TreeNode) -> bool:

        height_diff = abs(self.getHeight(root.left)-self.getHeight(root.right))
        if height_diff <= 1:
            return True
        else:
            return False



if __name__  == "__main__":
    pass