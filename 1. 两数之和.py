"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案


进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？


"""
from typing import List

from utils import ensure


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 遍历数组
        # 2. 算出 target - 当前元素的差值
        # 3. 判断差值是否在字典出现
        # 4. 如果未出现，则用字典保存，key=当前元素，value=当前坐标
        # 5. 如果出现，返回字典里该差值的 value 和当前坐标
        d = {}
        for i, current in enumerate(nums):
            diff = target - current
            if diff in d:
                return [d[diff], i]
            else:
                d[current] = i


class Test:

    @classmethod
    def test1(cls):
        nums = [2, 7, 11, 15]
        target = 9
        s = Solution()
        ensure(s.twoSum(nums, target), [0, 1], "测试 1")

    @classmethod
    def test2(cls):
        nums = [3, 2, 4]
        target = 6
        s = Solution()
        ensure(s.twoSum(nums, target), [1, 2], "测试 2")

    @classmethod
    def test3(cls):
        nums = [3, 3]
        target = 6
        s = Solution()
        ensure(s.twoSum(nums, target), [0, 1], "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
