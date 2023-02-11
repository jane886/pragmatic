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
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            mid = len(nums) // 2
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[len(nums) // 2]


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
