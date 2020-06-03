#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def maxSubArray(self, nums: list) -> int:

        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        len_nums = len(nums)

        max_sum = nums[0]

        # 利用nums创建dp table
        for i in range(1, len_nums):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            if nums[i] > max_sum:
                max_sum = nums[i]

        return max_sum
