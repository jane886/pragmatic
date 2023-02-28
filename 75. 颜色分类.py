"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。



示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]


提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2

"""
from typing import List

from utils import ensure


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1


class Test:

    @classmethod
    def test1(cls):
        nums = [2, 0, 2, 1, 1, 0]
        r = [0, 0, 1, 1, 2, 2]
        so = Solution()
        so.sortColors(nums)
        ensure(nums, r, "测试 1")

    @classmethod
    def test2(cls):
        nums = [2, 0, 1]
        r = [0, 1, 2]
        so = Solution()
        so.sortColors(nums)
        ensure(nums, r, "测试 2")


def main():
    t = Test()
    t.test1()
    t.test2()


if __name__ == '__main__':
    main()
