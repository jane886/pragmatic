"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。





示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。


提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
from typing import List

from utils import ensure


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # // 时间复杂度O(n ^ 2) + O(nlogN)总体算下来是O(n ^ 2)
        # // 核心优化思路是先排序 + 双指针

        # 先排序，因为是不重复的组合，先排序能减少访问节点的数量
        nums.sort()
        result = []
        n = len(nums)
        # 遍历每一个数
        for i in range(n):
            # 要判断一下当前访问的值和前一个值是不是相同，相同的话跳过直接遍历下一个
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 右指针
            right = n - 1
            # 总和是0，这里的target是 left + right 的目标值
            target = -nums[i]
            # 从第二个数从左到右遍历，找到左右指针相加 =target 的两个数
            for left in range(i + 1, n):
                # 跟前面一样，跳过和前一个值相同的数
                if left > i + 1 and nums[left] == nums[left - 1]:
                    continue

                # 保持左指针小于右指针，并且从右到左移动，找到符合 target 的两个指针
                while left < right and nums[left] + nums[right] > target:
                    right -= 1

                # 这里要判断一下，如果左右指针指向同一个数重合了，可以退出循环
                if left == right:
                    break

                # 此时左右指针和=target，符合条件
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])

        return result


class Test:

    @classmethod
    def test1(cls):
        nums = [-1, 0, 1, 2, -1, -4]
        r = [[-1, -1, 2], [-1, 0, 1]]
        so = Solution()
        ensure(so.threeSum(nums), r, "测试 1")

    @classmethod
    def test2(cls):
        nums = [0, 1, 1]
        r = []
        so = Solution()
        ensure(so.threeSum(nums), r, "测试 2")

    @classmethod
    def test3(cls):
        nums = [0, 0, 0]
        r = [[0, 0, 0]]
        so = Solution()
        ensure(so.threeSum(nums), r, "测试 3")

    @classmethod
    def test4(cls):
        nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
        r = [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2],
             [-1, 0, 1]]
        so = Solution()
        ensure(so.threeSum(nums), r, "测试 4")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()
    t.test4()


if __name__ == '__main__':
    main()
