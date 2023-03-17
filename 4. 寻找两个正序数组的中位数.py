"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5




提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List

from utils import ensure


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确定较短数组为 nums1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)  # 两个数组的长度
        left, right = 0, m  # 二分上下界，初始为整个 nums1 的范围

        while left <= right:
            i = (left + right) // 2  # nums1 分界线位置
            j = (m + n + 1) // 2 - i  # nums2 分界线位置

            # 找到 nums1 的右半部分的最小值和 nums2 的左半部分的最大值
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]

            # 找到 nums1 的左半部分的最大值和 nums2 的右半部分的最小值
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # 满足条件：左半部分的所有数都小于右半部分的所有数
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 判断总元素个数的奇偶性，确定中位数
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
                else:
                    return max(nums1_left_max, nums2_left_max)

            # 如果 nums1 的右半部分的最小值大于 nums2 的左半部分的最大值
            # 分界线需要左移
            elif nums1_right_min > nums2_left_max:
                right = i - 1

            # 如果 nums2 的右半部分的最小值大于 nums1 的左半部分的最大值
            # 分界线需要右移
            else:
                left = i + 1


class Test:

    @classmethod
    def test1(cls):
        nums1 = [1, 3]
        nums2 = [2]
        so = Solution()
        ensure(so.findMedianSortedArrays(nums1, nums2), 2.0, "测试 1")

    @classmethod
    def test2(cls):
        nums1 = [1, 2]
        nums2 = [3, 4]
        so = Solution()
        ensure(so.findMedianSortedArrays(nums1, nums2), 2.5, "测试 2")


def main():
    t = Test()
    t.test1()
    t.test2()


if __name__ == '__main__':
    main()
