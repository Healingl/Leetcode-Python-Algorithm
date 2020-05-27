#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# @Project: Leetcode-Python-Algorithm
# @IDE: PyCharm
# @File: 21_isValidBST.py
# @Author: ZhuangYuZhou
# @E-mail: 605540375@qq.com
# @Time: 2020/5/27
# @Desc: 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True