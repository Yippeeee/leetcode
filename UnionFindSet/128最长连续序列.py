# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 16:57
# @Author  : Yippee Song
# @Software: PyCharm

'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dict = dict()

        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)  # 左边界的连续长度
                right = hash_dict.get(num + 1, 0)  # 右边界的连续长度

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length  # 当前连续范围的左边界，设置连续长度
                hash_dict[num + right] = cur_length  # 当前连续范围的右边界，设置连续长度

        return max_length


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2, 2, 5, 101, 98, 99, 97]
    print Solution().longestConsecutive(nums)
